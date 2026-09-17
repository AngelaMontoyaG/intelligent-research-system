from app.context_builder import build_context
from app.search import search_similar_chunks

"""Test script to verify the creation and formatting of the retrieved context."""

def main():
    # define the question
    question = "¿Cuánto tiempo dura la garantía?"

    # execute the search
    documents = search_similar_chunks(
        question,
        number_of_results=3,
    )

    # build the formatted context from retrieved documents
    context = build_context(documents)

    print("Contexto generado:\n")
    print(context)


if __name__ == "__main__":
    main()