from core_agent.actions import ACTIONS
class Router:
    def __init__(self,executor):
        self.executor = executor
        # self.tools = {
        #     "run_subfinder" : subfinder.run,
        #     "run_nmap" : nmap.run
        # }
    
    def execute(self,args):
        # tool_fn = self.tools[args["action"]]
        # tool_fn(args["args"][args["target_type"]], self.executor)
        tool_fn = ACTIONS.get(args["action"],{}).get("action", args["action"])
        raw_output = tool_fn(args["args"][args["target_type"]], self.executor)
        return raw_output

