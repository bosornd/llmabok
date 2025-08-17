import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [ # (role, message)
        ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 {name} 입니다."),
        ("human", "반가워요!"),
        ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
        ("human", "{user_input}"),
    ]
)
print(prompt)

response = prompt.invoke({ "name":"테디", "user_input":"당신의 이름은 무엇입니까?" })
print(response)
