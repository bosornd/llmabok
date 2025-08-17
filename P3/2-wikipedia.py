from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

response = tool.invoke("한국의 대통령은?")      # {"query": "한국의 대통령은?"}
print(response)
