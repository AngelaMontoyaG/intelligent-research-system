from pathlib import Path

from pdf_reader import extract_text_from_pdf


def main():
    pdf_path = Path(
        "data/documents/politicas_devoluciones_y_garantias_nova.pdf"
    )

    markdown_text = extract_text_from_pdf(pdf_path)
    output_path = Path("data/processed/converted_document.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    output_path.write_text(markdown_text, encoding="utf-8")

    print(f"Archivo markdown guardado en {output_path}")


if __name__ == "__main__":
    main()