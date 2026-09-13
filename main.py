from ingestion import ingestionpipeline
from embedding import EmbeddingService
from vector_store import VectorStore
from context_builder import contextbuilder
from llm import LLM
from pathlib import Path

class ragassistant:
    def __init__(self):
        self.ingestion=ingestionpipeline()
        self.embedding_service=EmbeddingService()
        self.vector_store=VectorStore()
        self.context_builder = contextbuilder()
        self.llm=LLM()

    def ingest_document(self,file_path:str):
        self.ingestion.ingest(file_path)
    def ask(self,query:str,top_k: int=5):
        query_embedding=self.embedding_service.embed([query])[0]

        results=self.vector_store.search(query_embedding,top_k)
        context=self.context_builder.build(results)
        answers=self.llm.generate(query,context)
        return answers

if __name__ =="__main__":
    app=ragassistant()
    data_folder=Path("data")
    for file_path in data_folder.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in [".pdf", ".docx", ".txt"]:
            app.ingestion.ingest(str(file_path))
    question=input("Ask a question")
    answer=app.ask(question)
    print("\nAnswer")
    print(answer)