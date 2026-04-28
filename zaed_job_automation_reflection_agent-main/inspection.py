def stream_reflection(topic: str):
    from langchain_core.messages import HumanMessage, AIMessage
    from langgraph_reflection import create_reflection_graph
    from generator import build_generator
    from critic import build_critic

    reflection_graph = create_reflection_graph(
        assistant_graph=build_generator(),
        critique_graph=build_critic(),
    )

    inputs = {"messages": [HumanMessage(content=f"Write a 3-paragraph message on: {topic}")]}

    print("=== Reflection Loop ===\n")
    for step, state in enumerate(reflection_graph.stream(inputs, config={"recursion_limit": 10})):
        for node_name, update in state.items():
            if not update.get("messages"):
                print(f"[Step {step}] {node_name}: Critic approved — stopping.\n")
                continue
            for msg in update["messages"]:
                role = "Generator" if isinstance(msg, AIMessage) else "Critic"
                print(f"[Step {step}] {role} ({node_name}):")
                print(msg.content[:300] + ("..." if len(msg.content) > 300 else ""))
                print()

