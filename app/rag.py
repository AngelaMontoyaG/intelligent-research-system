from app.search import search_similar_chunks
from app.reranker import CohereReranker
from app.context_builder import build_context
from  app.prompt import create_rag_prompt
from app.llm import create_llm

# Function to ask a question
def ask_question(question: str) -> str:

    # Search for documents related to the question
    search_results = search_similar_chunks(question, 10)

    # Extract the document objects from FAIIS results
    candidate_documents = [
        document 
        for document, faiss_score in search_results
    ]

    # Rerank the candidate documents using Cohere
    reranker = CohereReranker()

    reranked_results = reranker.rerank(
        query=question,
        documents=candidate_documents,
        top_n=3,
    )

    # Display the reranking results
    print("\n========== COHERE RERANK ==========")

    for rank, result in enumerate(reranked_results, start=1):
        document = result["document"]
        score = result["relevance_score"]

        print(f"\n--- Resultado #{rank} ---")
        print(f"Puntuación de relevancia: {score:.4f}")
        print(f"Metadatos: {document.metadata}")
        print("Contenido:")
        print(document.page_content)

    print("\n===================================\n")


    # Extract the best ranked documents
    relevant_documents = [
        result["document"]
        for result in reranked_results
    ]

    # Build the context
    context = build_context(relevant_documents)

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