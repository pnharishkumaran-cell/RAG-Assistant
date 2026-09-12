from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        self.model=SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    def embed(self,text:list[str])->np.ndarray:
        return self.model.encode(
            text,
            normalize_embedding=True
        )