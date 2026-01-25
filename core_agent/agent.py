from rich.console import Console
console = Console()
class Agent:
    def __init__(self,llm,planner,router):
        self.llm = llm
        self.router = router
        self.planner = planner
        
    
    def run(self,user_goal):
        # Plan and prepare - part of action planning component
        # Plan - LLM selects action from goal
        try:
            action_params, action_label = self.planner.plan_next_action(user_goal)
        
        except Exception as e:
            console.print(f"[bold red][✗] {e}[/bold red]")
            return
        

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