import requests
from core_agent.prompt import load_prompt, render_prompt
class LLM:

    def __init__(self,provider,model,url=None,system_prompt=None):
        self.provider = provider
        self.model = model
        self.url = url
        self.system_prompt = load_prompt("system_prompts.txt")
    
    def generate(self, userprompt:str) -> str:
        payload = {
                "model": "llama3.1:8b",   # use your local ollama model name
                "messages": [
                    {
                        "role": "system",
                        "content":self.system_prompt
                    },
                    {
                        "role": "user",
                        "content":userprompt
                    }

                ],
                "stream": False      # ensures full response is returned at once
        }
        response = requests.post(self.url, json=payload)
        json_response = response.json()
        return json_response["message"]["content"]
