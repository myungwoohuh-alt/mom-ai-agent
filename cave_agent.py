import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
root.title("AI 에이전트 만들기")
root.geometry("900x600")
#----------------------
# 공통기능
#----------------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
def add_title(text,size=25,x=70,y=20):
    title=tk.Label(root,text=text,
    font=("나눔고딕",size,"bold"))
    title.place(x=x,y=y)
def add_next_button(text,command,size=12,x=650,y=480):
    button=tk.Button(root,text=text,
    font=("나눔고딕",size,"bold"),
    command=command)
    button.place(x=x,y=y)
def add_previous_button(text,command,size=12,x=70,y=480):
    button=tk.Button(root,text=text,
    font=("나눔고딕",size,"bold"),
    command=command)
    button.place(x=x,y=y)
def add_message(text,x=70,y=120,size=18):
    message=tk.Label(root,text=text,
    font=("나눔고딕",size,"bold"),justify="left")
    message.place(x=x,y=y)
#--------------------------------
# 1: 아이들 관련 기본 안전 문구
#--------------------------------
def show_child_safety():
    clear_screen()
    add_message("'미래로 통하는 동굴' 탐사 프로그램은,\n"
    "13세 이상을 대상으로 하며, 보호자와 함께 참여합니다.\n" 
    "계속 진행하면 위 안내와 아래 사항에 동의한 것으로 간주합니다.\n\n",size=20,x=70,y=130)
    add_message("* 개인정보는 입력하거나 공개하지 않습니다.\n" 
    "* 비밀번호와 API Key는 다른 사람에게 보여주지 않습니다.\n"
    "* 모르는 파일이나 프로그램은 함부로 설치하지 않습니다.\n"
    "* 결제나 비용이 발생하는 작업은 보호자와 함께 확인하고 승인합니다.\n"
    "* 'AI'의 답변은 틀릴 수 있으니 중요한 내용은 한 번 더 확인합니다.",size=18,x=70,y=270)
    add_next_button("탐사시작",show_cover)
#--------------------------------
# 2: 겉 표지
#--------------------------------
def show_cover():
    clear_screen()
    image=Image.open("cave_agent_cover_left_title.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_next_button("Go!",show_cave_end,x=800,y=530)
    add_previous_button("이전",show_child_safety,y=530)
#----------------------------------
# 3: 지난 탐사 되돌아보기
#---------------------------------
def show_cave_end():
    clear_screen()
    add_title("동굴 끝까지 거의 다왔어요.",size=28)
    add_message("지나왔던 탐사과정들을 되돌아 볼까요?\n\n"
    "'Python'과 'VS Code' 도구로 직접 코드 만들어 실행까지 했었죠?\n\n"
    "두갈래 길에서는 'if'와 'else'를 만났고,\n"
    "더 많은 선택의 길에선 'elif'까지 사용해 봤어요.\n\n"
    "그리고, 동굴이 요청했던 새로운 'LLM' 도구로,\n"
    "우리와 외부 'AI' 세계와의 연결도 실현시켰죠?\n\n"
    "새로운 경험들로 시간이 이렇게 빨리 지나간 것도 몰랐네요.",size=18,y=130)
    add_previous_button("이전",show_cover)
    add_next_button("밖으로 나갈까요?",show_first_step)
#---------------------------------------
# 4: 그냥 나가기엔 아쉬워요
#--------------------------------------
def show_first_step():
    clear_screen()
    add_title("나가기 전에 할일이 있어요.",size=28)
    add_message("엄마와 함께 탐사하는 동안,\n"
    "각각 자신의 느낌을 'trip.txt'에 요약해 놓았죠?\n\n"
    "혹시 빠진 것들이 있을지 모르니,\n"
    "지금이라도 잊기 전에 빨리 기록으로 남기세요.\n\n"
    "아이도 엄마도 서로의 생각과 느끼는 것이 다르니,\n"
    "각각 따로따로 탐사했던 흐름에 따라서 요약해 보세요.\n\n"
    "그리고나서 우리가 경험했던 기록들을,\n"
    "정리해서 가지고 나가면 좋지 않을까요?",size=18,y=130)
    add_previous_button("이전",show_cave_end)
    add_next_button("좋아요!",show_new_tool)
#-----------------------------------------
# 5: 새로운 도구로 정리 쉽게 할 수 있어요.
#-----------------------------------------
def show_new_tool():
    clear_screen()
    add_title("새로운 도구 'LLM'에게 정리 부탁해 볼까요? ",size=28)
    add_message("동굴도 새로운 도구인 'LLM'으로,\n"
    "기록 정리를 충분히 도와줄 수 있다고 하네요.\n\n"
    "자세히 안내할테니 잘 따라오라고 합니다.\n\n"
    "먼저, 이러한 목표를 수행하기 위한 'record_agent.py'라는\n" 
    "새 파일을 'VS Code'에서 만들어 달라고 합니다.\n\n"
    "그렇게하면, 'trip.txt'에 있는 우리 기록들 중에서,\n"
    "'LLM'이 두사람을 각각 분류해서 새파일로 정리한다고 하네요.",size=18,y=130)
    add_previous_button("이전",show_first_step)
    add_next_button("새파일 만들었어요.",show_structure)
#--------------------------------------------
# 6:  이 구조와 의미를 알아볼까요.
#--------------------------------------------
def show_structure():
    clear_screen()
    add_title("왜 이렇게 하는지 구조와 의미를 알아볼까요?\n\n",size=28)
    add_message("우리는 'LLM'에게 'trip.txt'의 우리 내용들을,\n"
    "각각 분류해서 계속 사용할 수 있게 해달라고 부탁했어요.\n\n"
    "이에따라, 'LLM'은 먼저 이러한 작업할 쉽게할 수 있는,\n"
    "새파일 'record_agent.py'를 만들어 달라고 요청했습니다.\n\n"
    "그 파일이 만들어진 후 두사람 각각의 기록을 분류 보관한다고 합니다.\n\n"
    "직접 도움 줄 수있는 'AI Agent'로서 역할을 시작하려는 겁니다.",size=18,y=140)
    add_previous_button("이전",show_new_tool)
    add_next_button("잘 알았습니다.",show_prompt_1)
#---------------------------------------------
# 7: 어떻게 'LLM'에게 부탁할 수 있나요?
#---------------------------------------------
def show_prompt_1():
    clear_screen()
    add_title("어떻게 'LLM'에게 부탁할 수 있을까요?",size=28)
    add_message("먼저 'record_agent.py'가\n" 
    "해야 할 일들을 간단히 살펴보아야 합니다.\n\n"
    "1. 'trip.txt'에 저장된 '탐사기록'을 읽습니다.\n\n"
    "2. 'LLM'에게 기록을 정리해 달라고 부탁합니다.\n\n"
    "3. '엄마와 아이의 기록'을 각각 나누어 정리합니다.\n\n"
    "4. '새로운 파일'에 정리한 내용을 저장합니다.\n\n"
    "이렇게 중간에서 여러가지 일을하는 'Python 파일'입니다.",size=18,y=110)
    add_previous_button("이전",show_structure)
    add_next_button("어떻게 부탁하죠?",show_prompt_2)
#---------------------------------------------
# 8: 프롬프트
#---------------------------------------------
def show_prompt_2():
    clear_screen()
    add_title("'AI'에게 어떻게 부탁하는게 효율적일까요?",size=28)
    add_message("'AI'에게 부탁할 때는 자세하고 분명하게\n"
    "무엇을 원하는지 알려주는 것이 중요한 요령입니다.\n\n"
    "즉, '우리 탐사기록을 정리해 주세요.'보다는,\n\n"
    "'trip.txt의 탐사기록 읽고,\n"
    "엄마와 아이 기록 구분 정리한 뒤,\n"
    "각각 다른 파일로 저장해 주세요.'라고 하면,\n"
    "부탁한 일이 훨씬 정확하고 분명해 집니다.\n\n"
    "'AI'가 부탁하는 것을 더 잘 이해할 수있게\n"
    "구체적으로 질문하고 부탁하는 것이,\n"
    "바로 효율적으로 '프롬프트(prompt)'하는 방법입니다.",size=18,y=110)
    add_previous_button("이전",show_prompt_1,y=520)
    add_next_button("효율적 '프롬프트' 이해했습니다.",show_code_1,x=550,y=520)
#--------------------------------------------------------
# 9: 'record_agent.py' 첫 번째 코딩
#---------------------------------------------------------
def show_code_1():
    clear_screen()
    add_title("먼저 '탐사 기록'을 읽어 볼까요?",size=25)
    add_message("새파일 'record_agent.py'를 열고,\n"
    "'VS Code'의 위쪽 작업장에 아래 코드를 입력하세요.\n\n"
    "from openai import OpenAI\n"
    "from dotenv import load_dotenv\n\n"
    "load_dotenv()\n"
        "client=OpenAI()\n\n"
        "with open(\"trip.txt\",\"r\",encoding=\"utf-8\")as file:\n"
        "trip=file.read()\n\n"
    "여기까지는 'trip.txt'에 있는 '탐사기록'을\n"
    "'AI'가 사용할 수있게 불러오는 코딩입니다.\n\n"
    "복잡하지만 문법이라 점 하나까지 정확하게 확인하세요.",size=17,y=100)
    add_previous_button("이전",show_prompt_2,y=540)
    add_next_button("다음 코딩은?",show_code_2,y=540)
#-------------------------------------------
# 10: 'LLM'에게 실제로 부탁하기
#------------------------------------------- 
def show_code_2():
    clear_screen()
    add_title("이제 'LLM'에게 일을 부탁해 볼까요?",size=25)
    add_message("방금 읽은 탐사기록과 함께\n"
    "우리가 원하는 일을 'LLM'에게 전달합니다.\n\n"
    "prompt=f\"\"\"\n"
    "다음은 엄마와 아이의 공동 탐사 기록입니다.\n\n"
    "{trip}\n\n"
    "이 기록에 없는 사실은 만들지 마세요.\n"
    "엄마와 아이의 닉네임으로 구분해서 내용을 정리해 주세요.\n"
    "\"\"\"\n\n"
    "이 부분이 바로 조금 전에 살펴본\n"
    "'프롬프트(prompt)'입니다., size=18,y=130")
    add_previous_button("이전",show_code_1)
    add_next_button("'LLM'과 연결",show_code_3)
#-------------------------------------------------
# 11: 'LLM' 호출
#------------------------------------------------
def show_code_3():
    clear_screen()
    add_title("'프롬프트'를 'LLM'에게 보낼까요?",size=25)
    add_message("")
 




show_child_safety()
root.mainloop()