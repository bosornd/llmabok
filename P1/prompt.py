from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{country}의 수도는?")
print(prompt)  # input_variables=['country'] template='{country}의 수도는?' ...

prompt = PromptTemplate(template="{country}의 수도는?", input_variables=["country"])
result = prompt.invoke({"country": "한국"})
print(result)  # text='한국의 수도는?'

result = prompt.invoke("일본")
print(result)  # text='일본의 수도는?'

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm  # RunnableSequence(prompt, llm)

response = chain.invoke("중국")
print(response)
