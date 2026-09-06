import chromadb

class VectorStore:
    def __init__(self):
        self.client=chromadb.PersistentClient(
            path="data/vector_store"
        )
        self.collection=self.client.get_or_create_collection(
            name="documents"
        )
    def add(self,chunks:list[str],embedding):
        for index,(chunk,embedding)in enumerate(
            zip(chunks,embedding)
        ):
            self.collection.add(
                ids=[str(index)],
                documents=[chunk],
                embeddings=[embedding.tolist()]
            )
    def search(self,query_embedding,top_k:int=5):
        return self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_rresult=top_k
        )