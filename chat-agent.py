import requests
import json
url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.1:8b",   # use your local ollama model name
    "messages": [
        {
            "role": "user",
            "content":"""
                    Find publicly available subdomains of example.com.

                    STRICT OUTPUT RULES:
                    - Only print subdomain names.
                    - One per line.
                    - No JSON.
                    - No lists.
                    - No bullets.
                    - No explanations.
                    - No additional text.
                    - No code blocks.


            """
        }

    ],
    "stream": False      # ensures full response is returned at once
}

response = requests.post(url, json=payload)

# The response contains a 'response' field with the model output
res_json = response.json()
# print(res_json.get("response", ""))
# print(json.dumps(res_json, indent=4))
print(res_json["message"]["content"])
