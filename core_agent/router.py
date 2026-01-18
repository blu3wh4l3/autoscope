from core_agent.actions import ACTIONS
class Router:
    def __init__(self,executor):
        self.executor = executor
    
    def execute(self,action_params):
        tool_fn = ACTIONS.get(action_params["action"],{}).get("skill", action_params["action"])
        raw_output = tool_fn(action_params["target"]["value"], self.executor)
        normalizer_fn = ACTIONS.get(action_params["action"],{}).get("normalizer", action_params["action"])
        normalized_output = normalizer_fn(action_params["target"]["value"],raw_output)
        return normalized_output

