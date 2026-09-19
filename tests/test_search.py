from app.search import search_similar_chunks


def main():
    # define the question
    question = "¿En qué horario puedo llamar a Nova Hardware?"

    # execute the search
    results = search_similar_chunks(
        question,
        number_of_results=6,
    )

    print("Pregunta:", question)
    print("Cantidad de resultados:", len(results))

    for index, document in enumerate(results, start=1):
        print(f"\n--- Resultado {index} ---")
        print(document.page_content)


if __name__ == "__main__":
    main()