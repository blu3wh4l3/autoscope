import requests
class LLM:

    def __init__(self,provider,model,url=None,system_prompt=None):
        self.provider = provider
        self.model = model
        self.url = url
        self.system_prompt = system_prompt
    
    def generate(self, userprompt:str) -> str:
        data = {
            "model": self.model,
            "prompt": self.prompt,
            "stream": False
        }
        response = requests.post(self.url, json=self.data)
        json_response = response.json()
        return json_response["response"]
