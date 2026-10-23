import os
import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

# Verify that the API key exists
if not api_key:
    raise ValueError("No se encontró COHERE_API_KEY en el archivo .env")

# Initialize the Cohere V2 client using the API key
co = cohere.ClientV2(api_key=api_key)

# Define query
consulta = "¿Cuánto tarda una inspección por garantía?"

# Test documents
documentos = [
    "La tienda atiende de lunes a viernes de 8:00 a. m. a 5:00 p. m.",
    "Las inspecciones de garantía tardan entre 3 y 5 días hábiles.",
    "Los productos nuevos tienen una garantía de doce meses.",
    "Los clientes pueden consultar el estado de sus solicitudes."
]

# Send the query and documents to Cohere's Rerank model
respuesta = co.rerank(
    model="rerank-v4.0-fast",
    query=consulta,
    documents=documentos,
    top_n=3 # Limiting to the top 3 results
)

# Print results and their respective scores
for resultado in respuesta.results:
    documento = documentos[resultado.index]

    print(f"\nPuntuación: {resultado.relevance_score:.4f}")
    print(f"Documento: {documento}")
