# File: /Python/api_gemini.py

# Install the Required Library:
# pip install -U google-generativeai

# Import the google.generativeai Library
import google.generativeai as genai

# Generate your API:
# https://aistudio.google.com/app/apikey

# Configure the API Key:
API_KEY = 'AIzaSyAVMXBtSPA_HagSAU1XZR67wmEwbH1biMI'
genai.configure(api_key=API_KEY)

# List Available Models:
for i1 in genai.list_models():
    if 'generateCotent' in i1.supported_generation_methods:
        print(i1.name)

# Create a Content Generation Model:
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Display Welcome Message to the User:
welcome = '### Welcome to the eCop Assistant with Gemine AI ###'
print(len(welcome) * '#')
print(welcome)
print(len(welcome) * '#')
print('### Enter "exit" to exit ###')
print('')

# User Interaction Loop:
while True:
    text = input('Write your message: ')
    if text == 'exit':
        break

    response = chat.send_message(text)
    print('Gemini:', response.text, '\n')

# End of Chat Message:
print('Chat ended.')
