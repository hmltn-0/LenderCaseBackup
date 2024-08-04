import requests

API_TOKEN = 'YOUR_API_TOKEN_HERE'
API_URL = 'https://api.languagemodel.com/extract'
PDF_PATH = 'path/to/your/pdf.pdf'

with open(PDF_PATH, 'rb') as f:
    files = {'file': f}
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    response = requests.post(API_URL, headers=headers, files=files)

if response.status_code == 200:
    print(response.json()['extracted_text'])
else:
    print('Failed to extract text', response.status_code, response.text)
