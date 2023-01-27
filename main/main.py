import openai
import tkinter as tk


root = tk.Tk()

API_KEY = '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'


def chat(prompt):
    completions = openai.Completion.create(model="text-davinci-003", prompt=prompt, api_key=API_KEY, max_tokens=4000)
    print(str(completions.choices[0].text))



question = input("whats up")
print(question)
chat(question)
question = " "



