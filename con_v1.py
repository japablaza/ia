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

mod_gem_pro = genai.GenerativeModel('gemini-pro')
response = mod_gem_pro.generate_content("Crear un artículo original de un máximo de 5 párrafos tomando como base el artículo. Tu respuesta tiene que estar en español, debes entregar 2 URL de imágenes reales de alta resolución y adicionalmente debe venir optimizado el SEO del artículo con enlaces externos para poder maximizar las visitas de búsqueda. Al final debes agregar la fuente del artículo: https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=161789&Lab=NHEERL&showcriteria=2&keyword=aliens&timstype=&timssubtypeid=&epanumber=&ombcat=Any&datebeginpublishedpresented=&dateendpublishedpresented=&datebeginupdated=&dateendupdated=&deid=&personname=&personid=&role=Any&journalname=&journalid=&publishername=&publisherid=&sortby=relevance&count=50")

# Check if it was blocked due to saftey concerns
#print(response.prompt_feedback)

print(response.text))
print(response.candidates)

articulo = response.candidates

titulo = articulo[articulo.find("Título")+1:articulo.find(" ")]

print(titulo)