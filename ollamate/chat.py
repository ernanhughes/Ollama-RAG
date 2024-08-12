from ollamate import chat

def response(user_msg: str, model: str = "llama3.1"):
    messages = [
        {
            "role": "user",
            "content": f'{user_msg}',
        },
    ]
    print(f"Model: {model}\nUser Message: {user_msg}")
    response = chat(model, messages=messages)
    content = response["message"]["content"]
    print(f"Response: {content}")
    return content


