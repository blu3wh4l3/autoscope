from core_agent.prompt import load_prompt, render_prompt
from core_agent.target_extractor import extract_target
from core_agent.action_param_builder import build_action_params
from core_agent.actions import ACTIONS
from rich.console import Console

console = Console()
import json
class Agent:
    def __init__(self,llm,router):
        self.llm = llm
        self.router = router
        
    
    def run(self,user_goal):

        # Plan - LLM selects action from goal
        action_prompt_template =  load_prompt("action_planning_prompt.txt")
        action_prompt = render_prompt(action_prompt_template, goal = user_goal )
        llm_response = self.llm.generate(action_prompt)
        action = json.loads(llm_response)
        print(f"Action returned by the LLM: {action}")
        # Prepare - Extract target from goal and build arguments and check for missing arguments
        target = extract_target(user_goal)

        try:
            action_params = build_action_params(action, target)
        
        except Exception as e:
            console.print(f"[bold red][✗] Action params building failed: {e}[/bold red]")
            return
        action_name = action["action"]
        action_label = ACTIONS.get(action_name, {}).get("label",action_name)
        

        # Execute the skill using router

        try:
            with console.status(f"[bold green] Running {action_label}..."):
                output = self.router.execute(action_params)
                if not output:
                    console.print(f"[bold red][✗] {action_label} returned no data.[/bold red]")
                    return

                console.print(f"[bold green][✓] {action_label} completed successfully")
                console.print(
                    f"[bold green][✓] Raw Output saved[/bold green] → "
                    f"[bold cyan]outputs/{{target}}[/bold cyan]"
                )
                console.print(
                    f"[bold green][✓] Normalized Output saved[/bold green] → "
                    f"[bold cyan]outputs/{{target}}/normalized[/bold cyan]"
                )
        except Exception as e:
            console.print(f"[bold red][✗] {action_label} failed: {e}[/bold red]")
            return

        


        # Interpret - Choose the correct normalizer based on the tool and normalize the tool output

        # Persist - Write normalized output to JSON and update ReconState, mark action completion and save state.