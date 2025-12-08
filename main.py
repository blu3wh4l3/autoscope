from executors.executor import Executor
from core_agent.agent import Agent
from core_agent.llm import LLM
from core_agent.router import Router


url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
provider = "ollama"
model = "llama3.1:8b"

# data = {
#     "model": "llama3.1:8b",   # use your local ollama model name
#     "prompt": "Find publicly available subdomains of tesla.com and list them in json format",
#     "stream": False      # ensures full response is returned at once
# }

executor = Executor("192.168.206.129","kali", "/home/anunv/.ssh/id_ed25519" )
llm = LLM(provider, model, url)
router = Router(executor)
goal = input("What recon type do you want to perform on the target? ")
agent = Agent(llm,router)
agent.actionPlan(goal)

#Send the user input to agent for action planning


# print(f"Output: {agent.runTask(goal)}")