import os
import shutil

# Define the updated folder structure
structure = {
    ".github": {
        "workflows": ["ci.yml", "cd.yml"]
    },
    "configs": ["config.yaml", "logging.yaml"],
    "docker": ["Dockerfile"],
    "scripts": ["setup.sh", "deploy.sh"],
    "src": [
        "__init__.py",
        {
            "data_extraction": ["__init__.py", "extract_initial.py", "extract_refresh.py"]
        },
        {
            "embedding": ["__init__.py", "generate_embeddings_initial.py", "update_embeddings.py"]
        },
        {
            "inferencing": ["__init__.py", "inference_api.py", "query_processing.py", "reranking.py"]
        },
        "utils.py",
        "requirements.txt"
    ],
    "shared": [
        "parent_embeddings/",
        "logs/"
    ],
    "tests": ["__init__.py", "test_data_extraction.py", "test_embedding.py", "test_inferencing.py"],
}

def clear_and_create_directory(path):
    """Clear the directory if it exists, then create a new empty directory."""
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def create_files_in_directory(directory_path, files):
    """Creates files and subdirectories within the given directory path."""
    for item in files:
        if isinstance(item, str):
            # If the item ends with '/', treat it as a directory
            if item.endswith('/'):
                os.makedirs(os.path.join(directory_path, item), exist_ok=True)
            else:
                file_path = os.path.join(directory_path, item)
                open(file_path, 'w').close()
        elif isinstance(item, dict):
            # Handle nested subfolders
            for subfolder, subfiles in item.items():
                subfolder_path = os.path.join(directory_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                create_files_in_directory(subfolder_path, subfiles)

# Create the directories and files
def create_structure(base_path="."):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        clear_and_create_directory(folder_path)
        create_files_in_directory(folder_path, files)

    # Create the top-level files
    with open(os.path.join(base_path, ".gitignore"), 'w') as f:
        f.write("__pycache__/\n*.pyc\n*.pyo\n*.pyd\n.env\n.vscode/\n.idea/\n*.sublime-project\n*.sublime-workspace\nlogs/\n*.log\ndocker-compose.override.yml\n")

    with open(os.path.join(base_path, "LICENSE"), 'w') as f:
        f.write("MIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy...\n")

    with open(os.path.join(base_path, "README.md"), 'w') as f:
        f.write("# LLM Production Template\n\nA standardized, reusable template for deploying Large Language Models (LLMs) in production environments using Python.\n")

if __name__ == "__main__":
    create_structure()
    print("Folder structure and files have been created.")
