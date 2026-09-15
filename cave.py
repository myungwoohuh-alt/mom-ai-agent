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
    font=("나눔고딕",size,"bold"), command=command)
    button.place(x=x,y=y)
def add_previous_button(text,command,x=90,y=480,size=12):
    button=tk.Button(root,text=text,
    font=("나눔고딕",size,"bold"),command=command)
    button.place(x=70,y=y)
def add_message(text,x=70,y=120,size=16):
    message=tk.Label(root,text=text,
    font=("나눔고딕",size,"bold"),justify="left")
    message.place(x=x,y=y)
#-----------------------------
# 컷 1: 아이들 관련 기본 안전 문구
#------------------------------ 
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
    add_next_button("탐사시작",show_entrance,x=750,y=500)
#----------------------- 
# 컷 2: 미래로 통하는 동굴
#----------------------
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
    add_previous_button("이전",show_child_safety,y=550)
    add_next_button("GO!",show_ready, x=800,y=550)
#-------------
# 컷 3 : 사전 준비물 확인
#-------------
def show_ready():
    clear_screen()
    add_title("사전 준비물 확인",x=70,size=30)
    computer=tk.Checkbutton(root,text="노트북이나 컴퓨터 준비됐나요?",
    font=("나눔고딕",18,"bold"))
    computer.place(x=70,y=140)
    internet=tk.Checkbutton(root,text="인터넷에 연결할 수 있는 'Chrome' 같은 프로그램이 준비되어 있나요?",
    font=("나눔고딕",18,"bold"))
    internet.place(x=70,y=220)
    chatgpt=tk.Checkbutton(root,text="휴대폰에서 'ChatGPT' 같은 'AI'와 직접 이야기할 준비 되어있나요?",
    font=("나눔고딕", 18,"bold"))
    chatgpt.place(x=70,y=300)
    add_message("앞으로 컴퓨터로 직접 작업하는 화면이 나오면,\n"
    "먼저, 그 안내 화면을 휴대폰으로 사진 찍어 두세요.\n"
    "그 사진을 옆에 놓고 하나씩 따라하면 훨씬 쉽지 않을까요?",size=18,x=70,y=390)
    add_previous_button("이전",show_entrance,x=70,y=520)
    add_next_button("OK! 함께 들어갈까요?", show_tool_room,y=520)

#----------------
# 컷 4: 도구방
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
    title.place(x=70,y=20)
    add_next_button("필요한 도구들을 찾아볼까요?",show_browser,y=540)
    add_previous_button("이전",show_ready,y=540)
#-------------------
# 컷 5 : 인터넷 연결 확인
#-------------------
def show_browser():
    clear_screen()
    add_title("'인터넷 연결' 확인 하세요.",x=90,size=28)
    text=("이 동굴은 인터넷에 연결해야 우리와 대화할 수 있어요.\n\n"
    "어떤 도구가 제일 먼저 필요할까요?\n\n"
    "바로 '브라우저'입니다.\n\n"
    "아까 동굴 앞에서 'Chrome'이 컴퓨터에 설치되어 있는 것 확인했었죠?\n"
    "그 'Chrome'이 바로 다양한 '브라우저' 중의 하나입니다.\n\n"
    "여기서도 잘 연결되나 한번 짧게 두번 '더블클릭'으로 실행해 볼까요?")
    message = tk.Label(root,text=text,
    font=("나눔고딕",18,"bold"), justify="left")
    message.place(x=90,y=140)
    add_next_button("엄마와 함께 실행 확인했어요.",show_ai,x=550)
    add_previous_button("이전",show_tool_room,x=90)
#--------------------
# 컷 6 : AI와 이야기하기
#--------------------
def show_ai():
    clear_screen()
    add_title("'AI'와 이야기하기",x=100,size=27)
    text=("'AI'에게 궁금한 것을 물어보려면 어떻게 해야 할까요?\n\n"
    "휴대폰에서 'ChatGPT'를 누르고 아래 'ChatGPT...'곳에,\n"
    "선생님에게 물어보듯이 편안하게 쓰기만 하면 됩니다.\n\n"
    "컴퓨팅 작업이 잘 안될 경우에도 일단 멈추고,\n"
    "컴퓨터 창 화면 사진찍어 질문 앞 (+)를 눌러,\n"
    "보낼 사진들을 선정하면 그 사진들이 질문창에 뜹니다. .\n\n"
    "그다음 사진 밑에 잘 안되는 상황을 함께 쓰고 보내면,\n"
    "'AI'는 왜 그런지 자세히 알려줄겁니다.\n\n"
    "그런데, 'AI'도 가끔은 실수할 수도 있으니,\n"
    "다시 한번 확인하는 습관을 들이는게 좋아요.")
    message=tk.Label(root,text=text,
    font=("나눔고딕",16,"bold"), justify="left")
    message.place(x=100,y=110)
    finish=tk.Button(root,
    text="브라우저와 AI 연결 다 확인했어요.",
    font=("나눔고딕",12),
    command=show_two_tools)
    finish.place(x=550,y=520)
    add_previous_button("이전",show_browser,x=100,y=520)
#-------------------------
# 컷 7 : 새로운 두가지 도구
#-------------------------
def show_two_tools():
    clear_screen()
    add_title("새로운 두가지 도구",x=90,size=28)
    text=("동굴과 소통하기 위한 도구들을 준비해 볼까요?\n\n"
    "하나는 코드를 쓰고 고치는 작업실인 'VS Code'입니다.\n\n"
    "다른 하나는 우리가 쓴 코드를 읽고,\n"
    "실제로 움직이게 해주는 'Python'입니다.\n\n"
    "'Python'은 누구나 사용할 수 있는 '오픈소스' 도구입니다.\n\n"
    "궁금한 것은 휴대폰 'AI'에게 물어보세요.")
    add_message(text,x=90,y=140,size=18)
    add_next_button("'Python'부터 만나볼까요?",show_python_download,x=550)
    add_previous_button("이전",show_ai,x=90)
#----------------------------
# 컷 8: Python 다운로드
#----------------------------
def show_python_download():
    clear_screen()
    add_title("먼저 'Python'부터 설치할까요?",size=25,x=90)
    text=("1.  'Chrome' 검색 창에 'Python'을 쓰고 'Enter'를 누르세요.\n"
    "2.  'Python org'를 누른 뒤 '공식적 프로그램'인 'Python.org'을 클릭하세요.\n\n"
    "3.  'Python 설치 창'이 뜨면 '다운로드'에 '커서'를  놓고 보이는 창에서,\n"
    "    '파이썬소스' 중 가장 위에 보이는 '파이썬 3 버전'이라는 곳을 클릭하세요.\n\n"
    "4.  자동으로 '다운로드'되니 조금 기다리면,\n"
    "    위에 '다운로드'가 '완료' 되었다는 작은 창이 열립니다.\n\n"
    "5.  그 곳에 '커서' 놓고 옆에 보이는 '파일 모양'을 '클릭'하면,\n"
    "    '파일 검색창'이 열리고 파란색으로 지금 설치하려는 파일이 보이게 됩니다.\n\n"
    "6.  그 곳에 '커서'를 놓고 연속으로 빨리 두번 '더블 클릭'하세요.\n"
    "    그러면, 'Python을 설치하겠냐고 묻는 창'이 나오고,\n"
    "    밑에 보이는 'Python 설치'라는 곳을 '클릭'합니다.\n\n"
    "7.  조금 기다리면, 검은 색의 'Python' 창이 열리는데,\n"
    "    아무 것도 누르지 말고 그냥 'Enter'를 누르세요.\n\n"
    "8. '기본선택'은 이미 자동으로 '설치' 되고 있으니 다시 'Enter'를 클릭하세요.\n"
    "    그다음 오른 쪽 위의 'X'를 눌러 이 'Python' 창을 닫으면 설치 완료된 겁니다.")
    add_message(text,size=13,x=90,y=90)
    add_next_button("'Python' 설치 확인했어요.",show_vscode_download_1,x=650,y=530)
    add_previous_button("이전",show_two_tools,x=90,y=530)
#------------------------------
# 컷 9: VS Code 다운로드 1.
#------------------------------
def show_vscode_download_1():
    clear_screen()
    add_title("같은 방식으로 'VS Code'를  설치할까요?",size=25,x=90)
    text=("처음이라 'Python'설치하느라 많이 힘드셨죠?\n"
    "이 동굴을 다 통과해 보면 아마 좋은 좋은 추억거리가 될겁니다.\n\n"
    "이제 앞으로 가장 많이 사용하게될 'VS Code'를\n"
    "'Python'보다는 약간 길지만 거의 비슷한 방식으로\n"
    "안내할테니 그대로 쫒아오면 아마 쉽게 설치될 겁니다.\n\n"
    "1.   먼저, 이전처럼 'Chrome 검색'에 'VS Code'를 쓰고 'Enter'를 누르세요.\n"
    "     맨 위의 공식 프로그램인 'Visual Studio Code'를 클릭합니다.\n\n"
    "2.   그러면 '다운로드'창이 보이는데, '윈도우 로고' 아래\n"
    "     파란색 '윈도우 10,11'을 클릭하면 '다운로드'가 진행되는 창이 보일 겁니다.\n\n"
    "     자동으로 '다운로드'가 진행되고 있으니,\n"
    "     절대로 오른 쪽 위의 파란색 '다운로드 버튼'은 누르지 마세요.\n\n"
    "3.   잠시 기다린 후, 오른쪽 위의 '다운로드'에 '커서'를 놓고 확인하신 다음,\n"
    "     앞의 'Python'처럼 '파일 모양'을 클릭하면, '파일 검색창'에 '파란색'으로 보일겁니다.")
    add_message(text,size=13,x=90, y=110)
    add_next_button("힘들지만 재미있어요.",show_vscode_download_2,x=650,y=500)
    add_previous_button("이전",show_python_download,x=90,y=500)
#---------------------------------------------------------------------
# 컷 10: VS Cdde 다운로드 2.
#----------------------------------------------------------------------
def show_vscode_download_2():
    clear_screen()
    add_title("힘들겠지만 조금만 더 힘내세요.",size=25,x=90)
    text=("4.   이 '파란색 파일'에 '커서'를 놓고 빠르게 두 번 '더블 클릭'하시면,\n"
    "     '라이선스 계약서' 창이 뜨는데 아래 쪽의 '동의합니다'와 '다음'을 클릭하세요.\n\n"
    "5.   다음 창이 뜨면 그냥 그대로 두고 아래에 있는 '다음'을 클릭하시면,\n"
    "     '시작 메뉴 폴더 선택'이라는 창이 뜨는데 또 밑에 있는 '다음'을 클릭하세요.\n\n"
    "6.   그러면, '추가 작업 선택'이라는 창이 뜹니다.\n"
    "     이 창 역시 아무 것도 건드리지 말고 오른쪽 아래 '다음'을 클릭합니다.\n\n"
    "7.   '설치 준비 완료' 창이 뜰겁니다. 밑에 있는 '설치'를 클릭하세요.\n"
    "     'VS Code'의 상징 심볼과 함께 '설치 마법사 완료'라는 창이 보일겁니다.\n\n"
    "8.   오른쪽 아래에 있는 '종료'를 클릭하면, 'VS Code'가 자동으로 열릴겁니다.\n"
    "     드디어, 'VS Code' 설치가 완료된 겁니다. 오른 쪽 위의 'X'를 눌러 종료하세요\n\n"
    "혹시라도, 설치가 잘 안될 경우 일단 멈추고, 휴대폰으로 'ChatGPT'에게 이상한 부분을\n"
    "사진찍어서 질문 옆의 (+)를 눌러 사진 보내면서 왜 그런지 질문해 보세요?") 
    add_message(text,y=110,size=13,x=90)
    add_next_button("'VS Code' 설치도 끝냈어요.",show_workspace,x=650,y=510)
    add_previous_button("이전",show_vscode_download_1,x=90,y=510)
#-------------------------------
# 컷 11: 우리의 작업실
#-------------------------------
def show_workspace():
    clear_screen()
    add_title("'코드 작업실' 입니다.",x=100,size=28)
    text=("'VS Code'창을 찬찬히 살펴볼까요?\n\n"
    "위쪽 넓은 곳은 코드를 쓰고 고치는\n"
    "작업 공간입니다.\n\n"
    "'터미널'이라고 하는 아래쪽 공간은,\n"
    "우리가 만든 코드를 직접 실행하고\n"
    "그 결과를 다시 확인하는 곳입니다.\n\n"
    "다시말해서, 위에서는 코드를 만들고,\n"
    "아래에서는 만든 코드를 실행하는 겁니다.")
    add_message(text,x=100,y=130,size=18)
    add_next_button("작업실 구조를 확인했어요.",show_run_method,x=570)
    add_previous_button("이전",show_vscode_download_2,x=100)  
#--------------------------------
# 컷 11: 저장하고 실행하기
#--------------------------------
def show_run_method():
    clear_screen()
    add_title("저장하고 실행하기",size=28,x=70)
    text=("코드를 입력한 후 반드시 저장부터 해야겠죠?\n"
    "왼쪽 아래 'Ctrl' 키를 찾아 'S'와 함께 누르면 '저장'이 됩니다.\n\n"
    "그다음 아래 터미널에 커서를 놓고\n"
    "'python 파일이름.py'를 쓰고 'Enter'로 실행하면 됩니다.\n\n"
    "새로운 파일을 만들어 그 파일이름으로\n"
    "내 파일에서 만든 이 코드를,\n"
    "실행해 달라고 부탁하는 거예요.\n\n")
    add_message(text,x=70,y=130,size=18)
    add_next_button("이제 직접 해볼까요?",show_nickname,x=570)
    add_previous_button("이전",show_workspace,x=70)
#----------------------------------
# 컷 12: 닉네임 만들기
#----------------------------------
def show_nickname():
    clear_screen()
    add_title("이름 만들기",x=80,size=28)
    text=("우리를 부를 때 이름이 필요하겠죠?\n\n"
    "'미래로 통하는 동굴'에서 사용될,\n"
    "의미있는 닉네임을 하나 생각해 보세요.\n\n"
    "엄마도 하나 만들어 보세요.\n"
    "왜 그렇게 정했는지 서로 한번 이야기해 보세요.\n\n"
    "탐사 중 그 의미를 잊지마세요.")
    add_message(text,x=80,y=140,size=18)
    add_next_button("우리 이름 정했어요.",show_first_file,x=570)
    add_previous_button("이전",show_run_method,x=80)
#------------------------------------
# 컷 13: 새 파일 만들기
#------------------------------------
def show_first_file():
    clear_screen()
    add_title("동굴과의 첫 소통 준비하세요?",x=70,size=25)
    text=("이제 'Windows 검색'에 입력해서,\n"
    "우리가 설치한 'VS Code'를 불러 볼까요?\n\n"
    "'VS Code'창이 열리면 왼쪽 위에 'File'을 찾아 클릭하세요.\n"
    "그 곳에서 'New File'을 클릭하면 '파란색'작은 창이 열립니다,\n\n"
    "맨 위의 빈칸에 커서를 놓고 'hello_cave.py'라고 입력하고,\n"
    "'Enter'한 후 나온 파일 창 아래의 'Create File'를 누르세요.\n\n"
    "그러면, 'VS Code' 창이 다시 열리면서,\n"
    "왼쪽 'Explorer'에 'hello_cave.py'가 보이게 됩니다.\n\n"
    "우리가 방금 새롭게 만든 첫 파일의 이름입니다.\n"
    "이 파일로 동굴과 소통이 되는가를 직접 시험해 볼겁니다.")
    add_message(text,size=15,y=120)
    add_previous_button("이전",show_nickname,x=70,y=520)
    add_next_button("직접 해 볼게요.", show_first_code,y=540)
#--------------------------------------------
# 컷 14: 첫 코딩
#--------------------------------------------
def show_first_code():
    clear_screen()
    add_title("동굴과의 첫 소통 코딩해 볼까요?",x=70)
    text=("왼쪽 'Explorer'에서 'hello_cave.py'를 클릭하고\n"
    "이 파일을 불러서 'VS Code'로 코딩 작업을 하려는 겁니다.\n\n"
    "위쪽 작업공간에 아래처럼 코드를 입력해 보세요.\n\n"
    'name = input("당신의 닉네임은?")\n'
    'print("안녕,",name)\n'
    'print("미래로 통하는 동굴에 온 것을 환영해!")\n\n'
    "점하나 틀려도 연결 안될 수 있으니 꼭 검토하세요.\n\n"
    "확인됐으면 'Ctrl'과 'S'를 함께 눌러 꼭 저장하세요.")
    add_message(text,y=130,size=18)
    add_next_button("코드 입력하고 저장했어요.",show_first_run,x=600,y=520)
    add_previous_button("이전",show_first_file,x=70,y=520)
#--------------------------------------
# 컷 15: 첫 실행
#--------------------------------------
def show_first_run():
    clear_screen()
    add_title("첫 실행",x=80,size=27)
    text=("아래 '터미널'에서 흰색으로 반짝거리는 곳에,\n"
    "커서를 놓고 'python hello_cave.py'라고 쓴 다음,\n"
    "'Enter'를 눌러 처음으로 직접 실행해 보세요.\n\n"
    "당신이 누구냐고 물어 보나요?\n"
    "당신의 닉네임을 입력해 보세요.\n\n"
    "와우!\n"
    "환영한다고 하나요?\n\n"
    "당신이 만든 코드로 동굴과 첫 소통에 성공했습니다.")
    add_message(text,y=140,size=18)
    add_next_button("첫 소통 성공!",show_mom_code,x=570,y=530)
    add_previous_button("이전",show_first_code,x=80,y=530)
#----------------------------------------
# 컷 16: 엄마도 함께
#----------------------------------------
def show_mom_code():
    clear_screen()
    add_title("엄마도 함께",x=80,size=28)
    text=("이번에는 코드에 엄마의 이름도 넣어볼까요?\n"
    "앞에했던 코딩에 추가 합니다.\n\n"
    'mom=input("함께하는 엄마의 닉네임은?")\n'
    'print(mom,"정말 반갑습니다.")\n'
    'print("우리의 첫 번째 연결 시작 되었어요!")\n\n'
    "검토 후 'Ctrl+S'로 저장, 아래 '터미널'에서,\n"
    "'python hello_cave.py'를 쓰고 'Enter'로 실행합니다.\n\n"
    "엄마도 동굴과 인사했나요?")
    add_message(text,x=80,y=130,size=18)
    add_next_button("둘 다 소통됐어요!",show_finish_today,x=580,y=530)
    add_previous_button("이전",show_first_run,x=80,y=530)
#----------------------------------------
# 컷 17: 오늘은 여기까지
#----------------------------------------
def show_finish_today():
    clear_screen()
    add_title("오늘은 여기까지",x=80,size=28)
    text=("동굴이 준비하느라 수고 많았다고 합니다.\n\n"
    "오늘은 첫 인사한 것으로 충분하니,\n"
    "탐사는 여기까지이고 즐거웠다고 하네요.\n\n"
    "우리도 동굴이 쉬도록 마지막에\n"
    "'종료'라 입력한 후 'Enter'를 누르면 됩니다.\n\n"
    "그러면 '실행'으로 다시 부를 때까지\n"
    "우리 모두 편안히 휴식합시다.")
    add_message(text,x=80, y=120,size=18)
    add_next_button("'준비단계' 일정 끝났네요.",show_review,x=570)
    add_previous_button("이전",show_mom_code,x=80)
#------------------------------------------
# 컷 18: 엄마와 함께 되돌아 보기
#------------------------------------------
def show_review():
    clear_screen()
    add_title("'준비 단계'에서 어떤 경험들을 했죠?",x=70,size=27)
    text=("'도구방'에서 필요한 도구들을 찾아서,\n"
    "어떻게 설치했고 무슨 작업들을 했었죠?\n\n"
    "새로운 파일을 만들어 이름까지 지어 주었죠?\n\n"
    "'코드 작업'은 어디에서 어떻게 했었죠?\n\n"
    "그런데, 왜 동굴에게 '코드 작업'으로 미리,\n"
    "대화 내용들을 알려주었을까요?\n\n"
    "엄마와 함께 이야기 해보고,\n"
    "더 궁금한 것들 있으면 휴대폰 'AI'에게도 물어보세요.")
    add_message(text,y=130,size=17)
    add_next_button("많이 생각해 볼게요.",show_last,x=550)
    add_previous_button("이전",show_finish_today,x=70)
#---------------------------------------------
# 컷 19: 진짜 탐사의 시작
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

show_child_safety()
root.mainloop()
