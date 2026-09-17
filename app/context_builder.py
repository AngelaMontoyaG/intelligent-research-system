# Receives the list of results retrieved by FAISS and will return a text string
def build_context(documents) -> str:
    # temporarily stores the text of each document.
    context_parts = []
    """document represents the current chunk
    index represents the number of document
    start=1 makes the numbering start at 1"""
    for index, document in enumerate(documents, start=1):
        context_parts.append(
            f"[Fragmento {index}]\n{document.page_content}"
        )

    #join de fragments
    #join() joins all elements of the list using that separator
    context = "\n\n---\n\n".join(context_parts)

    return context