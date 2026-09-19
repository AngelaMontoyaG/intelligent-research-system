from app.search import search_similar_chunks
from app.context_builder import build_context
from  app.prompt import create_rag_prompt
from app.llm import create_llm

# Function to ask a question
def ask_question(question: str) -> str:

    # Search for documents related to the question
    documents = search_similar_chunks(question, 3)

    # Build the context
    context = build_context(documents)

    # Create the prompt and the model
    promt = create_rag_prompt()
    llm = create_llm()

    # The LangChain | means passing the output of the first component as input to the second component
    chain = promt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content