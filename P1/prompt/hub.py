from dotenv import load_dotenv
load_dotenv()

from langchain import hub

prompt = hub.pull("rlm/rag-prompt")
print(prompt)

prompt_owner = "bosornd"
prompt_title = "rag-prompt"
hub.push(f"{prompt_owner}/{prompt_title}", prompt)
