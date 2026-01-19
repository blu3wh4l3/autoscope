import json
from pathlib import Path
from core_agent.actions import ACTIONS
class Router:
    def __init__(self,executor):
        self.executor = executor
    
    def execute(self,action_params):
        tool_fn = ACTIONS.get(action_params["action"],{}).get("skill", action_params["action"])
        raw_output = tool_fn(action_params["target"]["value"], self.executor)
        normalizer_fn = ACTIONS.get(action_params["action"],{}).get("normalizer", action_params["action"])
        normalized_output = normalizer_fn(action_params["target"]["value"],raw_output)
        normalized_str_output = json.dumps(normalized_output, indent=2)

        # Save normalized output in local file system
        project_dir = Path(__file__).resolve().parents[1]
        normalized_output_dir = project_dir / 'outputs' / action_params["target"]["value"] / 'normalized' / 'subdomains.txt'
        normalized_output_dir.parent.mkdir(exist_ok=True, parents=True)
        with open(normalized_output_dir, "w", encoding="utf-8") as f:
            f.write(normalized_str_output)
        return normalized_output

