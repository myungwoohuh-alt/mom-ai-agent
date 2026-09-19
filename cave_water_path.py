import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
root.title("물길 탐사")
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
    add_next_button("탐사시작",show_cover,x=700)
#--------------------------------
# 2: 겉 표지
#--------------------------------
def show_cover():
    clear_screen()
    image=Image.open("water_path_cave.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_next_button("Go!",show_review,x=800,y=530)
    add_previous_button("이전",show_child_safety,y=530)
#-------------------------------
# 3: 지나왔던 "준비단계" 돌아보기
#-------------------------------
def show_review():
    clear_screen()
    add_title("장착한 도구들 점검 해볼까요?",x=70,size=30)
    text=("배 고프지 않아요?\n\n"
    "'VS Code' 아래 '터미널'에 'python choice.py'를 실행합니다.\n\n "
    "'두갈래길'에서 만들었던 '밥 먹을까요?'를 반복해 보세요.\n\n" 
    "탐사 전에 배도 채웠으니 도구들 점검해 볼까요?\n\n"
    "자, 그럼 이제 동굴 안으로 더 깊이 들어가 봅시다.")
    add_message(text,y=140,size=20)
    add_previous_button("이전",show_cover)
    add_next_button("더 깊이 들어 갑시다.",show_deep_cave)
#--------------------------------
# 4: 더 깊은 동굴 안 탐사
#--------------------------------
def show_deep_cave():
    clear_screen()
    add_title("더 깊은 동굴 안 탐사",size=30,x=90)
    text=("와우! 여긴 길들이 꽤 복잡하네요.\n\n"
    "다른 동굴로 통하는 구멍들이 보이고\n"
    "오른 쪽 아래에는 쭉 이어지는 물길도 보이네요.\n\n"
    "작은 배 같은 것도 있는 것 같은데,\n"
    "배를 타고 물길을 따라가면,\n"
    "동굴을 쉽게 통과할 수 있지 않을까요?")
    add_message(text,x=90,y=140,size=20)
    add_previous_button("이전",show_review,x=90)
    add_next_button("동굴 안 복잡한 길들",show_three_way)
#-------------------------------
# 5: 동굴 안 복잡한 길 이미지
#-------------------------------
def show_three_way():
    clear_screen()
    image=Image.open("three_path_cave.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_deep_cave,y=550)
    add_next_button("어느 길로 갈까요?",show_path_choice,x=700,y=550)
#-------------------------------
# 6: 어느 길로 갈까요?
# ------------------------------
def show_path_choice():
    clear_screen()
    add_title("하나의 길만을 선택해야 합니다.",size=30,x=90)
    text=("우리가 왔던 길로 쭉 갈까요?\n\n"
    "왼쪽 동굴로 들어가볼까요?\n\n"
    "아니면 작은 동굴로 갈까요?\n\n"
    "아래에 보이는 물길따라서\n"
    "배를 타고 가는 '물길탐사'를 하면,\n"
    "더 신비롭고 재미있지 않을까요?")
    add_message(text,size=20,x=90,y=130)
    add_previous_button("이전",show_three_way,x=90)
    add_next_button("결정했어요!",show_elif_meaning)
#--------------------------------------
# 7: 추가하는 elif 코드의 의미  
#--------------------------------------
def show_elif_meaning():
    clear_screen()
    add_title("여러 조건 중 하나 선택하는 새 코드의 의미",size=28)
    text=("지난 '두갈래길'에서는 'if'와 'else'를 사용했었죠?\n\n"
    "이번에는 선택할 길들이 많으니, \n" 
    "'elif'라는 새로운 코드를 하나 더 추가합니다.\n\n"
    "즉, 'if'와 'elif'와 'else' 세가지로 \n"
    "여러가지 조건들이 있을 경우,\n"
    "하나를 선택할 수 있도록 코딩하는 겁니다.\n\n"
    "코딩에 있어서 매우 중요하니,\n" 
    "암기보다는 그 구조의 의미를 깊이 새겨 두세요.")
    add_message(text,size=19)
    add_previous_button("이전",show_path_choice)
    add_next_button("구조의 의미를 이해했습니다!",show_elif_coding,x=600)
#-------------------------------------
# 8: if / elif / else 직접 코딩
#-------------------------------------
def show_elif_coding():
    clear_screen()
    add_title("여러 조건 중 하나 선택하는 코드 입력",size=28)
    text=("먼저, 'water.py'라는 새파일을 'Explore'에서\n"
    "쉽게 만든 다음, 'water.py'를 열고 위의 작업창에 입력하세요.\n\n"
    '     cave=input("이번엔 다른 동굴 길로 갈까요?y/n:")\n'
    '     if cave=="y":\n'
    '         print("여러 동굴 길을 살펴봅니다.")\n\n'
    "'들여쓰기' 확인하고 저장한 뒤 터미널에서 실행해 보세요.\n"
    "그런데, 여기에 'elif'를 추가한다면 어떻게 될까요?\n\n"
    '     elif cave=="n":\n'
    '         print("다른 길을 찾아 봅시다.")\n'
    '     cave=input("배타고 물길 탐사해 보는 것은 어떨까요?y/n:")\n'
    '     if cave=="y":\n'
    '         print("배타고 물길 탐사 시작합시다.")\n\n'
    "'들여쓰기'와 아래 '오류 표시 확인'까지 꼭 검토하고 저장하세요.")
    add_message(text,size=16,y=100)
    add_previous_button("이전",show_elif_meaning,y=540)
    add_next_button("저장까지 완료했습니다.",show_run,y=540)
#---------------------------------------
# 9: 코딩 후 직접 실행
#---------------------------------------
def show_run():
    clear_screen()
    add_title("이제 직접 '실행'해 볼까요?",size=28)
    text=("'VS Code' 아래쪽 '터미널'에서,\n"
    "'python water.py'를 입력하고 'Enter'로 실행합니다.\n\n"
    "앞에서 두가지 중 하나를 선택했을 때와,\n"
    "'elif'가 추가 된 다음에는 무엇이 달라졌을까요?\n\n"
    "'if'는 첫 번째 조건이고,\n"
    "'elif'는 또 다른 조건을 확인합니다.\n\n"
    "'else'는 다른 조건들 찾을 필요 없을 때 사용합니다.\n\n"
    "코딩은 이렇게 우리가 생각하는 구조를 표현합니다.")
    add_message(text,size=19,y=100)
    add_previous_button("이전",show_elif_coding)
    add_next_button("배타러 물가로 갑시다.",show_boat)
#------------------------------------------
# 10: 물가에서 배에 승선
#------------------------------------------
def show_boat():
    clear_screen()
    add_title("배 점검하고 물길 탐사 준비하세요.",size=28)
    text=("겉은 조금 낡았지만 그래도 튼튼해 보이네요.\n\n"
    "쉬잇! 조용! 동굴이 뭐라고 속삭입니다.\n\n"
    "이 배에서 너희와 나를 새로운 도구로 연결해 줄래?\n"
    "그러면, 나도 정해진 말만하던 규칙에서 벗어나서,\n\n"
    "다양하게 더 많은 이야기로 소통할 수 있어.\n"
    "'물길탐사'에도 많은 도움 될거야.\n\n"
    "미래에 너희가 어디에 있던 나와 함께 연결되는\n"
    "아주 중요하고 유용한 도구니까 잘 보관해 달라네요.")
    add_message(text,size=19,y=130)
    add_previous_button("이전",show_run,y=520)
    add_next_button("새로운 연결은 어떤 의미죠?",show_meaning,y=520)
#--------------------------------------------
# 11: 새로운 도구 연결의 의미
#--------------------------------------------
def show_meaning():
    clear_screen()
    add_title("새로운 도구 연결은 어떤 의미 일까요?",size=27)
    text=("지금까지는 우리가 코드로 미리 만든\n"
    "내용으로만 동굴과 소통할 수 있었죠?\n\n"
    "동굴에게 새로운 연결 통로를 만들어주면,\n"
    "외부의 'AI'들 세계와도 자유롭게 함께할 수 있습니다.\n\n"
    "간략하게 이야기하면,\n"
    "    사람들 질문---> Python 프로그램(연결 역할)--->\n"
    "    OpenAI 라이브러리(통역겸 연결 어댑터 역할)--->\n"
    "    인터넷/API(통로 역할/API Key로 누구인지 확인하는 역할)--->\n"
    "    LLM(답변 만드는 역할)--->Python 프로그램(연결 역할)--->사람에게 답변.\n\n"
    "이처럼 눈에 안보이게 일어나는 연결 구조는 복잡한 것 같아도,\n\n"
    "    사람> Python> OpenAI> API Key> LLM> Python> 사람,\n\n"
    "이렇게 각각의 역할로 연결되어 있다는 것은 꼭 기억해 두세요")
    add_message(text,size=16,y=100)
    add_previous_button("이전",show_boat,y=540)
    add_next_button("연결구조 꼭 기억할게요!",show_llm_1,x=630,y=540)
#-------------------------------------------------
# 12:새로운 도구 'LLM' 연결 1,
#-----------------------------------------------
def show_llm_1():
    clear_screen()
    add_title("역할에 따른 연결 구조로 직접 설치해 볼까요?",size=25)
    text=("1.   'VS Code'의 'Explorer'에서 새파일 'app.py'을 만드세요.\n\n"
    "2.   'VS Code' 아래 '터미널'에 'pip install openai'라 쓰고 'Enter'하세요.\n\n"
    "     길게 설치되면서 '----successfully----'단어가 나오거나,\n"
    "     설치 다  끝나고 원래 '터미널' 창이 나오면 설치 완료된 겁니다.\n"
    "     '터미널'이 복잡하면 'CLS'라고 쓰고 'Enter'하면 깨끗해 집니다.\n\n"
    "     (여기까지가 연결을 위한 'Python' 프로그램 준비 작업입니다.\n"
    "      'VS Code'는 오른쪽 위 (-)를 누르고 필요할 때 맨 아래에서 클릭하면 됩니다.)\n\n"
    "3.   'Chrome' 검색으로 'OpenAI API Platform'을 클릭하면 'home page' 창이 열립니다.\n\n"
    "     '계정이 필요한데, 만약 'ChatGPT'에 'Google 계정'을 사용하고 있다면,\n"
    "     밑에 있는 'continue with Google'을 클릭하세요.\n\n"
    "     (지금은 'OpenAI 라이브러리'까지 연결했습니다.\n" 
    "      다음은 비밀번호처럼 안전하게 보관할 중요한 'API Key' 설치로 갑니다.)\n\n")
    add_message(text,size=14,y=120)
    add_previous_button("이전",show_meaning,y=540)
    add_next_button("'API Key' 설치합시다.",show_llm_2,y=540)
#------------------------------------------------
# 13: 새로운 도구 LLM 연결 2.
#---------------------------------------------
def show_llm_2():
    clear_screen()
    add_title("가장 중요한 'API Key'와 '결제' 연결합니다.",size=25)
    text=("4.   'API Key' 창에서 '새 비밀 키를 생성합니다./create new key'를 클릭하세요.\n"
    "     그러면, 작은 창에 여러가지 항목들을 물어 보는 것이 나오는데,\n"
    "     지금은 '실습차원'이라 그대로 두고, 단지 이름을 묻는\n"
    "     'name'에만 그냥 '물길탐사-연결연습'이라고 입력하고,\n"
    "     아래에 있는 'Create Secret Key'를 클릭하세요.\n\n"
    "5.   'Key'가 생성되었으면, 옆의 '복사/Copy' 버튼을 꼭 클릭하시고 그대로 두세요.\n"
    "          [혹시 잘몰라서 'ChatGPT'에게 사진으로 물어볼 때도,\n"
    "           'Key'가 보이는 사진은 절대로 보내면 안됩니다.]\n"
    "      마치 은행의 비밀번호처럼 누구에게도 가르쳐주면 안됩니다.\n\n "
    "6.   지금부터는 이 키를 가능한 안전하게 '복사'해서 보관할 겁니다.\n"
    "      지금 상태에서 밑에있는 'VS Code' 모양을 클릭하면 창이 뜨는데,\n"
    "      왼쪽 'Explorer'의 'New File'에서 '.env'라고만 쓰고 새파일을 만드세요.\n\n"
    "7.   새파일 '.env'가 보이면 클릭하고, 첫 번째 줄에 'OPEN_API_KEY='라고\n"
    "      '대문자' 똑같이 쓴 다음, (=) 바로 뒤에 커서를 놓고 'Ctrl + V'를 함께 누르면,\n"
    "      조금 전에 생성된 'Key'가 '복사'되어 붙여지게 됩니다.\n\n"
    "8.   그러면, '.env' 새파일 안에 안전하게 보관된 것이니,\n"
    "      'Crtl + S'로 저장하고 위에 있는 탭에 커서를 놓고 (X)로 파일을 닫습니다.\n\n.")
    add_message(text,size=14,y=80)
    add_previous_button("이전",show_llm_1,y=550)
    add_next_button("'결제' 방식 연결합시다.",show_verify,y=550)
#--------------------------------------------
# 14: 새로운 도구 연결시 확인 사항
#--------------------------------------------
def show_verify():
    clear_screen()
    add_title("'결제' 방식 연결할 때 꼭 확인하세요!",size=25)
    text=("     (조금 힘이 들었겠지만 지금까지 'OPenAI에서 권장하는 방식으로,\n" 
    "      'Key'를 생성해 가능한 안전하게 보관까지 끝낸 겁니다.\n"
    "      다음 '결제' 방식 연결은 '엄마'의 '동의'와 '협조'가 반드시 필요합니다.)\n\n"
    "9.    'key' 생성과 관련된 작은 창은 밖에 아무 곳이나 놓고 클릭해 닫은 후,\n"
    "      왼쪽 맨 위의 화살표를 눌러 처음 'home page'창으로 갑니다.\n\n"
    "      그 창에서 'go to billing' 또는 '결제/billing/credit'을 클릭하세요.\n"
    "      그러면, 'Billing/결제'라는 제목의 창이 열릴 겁니다.\n\n"
    "10.   검은색으로 된 'add payment details' 버튼을 누르면,\n"
    "       카드번호, 카드종류, 만료날짜, 보안코드(cvc/cvv)가 나옵니다.\n"
    "       '보안코드'는 대부분 신용카드 뒷면 '3 자리'를 적으면 됩니다.\n\n"
    "       제대로 다 기입했으면, 아래에 있는 'continue'를 누르세요.\n"
    "       'configure payment'라는 창이 열리는데, 처음엔 '최소금액'을 쓰고,\n"
    "       'use auto-reload/자동충전' 옆의 버튼을 눌러 일단 'off/끔'을 클릭합니다.\n\n"
    "       그리고 밑에 'continue'를 클릭하면 '최종 확인하는 작은 창'이 열립니다.\n"
    "       '최소금액'부분과 회색으로 '자동충전' 부분이 꺼져있는 것 재확인 한 후,\n"
    "       밑에있는 'continue'를 누르고 창을 닫으면 'LLM' 연결 끝난 겁니다.\n\n")
    add_message(text,size=14,y=90)
    add_previous_button("이전",show_llm_2,y=550)
    add_next_button("'LLM' 연결 끝냈습니다!",show_llm_3,y=550)
#--------------------------------------------
# 15: 새로운 도구 LLM
#--------------------------------------------
def show_llm_3():
    clear_screen()
    add_title("매우 유용한 도구 연결했습니다.",size=27)
    text=("연결하는데 복잡하고 조금 힘이 들었지만\n"
    "지금 연결된 새로운 도구를 'LLM' 이라고 합니다.\n\n"
    "'LLM'은 지금까지 글자로 기록된\n"
    "방대한 자료와 정보들을 알고 있어요.\n\n"
    "그래서, 질문하면 가능한 정확한\n"
    "대답을 해주려고 노력하고 있죠.\n\n"
    "간혹 실수가 있을 수도 있습니다.\n"
    "그래도, 이렇게 유용한 도구는 인류에게 처음있는 일입니다.\n\n"
    "물길 탐사 중에 동굴과 소통하며 직접 경험해 보세요.")
    add_message(text,y=100,size=16)
    add_previous_button("이전",show_verify)
    add_next_button("직접 경험해 볼게요.", show_llm_4)
#---------------------------------------------
# 16: LLM의 효율적 사용 방법
#---------------------------------------------
def show_llm_4():
    clear_screen()
    add_title("'LLM'을 더 효율적으로 사용하는 방법은?",size=28)
    text=("'LLM'은 자동차처럼 연료비가 들어갑니다.\n"
    "그래서, 효율적으로 사용하는 습관을 들이는게 좋아요?\n\n"
    "탐사 중 중요하다고 말한 구조를 잘 활용할수록\n"
    "더 효율적으로 미래를 펼쳐 나갈 수 있습니다.\n\n"
    "미래에는 코딩이 어떠한 구조를 표현하는지\n"
    "판별하는 능력이 더 중요하지 않을까요?\n\n"
    "구조를 통해서 그 의미를 파악하는 방향으로\n"
    "탐색해 보는 좋은 습관을 만들어 보세요.")
    add_message(text,y=120)
    add_previous_button("이전",show_llm_3)
    add_next_button("구조부터 먼저 보는 습관 만들게요.",show_llm_talk,x=580)
#-----------------------------------------------
# 17: LLM 사용 경험담
#-----------------------------------------------
def show_llm_talk():
    clear_screen()
    add_title("'LLM'과 소통하며 많은 이야기 했어요.",size=28)
    text=("조금 전에 동굴에게 물어 봤어요.\n\n"
    "이 물 속에도 물고기 들이 많이 있어?\n"
    "그랬더니, 동굴이 이렇게 이야기 하네요.\n\n"
    "여기에는 물고기뿐만 아니라\n"
    "수많은 생명체들이 함께 살고 있답니다.\n\n"
    "그래서 이 들을 품고 보듬으며 함께 있어서\n"
    "자기는 참 보람있고 행복하다네요.\n\n"
    "'LLM' 연결하니 이전과는 완전히 다르게 이야기하죠?")
    add_message(text,size=19,y=100)
    add_previous_button("이전",show_llm_4)
    add_next_button("우리도 행복한 기분들어요.",show_imagination)
#----------------------------------------------
# 18: 우리의 미래를 상상하며 
#----------------------------------------------
def show_imagination():
    clear_screen()
    add_title("미래에 무엇을 해보고 싶어요?",size=28)
    text=("'LLM'은 '언어기반'이라 엄마처럼\n"
    "함께하며 받쳐주고 있을거예요.\n"
    "이렇게 소통하는 디지털 지능을 'AI'라고 합니다.\n\n"
    "더 나아가 우리가 하는 일들을 \n"
    "도와주는 'AI'를 'AI Agent'라고 합니다.\n\n"
    "미래를 함께 펼쳐나갈 '동반자'로 생각해보면 어떨까요?\n"
    "'동반자'와 함께 펼쳐나갈 미래를 상상해 보세요.\n\n"
    "엄마도 미래의 삶을 마음 속에 그려보시지 않겠어요?")
    add_message(text,size=19)
    add_previous_button("이전",show_llm_talk)
    add_next_button("미래의 꿈을 상상해 봤습니다.",show_bright_path)
#--------------------------------------------------
# 19: 나가는 통로를 맞이하면서
#-------------------------------------------------
def show_bright_path():
    clear_screen()
    image=Image.open("boat_cave_explore.png")   
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_llm_2,y=530)

show_child_safety()
root.mainloop() 