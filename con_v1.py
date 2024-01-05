#!/usr/bin/python

# Test API connect with Google Gemini

import os
import google.generativeai as genai 

GOOGLE_API = os.environ.get('GOOGLE_AI')

genai.configure(api_key=GOOGLE_API)

# List the available Generative Models with your account
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)

consulta = """Crear artículo original de un máximo de 10 párrafos tomando como base la URL compartida. 
Tu respuesta tiene que estar en español, debe contener 2 imágenes y el SEO debe estar optimizado con al menos 
5 enlaces externos para poder maximizar las visitas de búsqueda. 
Al final debes agregar la fuente del artículo: https://towardsdatascience.com/preparing-for-climate-change-with-an-ai-assistant-cdceb5ce4426
"""

mod_gem_pro = genai.GenerativeModel('gemini-pro')
response = mod_gem_pro.generate_content(consulta)

# Check if it was blocked due to saftey concerns
#print(response.prompt_feedback)

print(type(response.parts))
print(type(response.parts))
print(type(response))
# print(response.text)
print(type(response))
print(type(response.text))
# print(response.candidates)
# print(type(response.candidates))
# articulo = response.candidates

# Trying to find text
# titulo = articulo[articulo.find("Título")+1:articulo.find(" ")]

# print(titulo)

# with open("respuesta6.txt", 'w') as file:
#     file.write(response.parts)