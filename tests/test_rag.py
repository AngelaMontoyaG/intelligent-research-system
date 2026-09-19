from app.rag import ask_question

# Function to test the RAG

def main():
    question = "¿Cuál es el horario de atención de Nova Hardware?"

    answer = ask_question(question)

    print("Pregunta enviada:")
    print(question)

    print("\nRespuesta:")
    print(answer)


if __name__ == "__main__":
    main()