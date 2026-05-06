from app.rag.vectorstore import vectorstore

def retrieve(state):
    results = vectorstore.similarity_search(state["question"], k=2)
    
    context = "\n".join([doc.page_content for doc in results])

    return {"context": context}