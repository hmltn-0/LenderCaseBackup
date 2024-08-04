#!/bin/bash

# Define the absolute path to the images
IMG_PATH="/Users/juliushamilton/Lender_Contract_Reversal_Case/Contracts/output_images/convert_pdf_to_images_absolute_output"

# Verify the OpenAI CLI is installed and configured
if ! command -v openai &> /dev/null
then
    echo "Error: openai CLI is not installed. Install it from https://github.com/openai/openai-python."
    exit 1
fi

# Extract text from image using the OpenAI CLI
response=$(openai api completions.create -m gpt-40-mini -p "Extract the text from the following image: $IMG_PATH" --max-tokens 100)

# Extract and display the generated text
text=$(echo "$response" | jq -r '.choices[0].text')
echo "Extracted Text:"
echo "$text"
