import convertapi
from text_to_speech import speak


API_Secret = 'sdfhsfhhhhhhhhdK'
API_Key = '499999992'

convertapi.api_secret = API_Secret

result = convertapi.convert('txt', { 'File': 'Document1.pdf' })

result.file.save('file.txt')

with open('file.txt') as f:
    contents = f.read()

speak(contents, "en", save=True, file="output.mp3", speak=True)