import dotenv
dotenv.load_dotenv()

from datetime import datetime
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Literal

from langchain import hub

from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder, load_prompt
from langchain_core.output_parsers import PydanticOutputParser, JsonOutputParser, StrOutputParser
from langchain.output_parsers import DatetimeOutputParser, EnumOutputParser

from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader, CSVLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_experimental.text_splitter import SemanticChunker

from langchain_core.retrievers import BaseRetriever
from langchain.retrievers import ContextualCompressionRetriever
from langchain_community.retrievers import WikipediaRetriever
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo

from ragas.testset import TestsetGenerator
from langsmith.evaluation import LangChainStringEvaluator, evaluate
from langsmith.schemas import Run, Example

from langchain_core.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.tools import PythonREPLTool

from langchain_mcp_adapters.client import MultiServerMCPClient
from mcp.server.fastmcp import FastMCP

from langchain.agents import create_tool_calling_agent, AgentExecutor

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.types import Command, Send, interrupt
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langgraph_supervisor import create_supervisor

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

from langchain_google_genai import ChatGoogleGenerativeAI
gemini = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_community.cross_encoders import HuggingFaceCrossEncoder
cross_encoder = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-v2-m3")

from sklearn.metrics.pairwise import cosine_similarity

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)

from langchain_chroma import Chroma

from google import genai

