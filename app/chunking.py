from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text_into_chunks(text: str) -> list[str]:

    # Object containing the text splitting rules
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, # Maximum number of characters per chunk
        chunk_overlap=150, # Number of characters shared between adjacent chunks
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    # Split the text
    chunks = splitter.split_text(text)

    return chunks