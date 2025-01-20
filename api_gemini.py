# File: /Python/api_gemini.py

# pip install -U google-generativeai

import google.generativeai as genai

# Generate your API:
# https://aistudio.google.com/app/apikey

API_KEY = 'AIzaSyAVMXBtSPA_HagSAU1XZR67wmEwbH1biMI'
genai.configure(api_key=API_KEY)

for i1 in genai.list_models():
    if 'generateCotent' in i1.supported_generation_methods:
        print(i1.name)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

welcome = '### Welcome to the eCop Assistant with Gemine AI ###'
print(len(welcome) * '#')
print(welcome)
print(len(welcome) * '#')
print('### Enter "exit" to exit ###')
print('')

while True:
    text = input('Write your message: ')
    if text == 'exit':
        break

    response = chat.send_message(text)
    print('Gemini:', response.text, '\n')

print('Chat ended.')
