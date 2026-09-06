from document_loading import DocumentLoader
from chunker import Textchunker
from embedding import EmbeddingService
from vector_store import VectorStore

class ingestionpipeline:
    def __init__(self):
        self.loader=DocumentLoader
        self.chunker=Textchunker
        self.embedding=EmbeddingService
        self.vectorstore=VectorStore

    def ingest(self,file_path:str):
        text=self.loader.load(file_path)
        chunks=self.chunker.split(text)
        embedding=self.embedding.embed(chunks)
        self.vectorstore.add(chunks,embedding)