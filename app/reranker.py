import os

import cohere
from dotenv import load_dotenv


load_dotenv()

# Reorders documents according to their relevance
class CohereReranker:

    def __init__(
        self,
        model: str = "rerank-v4.0-fast"
    ):
        api_key = os.getenv("COHERE_API_KEY")

        if not api_key:
            raise ValueError(
                "No se encontró COHERE_API_KEY. "
                "Verifica la configuración de tu archivo .env."
            )

        self.client = cohere.ClientV2(
            api_key=api_key
        )

        self.model = model

    def rerank(
        self,
        query: str,
        documents: list,
        top_n: int = 3
    ) -> list:
        """
        Receives a query and documents from LangChain.
        Returns the top-ranked documents, along with their relevance scores.
        """

        if not isinstance(query, str) or not query.strip():
            raise ValueError(
                "La consulta debe ser un texto no vacío."
            )

        if top_n < 1:
            raise ValueError(
                "top_n debe ser mayor o igual a 1."
            )

        if not documents:
            return []

        # Extract the content of the documents
        valid_documents = []

        for document in documents:
            content = document.page_content

            if isinstance(content, str) and content.strip():
                valid_documents.append(document)

        if not valid_documents:
            return []

        # Obtain the text that Cohere will receive
        texts = [
            document.page_content
            for document in valid_documents
        ]

        # Request the reorganization
        response = self.client.rerank(
            model=self.model,
            query=query,
            documents=texts,
            top_n=min(top_n, len(texts))
        )

        # Associate each result with its original document.
        results = []

        for item in response.results:
            results.append({
                "document": valid_documents[item.index],
                "relevance_score": item.relevance_score
            })

        return results
