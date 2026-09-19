from langchain_core.prompts import ChatPromptTemplate

""" create the prompt that combines the question with the context
{context} reserves the space for the actual context
{question} reserves space for the actual question """

def create_rag_prompt():
    prompt = ChatPromptTemplate.from_template(
        """
        Responde la pregunta utilizando únicamente la información proporcionada en el contexto.
        Si la respuesta no se encuentra en el contexto, indica que no hay información suficiente para responder.
        Contexto:
        {context} 

        Pregunta:
        {question}
        """
    )

    return prompt