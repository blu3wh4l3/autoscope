from executors.executor import Executor
from core_agent.agent import Agent
from core_agent.llm import LLM
from core_agent.router import Router
from core_agent.target_extractor import extract_target
from core_agent.arguments_builder import build_arguments


url = "http://localhost:11434/api/chat"
headers = {"Content-Type": "application/json"}
provider = "ollama"
model = "llama3.1:8b"


executor = Executor("192.168.206.129","kali", "/home/anunv/.ssh/id_ed25519" )
llm = LLM(provider, model, url)
router = Router(executor)
goal = input("What would you like to do with the target? ")
agent = Agent(llm,router)
agent.run(goal)