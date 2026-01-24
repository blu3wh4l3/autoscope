from executors.executor import Executor
from core_agent.agent import Agent
from core_agent.llm import LLM
from core_agent.router import Router
from core_agent.planner import Planner


url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
provider = "ollama"
model = "llama3.1:8b"


executor = Executor("192.168.206.129","kali", "/home/anunv/.ssh/id_ed25519" )
llm = LLM(provider, model, url)
planner = Planner(llm)
router = Router(executor)
goal = input("What would you like to do with the target? ")
agent = Agent(llm,planner,router)
agent.run(goal)