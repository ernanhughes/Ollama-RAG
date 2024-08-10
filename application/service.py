import os
from ollama import chat


def response(model: str, user_msg: str):
    messages = [
        {
            'role': 'user',
            'content': f'{user_msg}',
        },
    ]
    response = chat(model, messages=messages)
    content = response['message']['content']
    print(f'Response: {content}')
    return content
