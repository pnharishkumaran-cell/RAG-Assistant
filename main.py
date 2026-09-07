from ingestion import ingestionpipeline
from embedding import EmbeddingService
from vector_store import VectorStore

class ragassistant:
    def __init__(self):
        self.ingestion=ingestionpipeline()
        self.embedding_service=EmbeddingService()
        self.vector_store=VectorStore()

    def ingest_document(self,file_path:str):
        self.ingestion.ingest(file_path)
    def retrievel(self,query:str,top_k: int=5):
        query_embedding=self.embedding_service.embed([query])[0]

        results=self.vector_store.search(query_embedding,top_k)
        return results

if __name__ =="__main__":
    app=ragassistant()
    app.ingest_document("data/document.pdf")