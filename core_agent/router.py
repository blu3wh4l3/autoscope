from skills.subdomain_enum import subfinder
class Router:
    def __init__(self,executor):
        self.executor = executor
        self.tools = {
            "run_subfinder" : subfinder.run
        }
    
    def execute(self,args):
        tool_fn = self.tools[args["action"]]
        tool_fn(args["args"]["domain"], self.executor)

