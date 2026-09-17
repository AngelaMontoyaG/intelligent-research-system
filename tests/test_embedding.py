from pathlib import Path
import json
from app.embeddings import create_embedding_model


def main():
    input_path = Path("data/processed/chunks.json")

    #loads the content of the JSON file
    chunks_data = json.loads(
        input_path.read_text(encoding="utf-8")
    )

    #Extracts only the plain text from each dictionary in 'chunks_data'
    texts = [
        chunk["text"]
        for chunk in chunks_data
    ]

    # Initializes the embedding model
    embedding_model = create_embedding_model()

    # generates the vectors in batch (batch embedding)
    vectors = embedding_model.embed_documents(texts)


    print("Cantidad de chunks:", len(texts))
    print("Cantidad de vectores:", len(vectors))
    print("Dimensiones de cada vector:", len(vectors[0]))
    print("Primeros cinco valores:", vectors[0][:5])


if __name__ == "__main__":
    main()