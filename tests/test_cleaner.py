from pathlib import Path
from app.text_cleaner import clean_markdown

"""Read a Markdown file, clean its content, and save the result."""

def main():
    input_path = Path("data/processed/converted_document.md")
    output_path = Path("data/processed/cleaned_document.md")

    original_text = input_path.read_text(encoding="utf-8")

    cleaned_text = clean_markdown(original_text)

    output_path.write_text(cleaned_text, encoding="utf-8")

    print(f"Archivo limpio guardado en {output_path}")


if __name__ == "__main__":
    main()