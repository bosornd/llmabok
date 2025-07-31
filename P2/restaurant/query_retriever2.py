from dotenv import load_dotenv
load_dotenv()

from langchain.chains.query_constructor.base import AttributeInfo
metadata_field_info = [
    AttributeInfo(
        name="ID",
        description="the identifier of the restaurant",
        type="string",
    ),
    AttributeInfo(
        name="Taste",
        description="the taste of the food provided by the restaurant. Rated between 1 to 100",
        type="integer",
    ),
    AttributeInfo(
        name="Ambiance",
        description="the atmosphere provided by the restaurant. Rated between 1 to 100",
        type="integer",
    ),
    AttributeInfo(
        name="Service",
        description="the service provided by the restaurant. Rated between 1 to 100",
        type="integer",
    ),
    AttributeInfo(
        name="Worth_the_price",
        description="refers to if the price of the food is worth it. (yes or no)",
        type="string",
    ),
    AttributeInfo(
        name="Menu_variety",
        description="tells if the menu has a variety of options or not. Rated between 1 to 100",
        type="integer",
    ),
    AttributeInfo(
        name="Hygienic",
        description="review on the hygiene measure taken by the restaurant. Rated between 1 to 100",
        type="integer",
    ),
    AttributeInfo(
        name="Vegan_options",
        description="refers to if the restaurant offers vegan options. (yes or no)",
        type="string",
    ),
    AttributeInfo(
        name="Smoking_area",
        description="refers to if the restaurant has a smoking area or not. (yes or no)",
        type="string",
    ),
    AttributeInfo(
        name="Parking",
        description="refers to if the restaurant has parking or not. (yes or no)",
        type="string",
    ),
    AttributeInfo(
        name="Pet_friendly",
        description="refers to if the restaurant permits pets or not. (yes or no)",
        type="string",
    ),    
]

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="chroma_db")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain.chains.query_constructor.base import get_query_constructor_prompt
prompt = get_query_constructor_prompt(
    "Restaurant review data",  # 문서 내용 설명
    metadata_field_info,       # 메타데이터 필드 정보
)
# prompt.pretty_print()

from langchain.chains.query_constructor.base import StructuredQueryOutputParser
output_parser = StructuredQueryOutputParser.from_components()

query_constructor = prompt | llm | output_parser

query_output = query_constructor.invoke("주차장이 있고 맛 평가가 80점 이상인 식당은?") 
print(query_output)  # query='식당' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='Parking', value='yes'), Comparison(comparator=<Comparator.GTE: 'gte'>, attribute='Taste', value='80')]) limit=None

from langchain_community.query_constructors.chroma import ChromaTranslator
translator = ChromaTranslator()

filter = translator.visit_operation(query_output.filter)
print(filter)        # {'$and': [{'Parking': {'$eq': 'yes'}}, {'Taste': {'$gte': '80'}}]}

from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_community.query_constructors.chroma import ChromaTranslator
retriever = SelfQueryRetriever(
    query_constructor=query_constructor,
    vectorstore=vector_store,
    structured_query_translator=ChromaTranslator(),  # 쿼리 변환기
)
response = retriever.invoke("주차장이 있고 맛 평가가 80점 이상인 식당은?")
print(response)
for doc in response:
    print(doc.metadata)
