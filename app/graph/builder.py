from langgraph.graph import StateGraph
from app.graph.state import AgentState

from app.graph.nodes.decide import decide
from app.graph.nodes.retrieve import retrieve
from app.graph.nodes.answer import answer_direct, answer_rag
from app.graph.nodes.router import route


def build_graph():
    builder = StateGraph(AgentState)

    # nodes
    builder.add_node("decide", decide)
    builder.add_node("retrieve", retrieve)
    builder.add_node("answer_direct", answer_direct)
    builder.add_node("answer_rag", answer_rag)

    # entry
    builder.set_entry_point("decide")

    # branching
    builder.add_conditional_edges(
        "decide",
        route,
        {
            "answer": "answer_direct",
            "rag": "retrieve",
        }
    )

    # rag flow
    builder.add_edge("retrieve", "answer_rag")

    return builder.compile()