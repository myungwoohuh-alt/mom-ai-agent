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
def add_title(text,size=25,x=25,y=30):
    title = tk.Label(root, text=text,
    font=("나눔고딕",size,"bold"))
    title.place(x=x,y=y)
def add_next_button(text,command,x=650,y=480,size=12):
    button=tk.Button(root,text=text,
    font=("나눔고딕",size), command=command)
    button.place(x=x,y=y)
def add_previous_button(text,command,x=50,y=480,size=12):
    button=tk.Button(root,text=text,
    font=("나눔고딕",size),command=command)
    button.place(x=70,y=y)
def add_message(text,x=70,y=100,size=16):
    message=tk.Label(root,text=text,
    font=("나눔고딕",size),justify="left")
    message.place(x=x,y=y)
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
    font=("나눔고딕",20,"bold"))
    title.place(x=30,y=20)
    go=tk.Button(root,text="Go!",
    font=("나눔고딕",14,"bold"),
    command=show_ready)
    go.place(x=800,y=550)
#-------------
# 컷 2 : 사전 준비물 확인
#-------------
def show_ready():
    clear_screen()
    add_title("사전 준비물 확인",x=70,size=30)
    computer=tk.Checkbutton(root,text="노트북이나 컴퓨터 준비됐나요?",
    font=("나눔고딕",18))
    computer.place(x=70,y=150)
    internet=tk.Checkbutton(root,text="인터넷에 연결할 수 있는 'Chrome' 같은 프로그램이 준비되어 있나요?",
    font=("나눔고딕",18))
    internet.place(x=70,y=230)
    chatgpt=tk.Checkbutton(root,text="휴대폰에서 'ChatGpt' 같은 'AI'와 직접 이야기할 준비 되어있나요?",
    font=("나눔고딕", 18))
    chatgpt.place(x=70,y=310)
    add_previous_button("이전",show_entrance,x=70)
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
    font=("나눔고딕",20,"bold"))
    title.place(x=30,y=20)
    add_next_button("장착할 도구들을 찾아볼까요?",show_browser,y=540)
    add_previous_button("이전",show_ready,y=540)
#-------------------
# 컷 4 : 인터넷 연결 확인
#-------------------
def show_browser():
    clear_screen()
    add_title("'인터넷 연결' 확인 하세요.",x=70,size=26)
    text=("이 동굴은 인터넷에 연결해야 우리와 대화할 수 있어요.\n\n"
    "어떤 도구가 제일 먼저 필요할까요?\n\n"
    "바로 '브라우저'입니다.\n\n"
    "아까 동굴 앞에서 'Chrome'이 컴퓨터에 설치되어 있는 것 확인했었죠?\n"
    "그 'Chrome'이 바로 다양한 '브라우저' 중의 하나입니다.\n\n"
    "여기서도 잘 연결되나 한번 실행해 볼까요?")
    message = tk.Label(root,text=text,
    font=("나눔고딕",18), justify="left")
    message.place(x=70,y=140)
    add_next_button("엄마와 함께 실행 확인했어요.",show_ai)
    add_previous_button("이전",show_tool_room,x=70)
#--------------------
# 컷 5 : AI와 이야기하기
#--------------------
def show_ai():
    clear_screen()
    add_title("'AI'와 이야기하기",x=70,size=28)
    text=("'AI'에게 바로 전에 연결했던 '브라우저'에 대해\n"
    "궁금했던 것을 물어보려면 어떻게 해야 할까요?\n\n"
    "휴대폰에서 'ChatGpt'를 누르고\n"
    "질문하는 곳에 궁금했던 것들을 입력해 보세요.\n"
    "선생님처럼 편안하게 질문하면 됩니다.\n\n"
    "그런데, 'AI'도 가끔 실수할 수도 있어요.\n"
    "중요한 내용일수록 다시 한번 확인하는\n"
    "습관을 들이는게 좋아요.")
    message=tk.Label(root,text=text,
    font=("나눔고딕",18), justify="left")
    message.place(x=70,y=140)
    finish=tk.Button(root,
    text="브라우저와 AI 연결 다 확인했어요.",
    font=("나눔고딕",12),
    command=show_two_tools)
    finish.place(x=620,y=480)
    add_previous_button("이전",show_browser,x=70)
#-------------------------
# 컷 6 : 새로운 두가지 도구
#-------------------------
def show_two_tools():
    clear_screen()
    add_title("새로운 두가지 도구",x=70,size=28)
    text=("동굴과 소통하기 위한 도구들을 준비해 볼까요?\n\n"
    "하나는 코드를 쓰고 고치는 작업실인 'VS Code'입니다.\n\n"
    "다른 하나는 우리가 쓴 코드를 읽고,\n"
    "실제로 움직이게 해주는 'Python'입니다.\n\n"
    "'Python'은 누구나 사용할 수 있는 '오픈소스' 도구입니다.\n\n"
    "궁금한 것은 휴대폰 'AI'에게 물어보세요.")
    add_message(text,x=70,y=140,size=18)
    add_next_button("'Python'부터 만나볼까요?",show_python_download)
    add_previous_button("이전",show_ai,x=70)
#----------------------------
# 컷 7: Python 다운로드
#----------------------------
def show_python_download():
    clear_screen()
    add_title("'Python' 다운로드 하세요.",x=70,size=28)
    text=("'브라우저' 검색 창에 'Python'을 입력합니다.\n\n"
    "'Python' 사이트를 찾아 'Download'를 누르고,\n"
    "다운로드가 끝난 후 화면에 표시되는 'Python'을 클릭하세요.\n\n"
    "'Python'을 컴퓨터에서 준비하는 설치 화면이 나타나면,\n"
    "화면의 안내에 따라 설치를 끝내세요.\n\n"
    "설치가 끝나면 윈도우 아래쪽 검색 창에 'Python'이라고 입력하고,\n"
    "'Python'이 나타나면 클릭해서 직접 열어 보세요.\n\n"
    "창이 열렸나요? 그러면 제대로 설치된 겁니다.")
    add_message(text,y=130,size=18)
    add_next_button("'Python' 설치 확인했어요.",show_vscode_download,y=520)
    add_previous_button("이전",show_two_tools,x=70,y=520)
#------------------------------
# 컷 8: VS Code 다운로드
#------------------------------
def show_vscode_download():
    clear_screen()
    add_title("'VS Code' 다운로드 하세요.",x=80,size=28)
    text=("'브라우저' 검색 창에 'VS Code'를 입력하세요.\n\n"
    "'Visual Studio Code' 공식 사이트를 찾아서,\n"
    "'다운로드'하고 화면의 안내에 따라 설치하세요.\n\n"
    "설치가 끝나면 윈도우 아래 쪽 검색 창에 'VS Code'라고 입력합니다.\n"
    "'VS Code'가 나타나면 클릭해서 직접 열어 보세요.\n\n"
    "창이 열렸나요? 그러면 제대로 설치된 겁니다.\n\n"
    "앞으로 자주 돌아오게 될 우리의 작업실입니다.")
    add_message(text,x=80,y=130,size=18)
    add_next_button("'VS Code'도 준비됐어요.",show_workspace)
    add_previous_button("이전",show_python_download,x=80)
#-------------------------------
# 컷 9: 우리의 작업실
#-------------------------------
def show_workspace():
    clear_screen()
    add_title("'코드 작업실' 입니다.",x=90,size=28)
    text=("'VS Code'창을 찬찬히 살펴볼까요?\n\n"
    "위쪽 넓은 곳은 코드를 쓰고 고치는'\n"
    "작업 공간입니다.\n\n"
    "'터미널'이라고 하는 아래쪽 공간은,\n"
    "입력한 코드를 직접 확인하는 곳입니다.\n\n"
    "다시말해서 위에서 코드 만들고,\n"
    "아래에서 만든 코드를 실행하는 겁니다.")
    add_message(text,x=90,y=130,size=18)
    add_next_button("작업실 구조를 확인했어요.",show_run_method)
    add_previous_button("이전",show_vscode_download,x=90)  
#--------------------------------
# 컷 10: 저장하고 실행하기
#--------------------------------
def show_run_method():
    clear_screen()
    add_title("저장하고 실행하기",size=28,x=90)
    text=("코드를 입력한 후 'Ctrl + S'를 눌러서,\n"
    "반드시 저장부터 먼저 해야겠죠?\n\n"
    "그다음 아래 터미널에 커서를 놓고\n"
    "'python xxxx.py'를 쓰고 'Enter'로 실행하세요.\n\n"
    "'xxxx'는 코드 작업했던 파일이름입니다.\n"
    "내 파일에서 만든 이 코드를,\n"
    "실행해 달라고 부탁하는 거예요.\n\n")
    add_message(text,x=90,y=140,size=18)
    add_next_button("이제 직접 해볼까요?",show_nickname)
    add_previous_button("이전",show_workspace,x=90)
#----------------------------------
# 컷 11: 닉네임 만들기
#----------------------------------
def show_nickname():
    clear_screen()
    add_title("이름 만들기",x=90,size=28)
    text=("우리를 부를 때 이름이 필요하겠죠?\n\n"
    "'미래로 통하는 동굴'에서 사용될,\n"
    "의미있는 닉네임을 하나 생각해 보세요.\n\n"
    "엄마도 하나 만들어 보세요.\n"
    "왜 그렇게 정했는지 서로 한번 이야기해 보세요.\n\n"
    "탐사 중 그 의미를 잊지마세요.")
    add_message(text,x=90,y=130,size=18)
    add_next_button("우리 이름 정했어요.",show_first_code)
    add_previous_button("이전",show_run_method,x=90)
#------------------------------------
# 컷 12: 첫 코드
#------------------------------------
def show_first_code():
    clear_screen()
    add_title("동굴과의 첫 소통",x=70,size=28)
    text=("먼저 'VS Code'에서 새 'Python' 파일 하나 만드세요.\n"
    "파일의 이름을 'hello_cave'라고 정하면 어떨까요?\n\n"
    "위쪽 작업공간에 아래처럼 코드를 입력해 보세요.\n\n"
    'name = input("당신의 닉네임은?")\n'
    'print("안녕,",name)\n'
    'print("미래로 통하는 동굴에 온 것을 환영해!")\n\n'
    "점하나 틀려도 연결 안될 수 있으니 꼭 검토하세요.\n\n"
    "확인됐으면 'Ctrl + S'를 눌러 꼭 저장하세요.")
    add_message(text,y=130,size=18)
    add_next_button("코드 입력하고 저장했어요.",show_first_run,y=520)
    add_previous_button("이전",show_nickname,x=70,y=520)
#--------------------------------------
# 컷 13: 첫 실행
#--------------------------------------
def show_first_run():
    clear_screen()
    add_title("첫 실행",x=80,size=27)
    text=("'python hello_cave.py'라고 쓰고,\n"
    "'터미널'에서'Enter'를 눌러 실행해 보세요.\n\n"
    "당신이 누구냐고 물어 보나요?\n"
    "당신의 닉네임을 입력해 보세요.\n\n"
    "와우!\n"
    "환영한다고 하나요?\n\n"
    "당신이 만든 코드로 동굴과 처음으로 소통 됐습니다.")
    add_message(text,y=140,size=18)
    add_next_button("첫 소통 성공!",show_mom_code,y=530)
    add_previous_button("이전",show_first_code,x=80,y=530)
#----------------------------------------
# 컷 14: 엄마도 함께
#----------------------------------------
def show_mom_code():
    clear_screen()
    add_title("엄마도 함께",x=80,size=28)
    text=("이번에는 코드에 엄마의 이름도 넣어볼까요?\n"
    "앞에했던 코딩에 추가 합니다.\n\n"
    'name=input("당신의 닉네임은?")\n'
    'mom=input("함께하는 엄마의 닉네임은?")\n'
    'print("안녕,", name)\n'
    'print(mom,"정말 반갑습니다.")\n'
    'print("우리의 첫 번째 연결 시작 되었어요!")\n\n'
    "검토 후 'Ctrl+S'로 저장, 아래 '터미널'에서,\n"
    "'python hello_cave.py'를 쓰고 'Enter'로 실행합니다.\n\n"
    "엄마도 동굴과 인사했나요?")
    add_message(text,x=80,y=110,size=18)
    add_next_button("둘 다 소통됐어요!",show_finish_today,y=530)
    add_previous_button("이전",show_first_run,x=80,y=530)
#----------------------------------------
# 컷 15: 오늘은 여기까지
#----------------------------------------
def show_finish_today():
    clear_screen()
    add_title("오늘은 여기까지",x=80,size=28)
    text=("동굴이 첫 인사한 것으로 충분하니,\n"
    "오늘 탐사는 여기까지라고 하네요.\n\n"
    "그러면, 코드에 다음처럼 한 줄 더 추가해야 합니다.\n\n"
    'input("소통을 마치려면 종료라고 입력하세요:")\n\n'
    "이전처럼 저장하고 다시 터미널에서 실행한 후,\n"
    "마지막 질문 다음에 '종료'라 입력한 후 'Enter'를 누르세요.\n\n"
    "그러면 '실행'으로 다시 부를 때까지 소통할 수 없습니다.")
    add_message(text,x=80, y=120,size=18)
    add_next_button("'준비단계' 일정 끝났네요.",show_review)
    add_previous_button("이전",show_mom_code,x=80)
#------------------------------------------
# 컷 16: 엄마와 함께 되돌아 보기
#------------------------------------------
def show_review():
    clear_screen()
    add_title("'준비 단계'에서 어떤 경험들을 했죠?",x=70,size=28)
    text=("'도구방'에서 장착한 도구들은 뭐가 있었죠?\n\n"
    "'코드 작업'은 어디에서 어떻게 했었죠?\n\n"
    "'코드 작업'으로 동굴에게 내용들을,\n"
    "왜 미리 알려주었을까요?\n\n"
    "엄마와 함께 이야기 해보고,\n"
    "더 궁금한 것들 있으면 휴대폰 'AI'에게도 물어보세요.")
    add_message(text,y=140,size=18)
    add_next_button("많이 생각해 봤어요.",show_last)
    add_previous_button("이전",show_finish_today,x=70)
#---------------------------------------------
# 컷 17: 진짜 탐사의 시작
#---------------------------------------------
def show_last():
    clear_screen()
    add_title("이제부터 진짜 탐사",x=90,size=28)
    text=("필요한 도구들 찾아 코드 작업하고,\n"
    "연결해 동굴과 첫 대화를 경험 했습니다.\n\n"
    "그런데, 이상한 점 못 느끼셨나요?\n"
    "이 동굴은 미리 입력된 규칙대로만 반응합니다.\n\n"
    "왜 그럴까요?\n\n"
    "또 다른 방법을 찾을 수 있는지,\n"
    "본격적인 다음 탐사로 직접 경험해 볼까요?")
    add_message(text,x=90,y=120,size=20)
    add_previous_button("이전",show_review,x=90)

show_entrance()
root.mainloop()
