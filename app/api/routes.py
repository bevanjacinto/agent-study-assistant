from fastapi import APIRouter
from app.graph.builder import build_graph

router = APIRouter()
graph = build_graph()

@router.post("/ask")
def ask(question: str):
    result = graph.invoke({"question": question})
    return {
        "decision": result["decision"],
        "answer": result["answer"]
    }