import json
from core_agent.prompt import load_prompt, render_prompt
from core_agent.target_extractor import extract_target
from core_agent.action_param_builder import build_action_params
from core_agent.actions import ACTIONS
from rich.console import Console


console = Console()
class Planner:

    def __init__(self, llm):
        self.llm = llm

    def plan_next_action(self, user_goal):
        action_prompt_template =  load_prompt("action_planning_prompt.txt")
        action_prompt = render_prompt(action_prompt_template, goal = user_goal )
        llm_response = self.llm.generate(action_prompt)
        action = json.loads(llm_response)
        print(f"Action returned by the LLM: {action}")
        target = extract_target(user_goal)

        try:
            action_params = build_action_params(action, target)
            action_name = action["action"]
            action_label = ACTIONS.get(action_name, {}).get("label",action_name)
            return action_params, action_label
        
        except Exception as e:
            console.print(f"[bold red][✗] Action params building failed: {e}[/bold red]")
            return