import torch
from transformers import GPT2Tokenizer, GPT2Model
from qdrant_client import QdrantClient
from utils import load_config

def update_embeddings(data):
    config = load_config()
    tokenizer = GPT2Tokenizer.from_pretrained(config['gpt_model']['model_name'])
    model = GPT2Model.from_pretrained(config['gpt_model']['model_name'])

    client = QdrantClient(host=config['vector_db']['host'], port=config['vector_db']['port'])
    collection_name = config['vector_db']['collection_name']

    for text in data['text_column']:
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()
        client.upsert(collection_name=collection_name, points=[{'id': text, 'vector': embedding}])

    print("Embeddings update complete.")

if __name__ == "__main__":
    data = pd.read_csv('path_to_updated_data.csv')
    update_embeddings(data)

