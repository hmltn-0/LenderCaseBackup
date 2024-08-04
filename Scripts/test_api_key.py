import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Test the API key
try:
    response = openai.Engine.list()
    print('API key is valid. Available engines:')
    for engine in response['data']:
        print(f"- {engine['id']}")
except Exception as e:
    print('Failed to authenticate API key:', e)
