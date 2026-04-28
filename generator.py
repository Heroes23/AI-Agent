from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, END 
from dotenv import load_dotenv

load_dotenv()

GENERATOR_SYSTEM_PROMPT = """You are a helpful assistant. Write clear, well-structured, 
and engaging messages based on 
the provided job description. Your task it to help each 
individual applicant perform above and beyond
on each job interview by providing them with the most relevant information from the job description. 
When given feedback, 
incorporate it into a revised message. Always strive to make the messages more informative 
and helpful for the applicant. 
"""

llm = ChatOpenAI(model="gpt-4o", temperature=0.7)

def generate(state: MessagesState): 
    """Generate a message based on the current state of the job description and feedback."""
    messages = [SystemMessage(content=GENERATOR_SYSTEM_PROMPT)] + state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}

def build_generator(): 
    graph = StateGraph(MessagesState)
    graph.add_node("generate", generate)
    graph.set_entry_point("generate")
    graph.add_edge("generate", END)
    return graph.compile()


generator_llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
