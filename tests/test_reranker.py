
from langchain_core.documents import Document

from app.reranker import CohereReranker


def main():
    # Define question
    query = "¿Cuánto tarda una inspección por garantía?"

    # Create documents for test
    documents = [
        Document(
            page_content=(
                "La tienda atiende de lunes a viernes "
                "de 8:00 a. m. a 5:00 p. m."
            ),
            metadata={"source": "horarios.pdf"}
        ),
        Document(
            page_content=(
                "Las inspecciones de garantía tardan "
                "entre 3 y 5 días hábiles."
            ),
            metadata={"source": "garantias.pdf"}
        ),
        Document(
            page_content=(
                "Los productos nuevos tienen una "
                "garantía de doce meses."
            ),
            metadata={"source": "productos.pdf"}
        ),
        Document(
            page_content=(
                "Los clientes pueden consultar el "
                "estado de sus solicitudes de servicio."
            ),
            metadata={"source": "servicio.pdf"}
        )
    ]

    # Create reranker.
    reranker = CohereReranker()

    # Reorder the documents
    results = reranker.rerank(
        query=query,
        documents=documents,
        top_n=3
    )

    # Show results
    print(f"\nConsulta: {query}")
    print(f"Documentos originales: {len(documents)}")
    print(f"Documentos devueltos: {len(results)}")
    print("\n--- RESULTADOS DEL RERANKING ---")

    for position, result in enumerate(results, start=1):
        document = result["document"]
        score = result["relevance_score"]

        print(f"\nPosición: {position}")
        print(f"Puntuación: {score:.4f}")
        print(f"Fuente: {document.metadata['source']}")
        print(f"Contenido: {document.page_content}")


if __name__ == "__main__":
    main()
