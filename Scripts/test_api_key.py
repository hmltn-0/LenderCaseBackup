import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Test the API key
try:
    response = openai.Model.list()
    print('API key is valid. Available models:')
    for model in response['data']:
        print(f"- {model['id']}")
except Exception as e:
    print('Failed to authenticate API key:', e)
