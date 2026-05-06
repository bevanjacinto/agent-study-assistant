from app.llm.model import llm

def decide(state):
    prompt = f"""
    You are an AI system deciding whether to use retrieval (RAG) or answer directly.

    Question: {state['question']}

    Decision criteria:

    Use "rag" if:
    - The question is technical, domain-specific, or requires detailed explanation
    - External or stored knowledge could improve accuracy
    - The answer could vary based on context or documentation

    Use "answer" if:
    - The question is simple, factual, and widely known
    - The answer is short and does not need additional context

    Think step-by-step before deciding.

    Return ONLY one word: rag OR answer
    """

    decision = llm.invoke(prompt).content.strip().lower()

    # fallback safety
    if decision not in ["answer", "rag"]:
        decision = "answer"

    return {"decision": decision}