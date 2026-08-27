import tkinter as tk 
from PIL import Image, ImageTk
root = tk.Tk()
root.title("미래로 통하는 동굴")
root.geometry("900x600")
#-------------
#공통기능
#-------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
def add_title(text):
    title = tk.Label(root, text=text,
    font=("Arial",20,"bold"))
    title.place(x=30,y=20)
def add_next_button(text,command):
    button=tk.Button(root,text=text,
    font=("Arial",12), command=command)
    button.place(x=600,y=480)
#---------------
# 컷 1: 미래로 통하는 동굴
#---------------
def show_entrance():
    clear_screen()
    image=Image.open("cave_entrance.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    background=tk.Label(root,image=photo)
    background.image=photo
    background.place(x=0,y=0)
    title=tk.Label(root,text="미래로 통하는 동굴",
    font=("Arial",20,"bold"))
    title.place(x=30,y=20)
    go=tk.Button(root,text="Go!",
    font=("Arial",14,"bold"),
    command=show_ready)
    go.place(x=260,y=20)
#-------------
# 컷 2 : 사전 준비물 확인
#-------------
def show_ready():
    clear_screen()
    add_title("사전 준비물 확인")
    computer=tk.Checkbutton(root,text="노트북이나 컴퓨터 준비됐나요?",
    font=("Arial",16))
    computer.place(x=70,y=120)
    internet=tk.Checkbutton(root,text="인터넷에 연결할 수 있는 Chrome 같은 프로그램이 준비되어 있나요?",
    font=("Arial",16))
    internet.place(x=70,y=200)
    chatgpt=tk.Checkbutton(root,text="휴대폰에서 ChatGpt 같은 AI와 직접 이야기할 준비 되어있나요?",
    font=("Arial", 16))
    chatgpt.place(x=70,y=280)
    add_next_button("OK! 함께 들어갈까요?", show_tool_room)
#----------------
# 컷 3: 도구방
#----------------
def show_tool_room():
    clear_screen()
    image=Image.open("cave_inside.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    background=tk.Label(root,image=photo)
    background.image=photo
    background.place(x=0,y=0)
    title=tk.Label(root,text="도구방",
    font=("Arial",20,"bold"))
    title.place(x=30,y=20)
    add_next_button("장착할 도구들을 찾아볼까요?",
    show_browser)
#-------------------
# 컷 4 : 인터넷 연결 확인
#-------------------
def show_browser():
    clear_screen()
    add_title("인터넷 연결 확인")
    text=("이 동굴은 인터넷에 연결해야 우리와 대화할 수 있어요.\n\n"
    "어떤 도구가 제일 먼저 필요할까요?\n\n"
    "브라우저입니다.\n\n"
    "아까 동굴 앞에서 Chrome이 컴퓨터에 설치되어 있는 것 확인했었죠?\n"
    "그 Chrome이 바로 다양한 브라우저 중의 하나입니다.\n\n"
    "여기서도 잘 연결되나 한번 실행해 볼까요?")
    message = tk.Label(root,text=text,
    font=("Arial,16"), justify="left")
    message.place(x=70,y=100)
    add_next_button("엄마와 함께 실행 확인했어요.",
    show_ai)
#--------------------
# 컷 5 : AI와 이야기하기
#--------------------
def show_ai():
    clear_screen()
    add_title("AI와 이야기하기")
    text=("그러면 이제 AI에게 바로 전에 실행해 본 브라우저에 대해\n"
    "궁금했던 것들을 물어보려면 어떻게 해야 할까요?\n\n"
    "휴대폰에서 ChatGpt를 누르고\n"
    "질문하라는 곳에다 궁금했던 것들을 입력해 보세요.\n\n"
    "선생님에게 물어보듯 잘 모르는 용어나 기능들을 편하게 질문하면 됩니다.\n\n"
    "그런데, AI도 가끔 실수할 수도 있어요.\n"
    "중요한 내용일수록 다시 한번 확인하는 습관을 들이는게 좋아요.")
    message=tk.Label(root,text=text,
    font=("Arial",16), justify="left")
    message.place(x=70,y=100)
    finish=tk.Button(root,
    text="브라우저와 AI 연결 다 확인했어요.",
    font=("Arial",12))
    finish.place(x=620,y=530)
#-------------------------
# 시작
#-------------------------
show_entrance()
root.mainloop()
