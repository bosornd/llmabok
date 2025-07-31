from dotenv import load_dotenv
load_dotenv()

import os

# pip install langchain-huggingface hf_xet transformers torch
from huggingface_hub import login
login(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

from langchain_huggingface import HuggingFacePipeline
llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-1b-it",
    task="text-generation",
)

response = llm.invoke("한국의 수도는?")
print(response)