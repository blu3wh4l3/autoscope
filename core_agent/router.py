from skills.subdomain_enum import subfinder
class Router:
    def __init__(self,executor):
        self.executor = executor
        self.tools = {
            "run_subfinder" : subfinder.run
        }
    
    def execute(self, action, args):
        tool_fn = self.tools[action]
        tool_fn(**args, executor=self.executor)

