from ingestion import ingestionpipeline

class ragassistant:
    def __init__(self):
        self.ingestion=ingestionpipeline()

    def ingest_document(self,file_path:str):
        self.ingestion.ingest(file_path)

if __name__ =="__main__":
    app=ragassistant()
    app.ingest_document("data/document.pdf")