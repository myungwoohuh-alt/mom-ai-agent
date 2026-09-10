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
    "새 파일을 'VS Code'에서 만들라고 하네요.\n\n"
    "또한, 아이의 기록을 위한 'child_journey.txt'와,\n"
    "엄마의 기록을 위한 'mom_journey.txt' 두개의 새파일도 요청합니다.\n\n"
    "그렇게하면, 'trip.txt'에 있는 우리 기록들 중에서,\n"
    "'LLM'이 두사람 내용을 각각 분류해서 새파일로 정리한다네요.",size=18,y=120)
    add_previous_button("이전",show_first_step,y=550)
    add_next_button("새파일 만들었어요.",show_structure,y=550)
#--------------------------------------------
# 6:  이 구조와 의미를 알아볼까요.
#--------------------------------------------
def show_structure():
    clear_screen()
    add_title("왜 이렇게 하는지 구조와 의미를 알아볼까요?\n\n",size=30)
    add_message("우리는 'LLM'에게 'trip.txt'의 우리 내용들을,\n"
    "각각 분류해서 계속 사용할 수 있게 해달라고 부탁했어요.\n\n"
    "이에따라, 'LLM'은 먼저 이러한 작업할 손쉽게할 수 있는,\n"
    "새파일 'record_agent.py'를 만들어 달라고 했고,\n"
    "분류 후 두사람 각각의 기록을 보관할 새파일도 함께 요청했습니다.\n\n"
    "직접 도움 줄 수있는 'AI Agent'로서 역할을 시작하려는 겁니다.",size=20,y=140)
    add_previous_button("이전",show_new_tool)
    add_next_button("잘 알았습니다.",show_code_1)
#---------------------------------------------
# 7: 어떻게 코딩을 해야 LLM에게 부탁할 수 있나요?
#---------------------------------------------
def show_code_1():
    clear_screen()
#---------------------------------------------
# 8: 이 코딩의 구조 설명 요약 1.
#---------------------------------------------

#--------------------------------------------------------
# 9: 'llm'이 'record_agent.py'에서 작업 할 수 있게하는 코딩은?
#---------------------------------------------------------

#-----------------------------------------------------
# 10: 이 코딩의 구조 설명 요약 2.
#------------------------------------------------

#-----------------------------------------------
# 11: 아이와 엄마의 새파일로 분류해서 보내달라는 코딩은?
#-----------------------------------------------

#-----------------------------------------------
# 12: 이 코딩의 구조 설명 요약 3.
#----------------------------------------------

#--------------------------------------------
# 13: 앞으로도 계속 이렇게 작업해 줄 수있는 코딩은?
#--------------------------------------------    




show_child_safety()
root.mainloop()