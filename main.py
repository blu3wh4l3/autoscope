from executors.executor import KaliCommandExecutor
from core_agent.agent import Agent
import platform

comamndExecutor = KaliCommandExecutor("192.168.206.129","kali", "/home/anunv/.ssh/id_ed25519" )
agent = Agent(comamndExecutor)
while True:
    goal = input("What recon type do you want to perform on the target? ")
    print(f"Output: {agent.runTask(goal)}")