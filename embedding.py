from sentence_transformers import SentenceTransformer
import numpy as np

class EmbeddingService:
    def __init__(self):
        self.model=SentenceTransformer(
            "sentence-transfromers/all-MiniLM-L6-v2"
        )
    def embed(self,text:str)->np.ndarry:
        return self.model.encode(
            text,
            normalize_embedding=True
        )