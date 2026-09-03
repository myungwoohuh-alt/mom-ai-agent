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
def add_previous_button(text,command,y=480):
    button=tk.Button(root,text=text,
    font=("Arial",12),command=command)
    button.place(x=70,y=y)
def add_message(text,x=70,y=100,size=16):
    message=tk.Label(root,text=text,
    font=("Arial",size),justify="left")
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
    font=("Arial",20,"bold"))
    title.place(x=30,y=20)
    go=tk.Button(root,text="Go!",
    font=("Arial",14,"bold"),
    command=show_ready)
    go.place(x=600,y=480)
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
    add_previous_button("이전",show_entrance)
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
    add_previous_button("이전",show_ready)
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
    "여기서도 잘 연결되나 한번 실행해 볼까요?\n\n")
    message = tk.Label(root,text=text,
    font=("Arial,16"), justify="left")
    message.place(x=70,y=100)
    add_next_button("엄마와 함께 실행 확인했어요.",
    show_ai)
    add_previous_button("이전",show_tool_room)
#--------------------
# 컷 5 : AI와 이야기하기
#--------------------
def show_ai():
    clear_screen()
    add_title("AI와 이야기하기")
    text=("그러면 이제 AI에게 바로 전에 실행해 본 브라우저에 대해\n"
    "궁금했던 것들을 물어보려면 어떻게 해야 할까요?\n\n"
    "휴대폰에서 ChatGpt를 누르고\n"
    "질문하라는 곳에 궁금했던 것들을 입력해 보세요.\n\n"
    "선생님에게 물어보듯 잘 모르는 용어나 기능들을 편하게 질문하면 됩니다.\n\n"
    "그런데, AI도 가끔 실수할 수도 있어요.\n"
    "중요한 내용일수록 다시 한번 확인하는 습관을 들이는게 좋아요.\n\n")
    message=tk.Label(root,text=text,
    font=("Arial",16), justify="left")
    message.place(x=70,y=100)
    finish=tk.Button(root,
    text="브라우저와 AI 연결 다 확인했어요.",
    font=("Arial",12),
    command=show_two_tools)
    finish.place(x=620,y=530)
    add_previous_button("이전",show_browser)
#-------------------------
# 컷 6 : 새로운 두가지 도구
#-------------------------
def show_two_tools():
    clear_screen()
    add_title("새로운 두가지 도구")
    text=("이제 동굴과 직접 소통하기 위한 도구들을 준비해 볼까요?\n\n"
    "하나는 코드를 쓰고 고치는 작업실인 VS Code입니다.\n\n"
    "다른 하나는 우리가 쓴 코드를 읽고\n"
    "실제로 움직이게 해주는 Python입니다.\n\n"
    "Python은 누구나 사용할 수 있는 오픈소스 도구입니다.\n\n"
    "궁금한 것 있으면 휴대폰 AI에게 두가지 도구들의 역할을 물어보세요.\n\n")
    add_message(text)
    add_next_button("먼저 Python부터 만나볼까요?",show_python_download)
    add_previous_button("이전",show_ai)
#----------------------------
# 컷 7: Python 다운로드
#----------------------------
def show_python_download():
    clear_screen()
    add_title("Python 다운로드")
    text=("브라우저 검색창에 Python을 입력해 보세요.\n\n"
    "Python 사이트를 찾아서 Download를 선택합니다.\n\n"
    "다운로드가 끝나면 화면에 방금 내려받은 Python이 표시됩니다.\n\n"
    "그 곳을 클릭해 보세요.\n\n"
    "Python을 컴퓨터에서 사용할 수 있도록 준비하는 설치 화면이 나타납니다.\n\n"
    "화면의 안내에 따라 설치를 끝내세요.\n\n"
    "설치가 끝나면 윈도우 아래쪽 검색 창에 Python이라고 입력해 보세요.\n\n"
    "Python이 나타나면 클릭해서 직접 열어 보세요.\n\n"
    "창이 열렸나요? 그러면 제대로 설치된 겁니다.\n\n")
    add_message(text)
    add_next_button("Python 설치 확인했어요.",show_vscode_download)
    add_previous_button("이전",show_two_tools,y=530)
#------------------------------
# 컷 8: VS Code 다운로드
#------------------------------
def show_vscode_download():
    clear_screen()
    add_title("VS Code 다운로드")
    text=("이번에는 브라우저 검색창에 VS Code를 입력해 봅니다.\n\n"
    "Visual Studio Code 공식 사이트를 찾아서\n"
    "다운로드하고 화면의 안내에 따라 설치를 끝내세요.\n\n"
    "설치가 끝나면 윈도우 아래 쪽 검색 창에 VS Code라고 입력합니다.\n\n"
    "VS Code가 나타나면 클릭해서 직접 열어 보세요.\n\n"
    "창이 열렸나요? 그러면 제대로 설치된 겁니다.\n\n"
    "앞으로 자주 돌아오게 될 우리의 작업실입니다.\n\n"
    "여러 번 닫았다 다시 열어 보세요. 점점 익숙해 질겁니다.\n\n")
    add_message(text)
    add_next_button("VS Code도 준비됐어요.",show_workspace)
    add_previous_button("이전",show_python_download)
#-------------------------------
# 컷 9: 우리의 작업실
#-------------------------------
def show_workspace():
    clear_screen()
    add_title("우리의 작업실")
    text=("VS Code창을 찬찬히 한번 살펴볼까요?\n\n"
    "위쪽 넓은 공간은 코드를 쓰고 고치는 작업 공간입니다.\n\n"
    "터미널이라고 하는 아래쪽 공간은\n"
    "우리가 만든 코드를 직접 실행하고\n"
    "그 결과를 확인하는 장소 입니다.\n\n"
    "다시말해서 위에서 코드 만들고,\n"
    "아래에서 만든 코드를 실행하는 겁니다.\n\n")
    add_message(text)
    add_next_button("작업실 구조를 확인했어요.",show_run_method)
    add_previous_button("이전",show_vscode_download)  
#--------------------------------
# 컷 10: 저장하고 실행하기
#--------------------------------

def show_run_method():
    clear_screen()
    add_title("저장하고 실행하기")
    text=("코드를 입력한 다음에는 반드시 Ctrl + S로 저장하세요.\n"



          
    "Ctrl과 S를 동시에 눌러 저장부터 하라는 겁니다.\n\n"
    "그런 다음 아래 터미널의 반짝이는 곳에 커서를 놓고\n"
    "python xxxx.py라고 쓰고 실행하는 enter를 누르세요.\n\n"
    "xxxx는 코드 작업했던 파일이름입니다.\n"
    "그리고 의미는 내가 만든 이 코드를 실행해 달라고 명령하는 거예요.\n\n")
    add_message(text)
    add_next_button("이제 직접 해볼까요?",show_nickname)
    add_previous_button("이전",show_workspace)
#----------------------------------
# 컷 11: 닉네임 만들기
#----------------------------------
def show_nickname():
    clear_screen()
    add_title("우리 이름 만들기")
    text=("동굴이 우리를 부를 때 이름이 필요하겠죠?\n\n"
          
          

          
    "미래로 통하는 이 동굴에서 사용할\n"
    "나만의 의미있는 닉네임을 하나 생각해 보세요.\n\n"
    "엄마도 하나 만들어 보세요.\n\n"
    "왜 그렇게 정했는지 서로 한번 이야기해 보세요.\n\n"
    "그런 의미가 있다는 것을 마음 속에 새겨두세요.\n\n")
    add_message(text)
    add_next_button("우리 이름 정했어요.",show_first_code)
    add_previous_button("이전",show_run_method)
#------------------------------------
# 컷 12: 첫 코드
#------------------------------------
def show_first_code():
    clear_screen()
    add_title("동굴과 첫 소통")
    text=("먼저 VS Code 창에서 새 Python 파일 하나 만드세요.\n\n"
    "새 파일의 이름을 hello_cave라고 정하면 어떨까요?\n\n"
    "자, 그러면 위쪽 공간에서 처음으로 코드 작업 직접해 볼까요?\n\n"
    "다음처럼 똑같이 코드를 입력해 보세요.\n\n"
    'name = input("당신의 닉네임은?")\n'
    'print("안녕,",name)\n'
    'print("미래로 통하는 동굴에 온 것을 환영해!")\n\n'
    "다 똑 같이 입력됐나 꼭 확인하세요.\n"
    "점 하나, 철자하나 틀려도 연결이 안될 수 있으니까요.\n\n"
    "입력한 작업 재확인됐으면 Ctrl + S를 눌러서 꼭 저장하세요.\n\n")
    add_message(text,y=80,size=15)
    add_next_button("코드 입력하고 저장했어요.",show_first_run)
    add_previous_button("이전",show_nickname)
#--------------------------------------
# 컷 13: 첫 실행
#--------------------------------------
def show_first_run():
    clear_screen()
    add_title("첫 실행")
    text=("이제 아래쪽 터미널로 가세요.\n\n"
    "반짝이는 곳에 커서를 놓고 다음과 같이 입력합니다.\n\n"
    "python hello_cave.py \n\n"
    "그리고 다음엔 직접 Enter를 눌러 실행해 보세요.\n\n"
    "동굴이 당신이 누구냐고 물어 보나요?\n\n"
    "그러면 당신의 닉네임을 입력해 보세요.\n\n"
    "동굴이 당신을 환영한다고 하나요?\n\n"
    "와우!!\n"
    "당신이 직접 만든 코드로 동굴과 처음으로 소통 됐네요.\n\n")
    add_message(text)
    add_next_button("첫 소통 성공!",show_mom_code)
    add_previous_button("이전",show_first_code,y=530)
#----------------------------------------
# 컷 14: 엄마도 함께
#----------------------------------------
def show_mom_code():
    clear_screen()
    add_title("엄마도 함께")
    text=("이번에는 코드에 엄마의 이름도 넣어볼까요?\n\n"
    "앞에했던 코딩을 조금만 더 추가해서 다음처럼 수정합니다.\n\n"
    
    'name=input("당신의 닉네임은?")\n'
    'mom=input("함께하는 엄마의 닉네임은?")\n'
    'print("안녕,", name)\n'
    'print(mom,"정말 반갑습니다.")\n'
    'print("우리의 첫 번째 연결 시작 되었어요!")\n\n'
    
    "재확인 다 끝났으면 반드시 ctrl+s로 저장하세요.\n\n"
    "자, 그러면 터미널에서 python hello_cave.py로\n"
    "아까처럼 입력하고 Enter를 눌러 실행합니다.\n\n"
    "당신이 수정한 코드로 엄마도 함께 동굴과 인사했죠?\n\n")
    add_message(text,y=80,size=15)
    add_next_button("둘 다 소통됐어요!",
    show_finish_today)
    add_previous_button("이전",show_first_run,y=530)
#----------------------------------------
# 컷 15: 오늘은 여기까지
#----------------------------------------
def show_finish_today():
    clear_screen()
    add_title("오늘은 여기까지")
    text=("끝으로 동굴에게 오늘은 여기까지라고 할까요?\n\n"
    "코드 맨 아래에 다음처럼 한 줄 추가합니다.\n\n"
    'input("소통을 마치려면 종료라고 입력하세요:")\n\n'
    "여기까지 수정한 코드 저장하고 다시 터미널에서 실행합니다.\n\n"
    "이 번에는 마지막 질문에 종료라고 입력하고 Enter를 누르세요.\n\n"
    "그러면 다시 실행으로 부를때까지 소통이 종료됩니다.\n\n"
    "지금은 서로 첫 인사한 것만으로도 충분합니다.\n\n")
    add_message(text,y=80,size=15)
    add_next_button("탐사 첫 준비단계 일정 마쳤어요.",show_review)
    add_previous_button("이전",show_mom_code)
#------------------------------------------
# 컷 16: 엄마와 함께 되돌아 보기
#------------------------------------------
def show_review():
    clear_screen()
    add_title("준비 단계에서 어떤 경험들을 직접 했을까요?")
    text=("우리가 준비 단계에서 장착한 도구들은 뭐가 있었죠?\n\n"
    "코드 작업은 어디에서 어떻게 했었죠?\n\n"
    "그리고나서 작업한 코드 실행은 어디에서 어떻게 했었죠?\n\n"
    "동굴이 처음물어 본 것은 무었이었나요?\n\n"
    "그런데, 우리가 직접 동굴에게 미리 알려준 것은 왜 그랬을까요?\n\n"
    "그리고 어떤 방식으로 미리 알려 주어 소통까지 됐었죠?\n\n"
    "엄마랑 이야기 해보고, 더 궁금한 것들 있으면  휴대폰 AI와도 이야기 해보세요.\n\n")
    add_message(text)
    add_next_button("많이 생각해 봤어요.",
    show_last)
    add_previous_button("이전",show_finish_today)
#---------------------------------------------
# 컷 17: 진짜 탐사의 시작
#---------------------------------------------

def show_last():
    clear_screen()
    add_title("이제부터 진짜 탐사")
    text=("우리는 필요한 도구들을 준비하고,\n"
    "직접 코드를 작성하고,\n"
    "실행까지해서 동굴과 처음으로 대화했습니다.\n\n"
    "그런데, 이상한 점 못 느끼셨나요?\n\n"
    "지금 이 동굴은\n"
    "우리기 미리 알려 준 규칙대로만 반응합니다.\n\n"
    "왜 그럴까요?\n\n"
    "이제부터 왜 그런지 다른 방법도 있는지,\n"
    "직접 다음 단계의 진짜 탐사를 시작해 볼까요?\n\n")
    add_message(text)
    add_previous_button("이전",show_review)

show_entrance()
root.mainloop()
