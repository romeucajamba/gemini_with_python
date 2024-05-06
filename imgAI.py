## Descrição da Imagem

import google.generativeai as genai

import PIL
from IPython.display import display
from IPython.display import Markdown


genai.configure(api_key='AIzaSyB242jTrDOMEnxD9EPxHhkmk0tHnX_dC_0')

for m in genai.list_models():
     if 'generateContent' in m.supported_generation_methods:
       print(m.name)


model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('yhanko.jpeg')

response = model.generate_content(img)

print("Resposta", response)



question = str(input('O que queres que eu faça: '))

response = model.generate_content(question)

response.resolve()