#!/bin/bash
openai api completions.create -m text-davinci-003 -p "Say this is a test" --max-tokens 5
