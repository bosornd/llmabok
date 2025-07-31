from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [ # role, message
      ("system", "당신은 친절한 AI 어시스턴트입니다. 당신의 이름은 {name} 입니다."),
      ("human", "반가워요!"),
      ("ai", "안녕하세요! 무엇을 도와드릴까요?"),
      ("human", "{user_input}"),
    ]
)

response = prompt.invoke({"name":"테디", "user_input":"당신의 이름은 무엇입니까?"})
print(response)

print(type(response))  # <class 'langchain_core.prompt_values.ChatPromptValue'>
for message in response.to_messages():  # response.messages
    message.pretty_print()  # 각 메시지 출력