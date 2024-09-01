import logging
import yaml
import argparse
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_path="configs/config.yaml"):
    with open(config_path, "r") as config_file:
        return yaml.safe_load(config_file)

def init_qdrant_collection(config):
    client = QdrantClient(host=config['vector_db']['host'], port=config['vector_db']['port'])
    collection_name = config['vector_db']['collection_name']

    if not client.get_collection(collection_name):
        logger.info(f"Creating collection: {collection_name}")
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=768, distance=Distance.COSINE)
        )
    else:
        logger.info(f"Collection {collection_name} already exists.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility script")
    parser.add_argument('--init_db', action='store_true', help="Initialize Qdrant vector database")
    args = parser.parse_args()

    config = load_config()

    if args.init_db:
        init_qdrant_collection(config)

