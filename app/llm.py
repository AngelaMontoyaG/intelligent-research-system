import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


def create_llm():
    # loads the variables saved in .env
    load_dotenv() 

    # gets the key
    api_key = os.getenv("GROQ_API_KEY")

    # checks that the key exists
    if not api_key:
        raise ValueError("No se encontró la variable GROQ_API_KEY.")

    # creates the object that will communicate with the model
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        api_key=api_key,
    )

    return llm