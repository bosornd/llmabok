from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from ragas.embeddings import LangchainEmbeddingsWrapper
embeddings_wrapper = LangchainEmbeddingsWrapper(embeddings)

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from ragas.llms import LangchainLLMWrapper
llm_wrapper = LangchainLLMWrapper(llm)

import ast
with open("AI 에이전트 동향_LLM_Splitted.txt", "r", encoding="utf-8") as f:
    file = f.read()
    texts = ast.literal_eval(file)

from langchain_core.documents import Document
docs = [Document(page_content=text) for text in texts]

# pip install ragas rapidfuzz
from ragas.testset import TestsetGenerator
generator = TestsetGenerator(llm=llm_wrapper, embedding_model=embeddings_wrapper)

dataset = generator.generate_with_langchain_docs(docs, testset_size=10)
df = dataset.to_pandas()
df.to_csv('dataset.csv', index=False)

# 프로그램이 종료되면서 grpc 오류가 발생하는 경우가 있음. (무시)
"""
Traceback (most recent call last):
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 110, in grpc._cython.cygrpc.shutdown_grpc_aio
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 114, in grpc._cython.cygrpc.shutdown_grpc_aio
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 78, in grpc._cython.cygrpc._actual_aio_shutdown
AttributeError: 'NoneType' object has no attribute 'POLLER'
Exception ignored in: 'grpc._cython.cygrpc.AioChannel.__dealloc__'
Traceback (most recent call last):
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 110, in grpc._cython.cygrpc.shutdown_grpc_aio
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 114, in grpc._cython.cygrpc.shutdown_grpc_aio
  File "src/python/grpcio/grpc/_cython/_cygrpc/aio/grpc_aio.pyx.pxi", line 78, in grpc._cython.cygrpc._actual_aio_shutdown
AttributeError: 'NoneType' object has no attribute 'POLLER'
"""