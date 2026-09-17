from langchain_huggingface import HuggingFaceEmbeddings

# Function that returns an embedding model
def create_embedding_model() -> HuggingFaceEmbeddings:
    embedding_model = HuggingFaceEmbeddings(
        # Embedding model
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )

    return embedding_model