import prompt_template
import decorator
import primer
import pyperclip

# Modify question to be asked 
question = "How does recursion work?"

# Provide an example of question and answer to guide response
example = ""

# Change template, primer and decorator to be used
# Multiple primer and decorators can be used
prompt = prompt_template.template.format(
    priming=primer.explainer, 
    question=question,
    example=example, 
    decorator="")

# Run the script to get the prompt
print(prompt)

# Copy the prompt to clipboard
pyperclip.copy(prompt)