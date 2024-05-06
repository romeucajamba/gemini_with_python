import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


genai.configure(api_key='AIzaSyB242jTrDOMEnxD9EPxHhkmk0tHnX_dC_0')

for m in genai.list_models():
     if 'generateContent' in m.supported_generation_methods:
       print(m.name)


model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])

wellCome = "Bem-vindo a TechEduc"

print(wellCome)

print(len(wellCome) * "#")

print('Digit **sair** Para encerrar a conversa')
print('')


while True:
    questions = str(input('Digite assunto: '))

    if questions == 'sair':
        break

    response = chat.send_message(questions)
    print("Assistente:", response.text)

print("Encerrando o chat!!")

response = model.generate_content(questions, stream=True)

