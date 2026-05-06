from app.llm.model import llm

def answer_direct(state):
    response = llm.invoke(state["question"])
    return {"answer": response.content}


def answer_rag(state):
    prompt = f"""
    You MUST answer ONLY using the provided context.

    Rules:
    - Do NOT add any external knowledge
    - Do NOT give examples unless present in context
    - If the answer is not fully in the context, say:
    "I don't have enough information"

    Context:
    {state['context']}

    Question:
    {state['question']}
    """

    response = llm.invoke(prompt)
    return {"answer": response.content}