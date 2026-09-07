import os
from google import genai

class LLM:
    def __init__(self):

        
        self.client=genai.Client(api_key=os.getenv("GEMIN_API_KEY"))
    def generate(self,question:str,context:str)->str:
        prompt=f""""
    Answer the question using only the provided context

    Context:
    {context}

    Question:
    {question}

    if the answer cannot be found in the context, say that the information is not available in the provided document."""

        response = self.client.models.generaate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.txt
