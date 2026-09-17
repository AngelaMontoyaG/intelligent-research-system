from langchain_community.vectorstores import FAISS

from app.embeddings import create_embedding_model

# Function responsible for loading the existing FAISS index from disk
def load_vector_store():
    """Load the embedding model again because the search query must also be converted into a vector."""
    embedding_model = create_embedding_model()

    """Load the vector index with the specified embedding model and allow dangerous 
    deserialization for pickle files."""
    vector_store = FAISS.load_local(
        "data/processed/faiss_index",
        embeddings=embedding_model,
        allow_dangerous_deserialization=True,
    )

    return vector_store


# Function responsible for searching relevant information for a given query
def search_similar_chunks(
    question: str, #parameter 1: indicates that we expect to receive a text string.
    number_of_results: int = 3, #parameter 2: Indicates how many chunks we want to retrieve
):
    # The function is called and the result is the FAISS index ready to perform searches.
    vector_store = load_vector_store()

    # Search for the chunks most similar to the query
    results = vector_store.similarity_search(
        question, #The text input to search for
        k=number_of_results, #k indicates the number of results to be returned.
    )

    return results