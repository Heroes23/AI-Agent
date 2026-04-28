import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, MessagesState, END
# use this virtual envn -> reflection_env

load_dotenv()

# ── LLMs ──────────────────────────────────────────────────────────────────────
generator_llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
critic_llm = ChatOpenAI(model="gpt-4o", temperature=0)

# ── Generator ─────────────────────────────────────────────────────────────────
GENERATOR_PROMPT = """You are a helpful assistant. Write clear, well-structured, and engaging messages based on 
the provided job description. Your task is to create a message that can be emailed to recruiters about a specific job 
that will make reruiters look at the email, read it and read the applicants resume, 
and reply back so they can interview the applicant, all based on the relevant information from the job description. 
Criteria: 
- keep it 2 paragraphs. 
- include candidates name and company name. 

When given feedback, incorporate it into a revised message. Always strive to improve clarity, depth, and usefulness. 
"""
#update generator propmt to encase recruiter name and company name. as well as own name and contact information. 
# i should use an example resume that can be used to pull relevant information from the resume to include in the email draft. and i also 
# need to make sure the prompt addresses gaps in resume and creates a message that can make up for
# those gaps and make the applicant look more qualified for the job. 

# Ali's comments: 
# deep research - why is coompany hiring, what's their goal, and how can candidate help them achieve that goal. 
# keep the email short but concise - 2 paragraphs max. 

def replacement(state: MessagesState):
    metadata = state.get("metadata", {})
    recruiter_name = metadata.get("recruiter_name", "[Recruiter's Name]")
    company_name = metadata.get("company_name", "[Company Name]")
    applicant_name = metadata.get("applicant_name", "[Your Name]")
    previous_company = metadata.get("previous_company", "[Previous Company Name]")

    last_msg = state["messages"][-1].content
    last_msg = last_msg.replace("[Recruiter's Name]", recruiter_name)
    last_msg = last_msg.replace("[Previous Company Name]", previous_company)
    last_msg = last_msg.replace("[Your Name]", applicant_name)
    last_msg = last_msg.replace("[Company Name]", company_name)

    updated_messages = state["messages"][:-1] + [HumanMessage(content=last_msg)]
    return {"messages": updated_messages, "metadata": metadata}

def generate(state: MessagesState):
    messages = [SystemMessage(content=GENERATOR_PROMPT)] + state["messages"]
    response = generator_llm.invoke(messages)
    return {"messages": state["messages"] + [response]}

generator_graph = StateGraph(MessagesState)
generator_graph.add_node("generate", generate)
generator_graph.set_entry_point("generate")
generator_graph.add_edge("generate", END)
generator = generator_graph.compile()

# ── Critic ────────────────────────────────────────────────────────────────────
CRITIC_SYSTEM_PROMPT = """You are a strict message editor. Review each message and evaluate it on:
- Clarity and coherence
- Strength of argument
- Use of evidence or examples
- Grammar and style 
- Humanisitc tone 

If the message meets a high standard on all criteria, respond with exactly: APPROVED

If it needs improvement, respond with specific, actionable feedback starting with: FEEDBACK:
"""

def critique(state: MessagesState):
    messages = [SystemMessage(content=CRITIC_SYSTEM_PROMPT)] + state["messages"]
    response = critic_llm.invoke(messages)
    critique_text = response.content.strip()
    return {"messages": state["messages"] + [HumanMessage(content=critique_text)]}

critic_graph = StateGraph(MessagesState)
critic_graph.add_node("critique", critique)
critic_graph.set_entry_point("critique")
critic_graph.add_edge("critique", END)
critic = critic_graph.compile()

# ── Reflection Loop ────────────────────────────────────────────────────────────
def reflection_loop(initial_state, max_iters=5):
    state = initial_state

    for i in range(max_iters):
        # Generate draft
        state = generator.invoke(state)

        # Critique draft
        state = critic.invoke(state)

        last_msg = state["messages"][-1].content
        print(f"Iteration {i+1} critique: {last_msg}\n")

        if "APPROVED" in last_msg:
            print(f"Approved after {i+1} iteration(s)\n")
            break

    return state

# ── Run ────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    topic = "What are the key responsibilities and qualifications for the Retail Sales - Accessories position at Sephora in Schaumburg, IL, and how can an applicant best prepare for the interview?"

    print(f"Topic: {topic}\n")
    print("Running reflection loop...\n")

    result = reflection_loop(
        {"messages": [HumanMessage(content=f"Write a 3-paragraph message on: {topic}")]}
    )

    # Extract final essay (last AIMessage)
    final = next(
        m.content for m in reversed(result["messages"]) if isinstance(m, AIMessage)
    )

    # Count feedback cycles
    cycles = sum(
        1 for m in result["messages"]
        if isinstance(m, HumanMessage) and "FEEDBACK" in m.content
    )

    print(f"Completed in {cycles} reflection cycle(s).\n")
    print("=== Final Message ===\n")
    print(final)


#done 
# draft the right outreach message to the recruiter for any job -> make my email draft to make the recruiter respond. 
# make the agent give you a better draft to increase percentage of recruiter responding back to your email. 
# how recrutiers think -> how would a recruiter evaluate your email -> how to make it better -> how to make it more likely for the recruiter to respond back to applicant.