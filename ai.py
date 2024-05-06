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

questions = str(input('Digite uma questão ou assunto: '))

response = model.generate_content(questions, stream=True)

for chuck in response:
    print(chuck.text)
    ##print("_"*80)