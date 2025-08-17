import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 나의 친구입니다. 편안하게 대화해 주세요."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}")
])

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chain = prompt | llm
