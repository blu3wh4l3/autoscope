import requests

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

data = {
    "model": "llama3.1:8b",   # use your local ollama model name
    "prompt": "Find publicly available subdomains of tesla.com and list them in json format",
    "stream": False      # ensures full response is returned at once
}

response = requests.post(url, headers=headers, json=data)

# The response contains a 'response' field with the model output
res_json = response.json()
print(res_json.get("response", ""))
