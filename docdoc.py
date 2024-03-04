import requests
import json

url = 'https://api.openai.com/v1/chat/completions'

headers = {"Content-Type": "application/json" , "Authorization" : "Bearer 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", }
data = { "model": "gpt-3.5-turbo","messages": 
          [ 
             { "role": "system","content": "You are a helpful assistant." 
              }, 
             
             {  "role": "user", "content": "Can you make a Speech using Only ABCDEFGHIJK" 
              }

             ]

             }


billy = requests.post(url, headers=headers, data = json.dumps(data))

message = billy.json()["choices"][0]["message"] ["content"]

print(message)