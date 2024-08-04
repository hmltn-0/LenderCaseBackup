#!/bin/bash
openai api chat.completions.create -m gpt-4o-mini -g user "Extract text from this image: <IMAGE_URL>" --max-tokens 100
