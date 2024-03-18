import openai
import os


def run_request(question):
    openai.organization = ''
    openai.api_key = ''
    format = {'role' : 'user', 'content' : 'Do not mention that you are an AI model. Create a short response. ' + question}
    answer = openai.ChatCompletion.create(model = 'gpt-3.5-turbo', messages = [format])
    return answer['choices'][0]['message']['content']

with open('') as f:
    openai.api_key = f.read().split()




