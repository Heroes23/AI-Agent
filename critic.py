from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, MessagesState, END
from dotenv import load_dotenv

load_dotenv()

CRITIC_SYSTEM_PROMPT = """You are a strict message editor. Review each message and evaluate it on:
- Clarity and coherence
- Strength of argument
- Use of evidence or examples
- Grammar and style 
If the message meets a high standard on all criteria, respond with exactly: APPROVED
If it needs improvement, respond with specific, actionable feedback starting with: FEEDBACK:
"""


llm = ChatOpenAI(model="gpt-4o", temperature=0) 

def critique(state: MessagesState):
    """Critique the latest message draft."""
    messages = [SystemMessage(content=CRITIC_SYSTEM_PROMPT)] + state["messages"]
    response = llm.invoke(messages)

    critique_text = response.content.strip()

    # Signal completion if the message is approved
    if critique_text.upper().startswith("APPROVED"):
        return {"messages": []} 
    
    # Return feedback as a HumanMessage for the generator to use in revisions
    return {"messages": [HumanMessage(content=critique_text)]}

def build_critic():
    graph = StateGraph(MessagesState)
    graph.add_node("critique", critique)
    graph.set_entry_point("critique")
    graph.add_edge("critique", END)
    return graph.compile()


critic_llm = ChatOpenAI(model="gpt-4o", temperature=0)