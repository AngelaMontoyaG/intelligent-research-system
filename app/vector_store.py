import json
from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.embeddings import create_embedding_model


def create_vector_store():
    # Configuration of input (chunks) and output (FAISS index) paths
    input_path = Path("data/processed/chunks.json")
    output_path = Path("data/processed/faiss_index")

    # Loading and parsing of the JSON file
    chunks_data = json.loads(
        input_path.read_text(encoding="utf-8")
    )

    # Extraction of the plain text list
    texts = [
        chunk["text"]
        for chunk in chunks_data
    ]

    # Initialization of the embedding model
    embedding_model = create_embedding_model()

    #Transformation of texts to vectors and construction of the FAISS index
    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embedding_model,
    )

    # Save generated vector index to target directory
    vector_store.save_local(str(output_path))

    return vector_store