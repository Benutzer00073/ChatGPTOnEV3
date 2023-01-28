import os

import openai

openai.api_key = open(os.getcwd() + '/api_key.txt', 'r').readline().rstrip()


def chat(prompt):
    completions = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=4096, temperature=0)
    print(completions["choices"][0]["text"])


question = input("> ")
print(question)
chat(question)
