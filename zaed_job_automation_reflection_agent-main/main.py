from langchain_core.messages import HumanMessage
from langgraph_reflection import create_reflection_graph
from generator import build_generator
from critic import build_critic


def main():
    generator = build_generator()
    critic = build_critic()

    # Wire them together into a reflection loop
    reflection_graph = create_reflection_graph(
        assistant_graph=generator,
        critique_graph=critic,
    )

    topic = "How should applicant respond to each question during the interview for the Retail Sales - Accessories position at Sephora in Schaumburg, IL?"

    result = reflection_graph.invoke(
        {"messages": [HumanMessage(content=f"Write a 3-paragraph essay on: {topic}")]},
        config={"recursion_limit": 10},
    )

    # The final AI response is the last AIMessage in the message list
    final_essay = next(
        msg.content
        for msg in reversed(result["messages"])
        if isinstance(msg, __import__("langchain_core.messages", fromlist=["AIMessage"]).AIMessage)
    )

    print("=== Final Essay ===")
    print(final_essay)


if __name__ == "__main__":
    main()