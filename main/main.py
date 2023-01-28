import openai
import tkinter as tk
import os

root = tk.Tk()

API_KEY = open(os.getcwd() + '/api_key.txt', 'r').readline().rstrip()


def chat(prompt):
    completions = openai.Completion.create(model="text-davinci-003", prompt=prompt, api_key=API_KEY, max_tokens=4000)
    print(str(completions.choices[0].text))


question = input("whats up")
print(question)
chat(question)
question = " "
