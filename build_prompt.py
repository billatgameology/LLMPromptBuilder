import prompt_template
import decorator
import primer

# Modify question to be asked 
question = "What is your name?"

# Change primer and decorator to be used
# Multiple primer and decorators can be used
prompt = prompt_template.template_pqd.format(
    priming=primer.explainer, 
    question=question, 
    decorator= decorator.add_comment + decorator.explore_ways)

# Run the script to get the prompt
print(prompt)