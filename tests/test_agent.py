from agent.agent_engine import AgentEngine

agent = AgentEngine()

while True:

    question = input("\nYou : ")

    if question.lower() == "exit":
        break

    answer = agent.chat(question)

    print("\nAssistant:\n")

    print(answer)