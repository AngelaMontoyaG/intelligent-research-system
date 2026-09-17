from app.vector_store import create_vector_store

"""Test function to verify the creation of the FAISS vector store."""

def main():
    vector_store = create_vector_store()

    print("Índice FAISS creado correctamente.")
    print("Tipo del almacén:", type(vector_store))


if __name__ == "__main__":
    main()