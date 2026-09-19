from app.prompt import create_rag_prompt
from app.llm import create_llm
from app.search import search_similar_chunks
from app.context_builder import build_context

def main():
    # Define the question
    question = "¿Cuánto tiempo dura la garantía"

    # Searches for the chunks
    documents = search_similar_chunks(question, 3)

    # Build the context
    context = build_context(documents)

    # Creates the ChatPromptTemplate and returns it
    prompt = create_rag_prompt()
    # Create the ChatGroq model
    llm = create_llm()

    # The LangChain | means passing the output of the first component as input to the second component
    chain = prompt | llm

    # Prepares the prompt by sending the context and the question
    response = chain.invoke(
        {
            "context": context,
            "question": question,
        }
    )

    print("Respuesta del modelo:\n")
    print(response.content)


if __name__ == "__main__":
    main()