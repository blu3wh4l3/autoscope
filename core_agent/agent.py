from core_agent.prompt import load_prompt, render_prompt
import json
class Agent:
    def __init__(self,llm,router):
        self.llm = llm
        self.router = router
        
    def actionPlan(self, user_goal):
        action_prompt_template =  load_prompt("action_planning_prompt.txt")
        action_prompt = render_prompt(action_prompt_template, goal = user_goal )
        llm_response = self.llm.generate(action_prompt)
        action = json.loads(llm_response)
        return action