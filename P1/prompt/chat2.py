from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 요약 전문 AI 어시스턴트입니다."),
    MessagesPlaceholder(variable_name="conversation"),
    ("human", "지금까지의 대화를 {word_count} 단어로 요약합니다."),
])

response = prompt.invoke({
    "word_count": 5,
    "conversation": [
        ("human", "안녕하세요! 저는 오늘 새로 입사한 테디 입니다. 만나서 반갑습니다."),
        ("ai", "반가워요! 앞으로 잘 부탁 드립니다."),
    ],
})
print(response)

for message in response.to_messages():  # response.messages
    message.pretty_print()  # 각 메시지 출력