class contextbuilder:
    def build(self,results)->str:
        documents=results["documents"][0]
        context="\n\n".join(documents)
        return context
