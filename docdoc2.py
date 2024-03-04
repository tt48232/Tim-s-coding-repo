from openai import OpenAI

import json



client = OpenAI(api_key="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")


message_list= [
    {"role": "system", "content": "You are a helpful assistant."}, 
               {"role": "user", "content": "you are trying spy working for the U.S!"} 
               
               ]

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages= message_list
    
    #[ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "you are trying spy working for the U.S!"} )
)

print(completion.choices[0].message)

f = completion.choices[0].message
message_list += message_list.append([{"role": "system", "content": "You are a helpful assistant."}, 
               {"role": "user", "content": str(f)} )