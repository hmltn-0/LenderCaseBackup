import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY', 'YOUR_API_KEY_HERE')

# Path to the PDF file
document_path = 'path/to/your/pdf.pdf'

# Function to read PDF and extract text
import PyPDF2

with open(document_path, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(reader.numPages):
        page = reader.getPage(page_num)
        text += page.extract_text() + '
'

# Request LLM API to process the extracted text
response = openai.Completion.create(
    engine='davinci',
    prompt=f'Extract accurate text from the following document: {text}',
    max_tokens=500
)

# Output the result
extracted_text = response.choices[0].text.strip()
print(extracted_text)
