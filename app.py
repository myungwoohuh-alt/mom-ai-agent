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
if "좋아" in mood:
    print("기분이 좋으시다니 저도 좋아요!")
elif "힘들" in mood:
    print("힘드시군요. 잠시 쉬어가도 괜찮아요.")
else:
    response = client.responses.create(
        model="gpt-5-mini",
        input=mood
)
    print(response.output_text)
print("말해 주셔서 감사합니다.")
print("자, 오늘도 함께 한 걸음 또 나아가 볼까요?")
while True:
    print("다시 질문합니다.")
    question = input("무엇을 이야기하고 싶으세요?")
    print("말씀하신 내용:", question)
    if "재미" in question:
        print("재미를 느끼셨군요!")
    elif "힘들" in question:
        print("힘드셨군요. 잠시쉬어가도 괜찮아요.")
    else:
        response = client.responses.create (
            model="gpt-5-mini",
                input="2-3문장으로 짧게 요약 친근하게 답해주세요.\n질문:" + question
                ) 
        print(response.output_text)       
    answer = input("계속 할까요? (종료하려면 '종료' 입력):")
    if answer == "종료":
        break