from openai import OpenAI
from dotenv import load_dotenv
import os
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
MAX_HISTORY = 1000
HISTORY_FILE = "history.txt"
MEMORY_FILE = "memory.txt"
memory = ""
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE,"r", encoding="utf-8") as file:
        memory=file.read()
history=""
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE,"r", encoding="utf-8") as file:
        history=file.read()
while True:
    question = input("무엇을 이야기하고 싶으세요?")
    if question == "종료": 
        break
    elif question == "기억삭제":
        history=""
        with open(HISTORY_FILE,"w", encoding="utf-8") as file:
            file.write("")
        print("기억을 삭제했어요.")
        continue
    elif question.startswith("기억해:"):
        new_memory = question.replace("기억해:", "").strip()
        with open(MEMORY_FILE,"a", encoding = "utf-8") as file:
            file.write(new_memory + "\n")
        memory = memory + new_memory + "\n"
        print("중요한 기억으로 저장했어요.")
        continue
    elif question == "중요기억삭제":
        memory = ""
        with open(MEMORY_FILE,"w", encoding = "utf-8") as file:
            file.write("")
        print("중요한 기억을 삭제했어요.")
        continue
    elif question == "중요기억보기":
        with open(MEMORY_FILE,"r",encoding = "utf-8") as file:
            memory = file.read()
        print("중요기억:",memory)  
        continue
    elif question.startswith("기억찾기"):
        keyword = question.replace("기억찾기:", "").strip()
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
        matches = [line.strip() for line in lines if keyword in line]
        if matches:
            print("찾은 기억:", matches)
        else:
            print("찾은 기억이 없어요.")
        continue
    elif question.startswith("중요기억선택삭제:"):
        target = question.replace("중요기억선택삭제:", "").strip()
        with open(MEMORY_FILE,"r", encoding = "utf-8") as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() !=target]
        with open(MEMORY_FILE,"w", encoding = "utf-8") as file:
            file.writelines(lines)
        print("선택한 중요기억을 삭제했어요.")
        continue
    elif question in  ["도움", "도와줘", "도와주세요."]:
        print("어떤 도움이 필요한지 말씀해 주세요.")
        continue
    elif question == "안내":
        print("종료, 도움 또는 자유롭게 이야기할 수 있어요.")
        continue
    elif question == "👍":
        print("새로운 아이디어가 떠올랐군요.")
        continue
    response = client.responses.create (
            model="gpt-5-mini",
                input="사용자의 말에서 분위기를 파악하되 평가하거나 설명하지 말고 답변에 자연스럽게 반영하세요. 편안하고 자연스럽게 대화하되 항상 존댓말을 사용하세요.사용자의 말을 성급히 해석하거나 설명하려 하지 마세요.덧붙이는 조언.제안.질문 없이 필요한 말만 짧게 답하세요."+"\n이전대화:"+ history + "\n사용자:" + question + "\n중요기억:" + memory
                ) 
    print(response.output_text)
    history = history + "\n사용자:" + question + "\nAI:" + response.output_text       
    history = history[-MAX_HISTORY:]
    with open(HISTORY_FILE,"w", encoding="utf-8")as file:
        file.write(history)