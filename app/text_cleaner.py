import re

def clean_markdown(text: str) -> str:
    # Replace escaped characters
    text = text.replace(r"\-", "-")
    text = text.replace(r"\|", "|")
    text = text.replace(r"\.", ".")

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        line_str = line.strip()

        # Skip empty bullet points or orphan symbols (like - ● o - *)
        # Ignores the line if it only contains hyphens, asterisks, and special symbols like ● but NO letters or numbers
        if re.match(r'^\s*[-*•]\s*[●•▪]*\s*$', line_str):
            continue

        # Fix headings wrapped in bold (**## Title**)
        if line_str.startswith("**##") and line_str.endswith("**"):
            line = line_str[2:-2].strip() #Starts at position 2 and ends 2 positions before

        cleaned_lines.append(line)

    text = "\n".join(cleaned_lines)

    # Join split sentences if the next line starts with lowercase
    text = re.sub(r'\n\s*\n?(?=[a-zà-ÿ])', ' ', text)

    # Ensure spaces before headings (#, ##, ###)
    text = re.sub(r'([^\n])\n(#{1,6}\s)', r'\1\n\n\2', text)

    # Normalize extra multiple spaces (Maximum 2 breaks / 1 blank line)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()