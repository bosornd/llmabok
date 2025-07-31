from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

print(tool.name)
print(tool.description)
print(tool.args)

print(tool.invoke({"query": "한국의 대통령은?"}))
