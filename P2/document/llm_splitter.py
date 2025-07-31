from dotenv import load_dotenv
load_dotenv()

with open("AI 에이전트 동향-1.txt", "r", encoding="utf-8") as f:
    file = f.read()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
입력 문서에서 검색에 필요한 정보를 찾아서 나열해줘.
1. 복잡한 문장은 간단한 문장으로 바꿔줘. 가능한 원본 문장은 유지하고.
2. 지시 대명사는 사용하지 말고, 구체적인 명사로 바꿔줘.
3. 문서에 있는 내용만 사용해줘. 다른 정보는 사용하지 말고.
4. 결과는 문자열의 배열로 출력해줘.
---
예시 입력:
[AI브리프 스페셜] AI 에이전트 동향2024년 12월호
SPRi AI Brief Special |  2024-12월호
1
AI 에이전트 동향– 빅테크 기업의 AI 에이전트 사례를 중심으로  최근 생성형 AI의 확산과 함께 인간과 상호작용이 가능한 AI 에이전트에 대한 관심이 급증하고 있으며, 향후 몇 년 안에 관련 시장이 급속히 성장할 것으로 예상된다. 빅테크 기업들이 AI 에이전트 시장에 잇따라 진출하며 다양한 수익 모델을 창출하고 있는 상황이다. 그러나 AI 에이전트는 기술적, 사회적, 윤리적, 법적 문제를 초래할 가능성도 내포하고 있다. 앞으로 AI 에이전트는 기술 혁신과 사회 변화를 주도하는 핵심 요소로 자리 잡으며, 기업의 업무방식과 개인의 삶에 깊숙이 통합되어 획기적인 변화를 이끌어갈 것으로 전망된다.1. AI 에이전트(AI Agent)의 도입 및 부상 1) AI 에이전트의 정의 £AI 에이전트에 대한 합의된 학술적 정의는 부재하나, 관련 연구에서는 AI 에이전트를 단순한 AI 모델이나 알고리즘과 구별하여  설명하며, 특히 상호작용과 독립적인 의사결정 능력을 강조 ∙스튜어트 러셀(Stuart Russell)과 피터 노비그(Peter Norvig)는 2021년 출판한 저서 ‘인공지능 – 현대적 접근법’에서 에이전트(Agent)는 센서를 통해 환경을 인식하고 센서가 액추에이터를 통해 해당 환경에 작용하는 것으로, 합리적 에이전트(Rational Agent)는 최선의 결과를 달성하기 위해 행동하거나, 불확실성이 있는 경우 최선의 기대 결과를 얻기 위해 행동하는 행위자로 정의1) ∙알란 찬(ALan Chan) 등은 2024년 발간된 연구논문인 ‘AI 에이전트에 대한 가시성’2)에서 많은 AI 개발자들이 더 큰 자율성, 외부 도구나 서비스 접근, 장기적 목표 달성을 위해 안정적으로 적응하고 계획하며 지속적 행동할 수 있는 능력 향상을 갖춘 시스템을 제작하고 있다고 설명하면서 이러한 시스템에 대해 AI 에이전트(AI agents 또는 agentic systems)라고 지칭
1) Russell, S. J., & Norvig, P.  Artificial Intelligence: A Modern Approach (4th ed.). Pearson. 20212) Alan Chan 외, Visibility into AI Agents, 2024
출력:
빅테크 기업의 AI 에이전트 사례를 중심으로  최근 생성형 AI의 확산과 함께 인간과 상호작용이 가능한 AI 에이전트에 대한 관심이 급증하고 있으며, 향후 몇 년 안에 관련 시장이 급속히 성장할 것으로 예상된다.
빅테크 기업들이 AI 에이전트 시장에 잇따라 진출하며 다양한 수익 모델을 창출하고 있는 상황이다.
그러나 AI 에이전트는 기술적, 사회적, 윤리적, 법적 문제를 초래할 가능성도 내포하고 있다.
앞으로 AI 에이전트는 기술 혁신과 사회 변화를 주도하는 핵심 요소로 자리 잡으며, 기업의 업무방식과 개인의 삶에 깊숙이 통합되어 획기적인 변화를 이끌어갈 것으로 전망된다.
에이전트에 대한 합의된 학술적 정의는 부재하나, 관련 연구에서는 AI 에이전트를 단순한 AI 모델이나 알고리즘과 구별하여 설명하며, 특히 상호작용과 독립적인 의사결정 능력을 강조한다.
스튜어트 러셀(Stuart Russell)과 피터 노비그(Peter Norvig)는 2021년 출판한 저서 ‘인공지능 – 현대적 접근법’에서 에이전트(Agent)는 센서를 통해 환경을 인식하고 센서가 액추에이터를 통해 해당 환경에 작용하는 것으로, 합리적 에이전트(Rational Agent)는 최선의 결과를 달성하기 위해 행동하거나, 불확실성이 있는 경우 최선의 기대 결과를 얻기 위해 행동하는 행위자로 정의하고 있다.
알란 찬(ALan Chan) 등은 2024년 발간된 연구논문인 ‘AI 에이전트에 대한 가시성’에서 많은 AI 개발자들이 더 큰 자율성, 외부 도구나 서비스 접근, 장기적 목표 달성을 위해 안정적으로 적응하고 계획하며 지속적 행동할 수 있는 능력 향상을 갖춘 시스템을 제작하고 있다고 설명하면서 이러한 시스템에 대해 AI 에이전트(AI agents 또는 agentic systems)라고 지칭하고 있다.
---
입력 문서: {input}
""")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt | llm
response = chain.invoke(file)
print(response)

with open("AI 에이전트 동향_LLM_Splitted.txt", "w", encoding="utf-8") as f:
    f.write(response.content)