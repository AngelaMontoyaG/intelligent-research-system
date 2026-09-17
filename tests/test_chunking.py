import json
from pathlib import Path

from app.chunking import split_text_into_chunks

"""Read a Markdown file, split it into chunks, and save them as JSON."""

def main():
    # Define file paths for input and output
    input_path = Path("data/processed/cleaned_document.md")
    output_path = Path("data/processed/chunks.json")

    # Read the cleaned text content
    text = input_path.read_text(encoding="utf-8")

    # Split the text into smaller chunks
    chunks = split_text_into_chunks(text)

    # Format each chunk with an ID
    chunks_data = []

    for index, chunk in enumerate(chunks):
        chunks_data.append(
            {
                "chunk_id": index,
                "text": chunk,
            }
        )

    # Save the structured chunks to a JSON file
    output_path.write_text(
        json.dumps(chunks_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Cantidad de chunks:", len(chunks))
    print(f"Chunks guardados en: {output_path}")


if __name__ == "__main__":
    main()