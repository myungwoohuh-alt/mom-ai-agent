from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()
response = client.responses.create(
model="gpt-5-mini",
input="안녕하세요. 한 문장으로 인사해 주세요."
)
print(response.output_text)
name=input("이름을 입력하세요:")
print("안녕하세요.",name + "님!")
print("엄마와 함께 AI 에이전트입니다.")
print("엄마와 함께 한 걸음 나아가 볼까요?")
mood = input("오늘 기분은 어떠신가요?")
response = client.responses.create(
    model="gpt-5-mini",
    input="편안하고 자연스럽게 존댓말로 짧게 답해주세요.조언이나 제안, 질문으로 대화를 이어가려 하지 마세요.\n기분:" + mood
)
print(response.output_text)
history = ""
while True:
    question = input("무엇을 이야기하고 싶으세요?")
    if question == "종료": 
        break
    response = client.responses.create (
            model="gpt-5-mini",
                input="편안하고 자연스럽게 대화하되 항상 존댓말을 사용하세요.사용자의 말을 성급히 해석하거나 설명하려 하지 마세요.덧붙이는 조언.제안.질문 없이 필요한 말만 짧게 답하세요. \n이름:" + name + "\n기분:" + mood + "\n질문:" + "\n대화기록:" + "\n이전 대화:" + history + "\n사용자:" + question 
                ) 
    print(response.output_text)
    history = history + "\n사용자:" + question + "\nAI:" + response.output_text       
    