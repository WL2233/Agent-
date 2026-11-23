from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

# 自动读取环境变量中的 Key 和 API 地址
model = ChatOpenAI(
    model="gpt-6-luna",
    use_responses_api=False,
)
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant,return tools result",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)
