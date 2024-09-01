from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2Model
from qdrant_client import QdrantClient
from utils import load_config

app = FastAPI()

config = load_config()
tokenizer = GPT2Tokenizer.from_pretrained(config['gpt_model']['model_name'])
model = GPT2Model.from_pretrained(config['gpt_model']['model_name'])

client = QdrantClient(host=config['vector_db']['host'], port=config['vector_db']['port'])
collection_name = config['vector_db']['collection_name']

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    results: list

@app.post("/query", response_model=QueryResponse)
async def query_vector_db(request: QueryRequest):
    inputs = tokenizer(request.query, return_tensors="pt")
    outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()

    # Retrieve similar embeddings from Qdrant
    search_result = client.search(
        collection_name=collection_name,
        query_vector=query_embedding,
        limit=5
    )

    results = [result['id'] for result in search_result]
    return QueryResponse(results=results)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

