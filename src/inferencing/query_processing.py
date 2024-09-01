from transformers import GPT2Tokenizer, GPT2Model
import torch
from utils import load_config

def process_query(query):
    config = load_config()
    tokenizer = GPT2Tokenizer.from_pretrained(config['gpt_model']['model_name'])
    model = GPT2Model.from_pretrained(config['gpt_model']['model_name'])

    inputs = tokenizer(query, return_tensors="pt")
    outputs = model(**inputs)
    query_embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    return query_embedding

