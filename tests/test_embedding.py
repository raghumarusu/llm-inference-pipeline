from embedding.generate_embeddings_initial import generate_embeddings
from embedding.update_embeddings import update_embeddings
import pandas as pd

def test_generate_embeddings():
    data = pd.DataFrame({'text_column': ['Test text 1', 'Test text 2']})
    embeddings = generate_embeddings(data)
    assert len(embeddings) == len(data)

def test_update_embeddings():
    data = pd.DataFrame({'text_column': ['Updated text 1', 'Updated text 2']})
    update_embeddings(data)
    assert len(data) > 0

