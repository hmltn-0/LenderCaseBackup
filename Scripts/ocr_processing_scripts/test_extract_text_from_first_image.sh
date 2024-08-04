#!/bin/bash

# Define the absolute path to the images
IMG_DIR="/Users/juliushamilton/Lender_Contract_Reversal_Case/Contracts/output_images/convert_pdf_to_images_absolute_output"
FIRST_IMG=$(ls "$IMG_DIR" | head -n 1)
IMG_PATH="$IMG_DIR/$FIRST_IMG"

# Extract text from the first image using the OpenAI CLI
# response=$(openai api chat.completions.create -m gpt-4o-mini -p "Extract the text from the following image: $IMG_PATH" --max-tokens 100)

response=$(openai api chat.completions.create -g system 'Extract the text from the following image:' -g user "$IMG_PATH" -m gpt-4o-mini --max-tokens 100)

# Debug: Print the raw response
echo "$response"



# Extract and display the generated text
text=$(echo "$response" | jq -r ".choices[0].text")
echo "Extracted Text from $FIRST_IMG:"
echo "$text"
