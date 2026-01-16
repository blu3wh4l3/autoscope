from core_agent.prompt import load_prompt, render_prompt
from core_agent.target_extractor import extract_target
from core_agent.arguments_builder import build_arguments
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
        # Prepare - Extract target from goal and build arguments and check for missing arguments
        target = extract_target(user_goal)
        args = build_arguments(action, target)

        # Execute the skill using router
        console.status("[bold green] Running subfinder...")

        try:
            with console.status("[bold green] Running subfinder..."):
                self.router.execute(args)

        except Exception as e:
            console.print(f"[bold red][✗] Subfinder failed: {e}[/bold red]") #need to make this error message dynamic based on the action which is chosen
            return

        console.print("[bold green][✓] subfinder execution completed successfully")
        console.print(
            f"[bold green][✓] Output saved[/bold green] → "
            f"[bold cyan]outputs/{{target}}[/bold cyan]"
        )


        # Interpret - Choose the correct normalizer based on the tool and normalize the tool output

        # Persist - Write normalized output to JSON and update ReconState, mark action completion and save state.