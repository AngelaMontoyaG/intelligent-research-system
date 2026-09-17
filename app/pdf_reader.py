from pathlib import Path

from docling.document_converter import DocumentConverter

"""Extract text from a PDF file and return it as Markdown.
Args:
    pdf_path (Path): The path to the PDF file.
Returns:
    str: The extracted content in Markdown format.
"""
def extract_text_from_pdf(pdf_path: Path) -> str:
    converter = DocumentConverter()

    result = converter.convert(pdf_path)

    return result.document.export_to_markdown()