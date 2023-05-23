import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


messages = [{"role": "system", "content": "Hello, how are you?"}]

while True:
    message = input("You:\n")
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        
    reply = chat.choices[0].message.content
    print(f"ChatGPT: \n{reply}")
    messages.append({"role":"assistant", "content":reply})