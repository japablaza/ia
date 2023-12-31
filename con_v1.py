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
response = mod_gem_pro.generate_content("who is the most advance civilization?")

# Check if it was blocked due to saftey concerns
#print(response.prompt_feedback)

print(response.text)
