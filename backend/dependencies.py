from functools import lru_cache

from agent.agent_engine import AgentEngine

@lru_cache
def get_agent():
    return AgentEngine()