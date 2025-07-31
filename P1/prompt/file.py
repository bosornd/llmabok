from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{country}의 수도는?")
prompt.save("capital.json")
prompt.save("capital.yaml")

from langchain_core.prompts import load_prompt
prompt = load_prompt("capital.json")
print(prompt)  # input_variables=['country'] template='{country}의 수도는?' ...
