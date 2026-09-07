from ingestion import ingestionpipeline
from embedding import EmbeddingService
from vector_store import VectorStore
from context_builder import ContextBuilder
from llm import LLM

class ragassistant:
    def __init__(self):
        self.ingestion=ingestionpipeline()
        self.embedding_service=EmbeddingService()
        self.vector_store=VectorStore()
        self.context_builder = ContextBuilder()
        self.llm=LLm()

    def ingest_document(self,file_path:str):
        self.ingestion.ingest(file_path)
    def ask(self,query:str,top_k: int=5):
        query_embedding=self.embedding_service.embed([query])[0]

        results=self.vector_store.search(query_embedding,top_k)
        context=self.context_builder(results)
        answer=self.llm.generate(question,context)
        return answers

if __name__ =="__main__":
    app=ragassistant()
    app.ingest_document("data/document.pdf")
    question=input("Ask a question")
    answer=app.ask(question)
    print("\nAnswer")
    print(answer)