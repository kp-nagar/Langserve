import requests
 
URL = "http://localhost:4002/ask/invoke"
 
payload = {"input" : {
        "item": "computer"}
    }

response = requests.post(URL, json=payload)
output = response.json()["output"]
print(output)