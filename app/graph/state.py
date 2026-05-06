from typing import TypedDict, Optional

class AgentState(TypedDict):
    question: str
    decision: Optional[str]
    context: Optional[str]
    answer: Optional[str]