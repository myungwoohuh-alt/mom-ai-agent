import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
root.title("물길 탐사")
root.geometry("900x600")
#--------------------------------
# 공통기능
#--------------------------------
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
    "'VS Code'아래 '터미널'에 'python choice.py'를 실행합니다.\n\n "
    "저번에 만들었던 '밥 먹을까요?'를 반복해 보세요.\n\n" 
    "도구들 점검하면서 배도 채워볼까요?\n\n"
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
    add_message(text,size=20,x=90)
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
    add_next_button("구조의 의미를 이해했습니다!",show_elif_coding)
#-------------------------------------
# 8: if / elif / else 직접 코딩
#-------------------------------------
def show_elif_coding():
    clear_screen()
    add_title("여러 조건 중 하나 선택하는 코드 입력")
    text=('cave=input("이번엔 다른 동굴 길로 갈까요?y/n:")\n\n'
    'if cave=="y":\n'
        'print("여러동굴 길을 살펴봅니다")\n\n'
    'elif cave=="n":\n'
        'print("다른 길을 찾아 봅시다.")\n\n'
    'else:\n'
        'print("어떤 길이 있을지 더 생각해 봅시다.)\n\n'
    'cave=input("배타고 물길 탐사해 보는 것은 어떨까요?y/n:")\n\n'
    'if cave=="y":\n'
        'print("배를타고 물길 탐사 시작합시다.")')
    add_message(text,y=90)
    add_previous_button("이전",show_elif_meaning,y=550)
    add_next_button("저장까지 완료했습니다.",show_run,y=550)
#---------------------------------------
# 9: 코딩 후 직접 실행
#---------------------------------------
def show_run():
    clear_screen()
    add_title("이제 직접 '실행'해 볼까요?",size=28)
    text=("VS Code 아래쪽 '터미널'에서,\n"
    "'python choice.py'를 입력하고 'Enter'로 실행합니다.\n\n"
    "'y'와 'n', 그리고 다른 답도 입력해 보면서\n"
    "달라지는 결과를 확인해 보세요.\n\n"
    "'if'는 첫 번째 조건이고\n"
    "'elif'는 '그 조건이 아니면 뭐가 있을까?'를 의미하죠.\n\n"
    "'else'는 위의 조건들 찾을 필요 없을 때 사용하죠.\n\n"
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
    add_message(text,size=19,y=100)
    add_previous_button("이전",show_run)
    add_next_button("새로운 연결은 어떤 의미죠?",show_meaning)
#--------------------------------------------
# 11: 새로운 도구 연결의 의미
#--------------------------------------------
def show_meaning():
    clear_screen()
    add_title("새로운 도구 연결은 어떤 의미 일까요?",size=28)
    text=("지금까지는 우리가 코드로 미리 만든,\n"
    "내용으로만 동굴과 소통할 수 있었죠?\n\n"
    "동굴에게 새로운 연결 통로를 만들어주면,\n"
    "외부의 'AI'들 세계와도 자유롭게 함께할 수 있습니다.\n\n"
    "실제로 연결하려면 휴대폰 'AI'에게 컴퓨터 화면 창을\n"
    "사진찍어 물어보면 한단계씩 자세히 안내해 줄겁니다.\n\n"
    "이제, 외부와의 새로운 연결을 위해 우리가 미리 만든\n"
    "'app.py'라는 '새 코드 파일'을 불러 볼게요.")
    add_message(text,size=19,y=100)
    add_previous_button("이전",show_boat)
    add_next_button("연결시 꼭 확인하세요!",show_verify)
#--------------------------------------------
# 12: 새로운 도구 연결시 확인 사항
#--------------------------------------------
def show_verify():
    clear_screen()
    add_title("새로운 도구 연결할 때 꼭 확인하세요!",size=28)
    text=("실제로 새로운 도구를 연결하려면,\n"
    "몇가지 준비와 확인할 것들이 있습니다.\n\n"
    "엄마의 협조가 필요하니 함께 휴대폰 'AI'에게\n"
    "컴퓨터 창의 화면을 사진찍어 보내며 한단계씩 진행하세요.\n\n"
    "그리고, 아래 사항도 꼭 확인하세요.\n\n"
    "[Key]는 비밀번호처럼 중요한 것이니 남에게 공개하지 않기.\n"
    "[비용]은 처음에는 '최소 연료비'만 넣어 시험하기.\n"
    "[자동충전]은 창에 '자동충전'이 열려있으면 처음엔 꺼 줄것을 추천합니다.\n\n")
    add_message(text,size=18,y=120)
    add_previous_button("이전",show_meaning)
    add_next_button("확인 끝났습니다.",show_llm_1)
#--------------------------------------------
# 13: 새로운 도구 LLM
#--------------------------------------------
def show_llm_1():
    clear_screen()
    add_title("매우 유용한 도구 연결했습니다.",size=28)
    text=("새로운 도구를 'LLM' 이라고 합니다.\n\n"
    "'LLM'은 지금까지 글자로 기록된\n"
    "방대한 자료와 정보들을 알고 있어요.\n\n"
    "그래서, 질문하면 가능한 정확한\n"
    "대답을 해주려고 노력하고 있죠.\n\n"
    "간혹 실수가 있을 수도 있습니다.\n"
    "그래도, 이렇게 유용한 도구는 인류에게 처음있는 일입니다.\n\n"
    "물길 탐사 중에 동굴과 소통하며 직접 경험해 보세요.")
    add_message(text,y=100,size=19)
    add_previous_button("이전",show_verify)
    add_next_button("직접 경험해 볼게요.", show_llm_2)
#---------------------------------------------
# 14: LLM의 효율적 사용 방법
#---------------------------------------------
def show_llm_2():
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
    add_previous_button("이전",show_llm_1)
    add_next_button("구조부터 먼저 보는 습관 만들게요.",show_bright_path,x=580)
#----------------------------------------------
# 15: 동굴 끝 밝은 빛이 보이는 이미지
#----------------------------------------------
def show_bright_path():
    clear_screen()
    image=Image.open("boat_cave_explore.png")   
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_llm_2,y=530)
    add_next_button("빛이 많이 들어 오네요!",show_llm_talk, x=700,y=530)
#-----------------------------------------------
# 16: LLM 사용 경험담
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
    add_previous_button("이전",show_bright_path)
    add_next_button("우리도 행복한 기분들어요.",show_imagination)
#----------------------------------------------
# 17: 우리의 미래를 상상하며 
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
    add_next_button("미래의 꿈을 상상해 봤습니다.",show_exit)
#--------------------------------------------------
# 18: 나가는 통로를 맞이하면서
#-------------------------------------------------
def show_exit():
    clear_screen()
    add_title("와우! 밖으로 나가는 통로가 보여요!",size=28)
    text=("이 번 탐사에서 어떤 경험들을 했고,\n"
    "코딩으로는 어떤 구조로 표현되었는지 떠 올려 보세요.\n\n"
    "탐사 경험과 미래의 꿈까지\n"
    "'trip.txt'에 잊지 않도록 꼭 기록하세요\n\n"
    "가능한 한줄로 요약해 보는 습관을 만드세요.\n"
    "새로운 미래 설계도 한줄 요약이\n"
    "될 때까지 다지고 다진다음 출발하세요.\n\n"
    "동굴도 함께해서 행복했고 밝은 미래를 응원한데요.")
    add_message(text,size=19,)
    add_previous_button("이전",show_imagination)
    add_next_button("밝은 미래로 나갑시다!",show_final)
#----------------------------------------------------
# 19: 밝은 미래로 향하는 이미지
#----------------------------------------------------
def show_final():
    clear_screen()
    root.geometry("900x600")
    image=Image.open("cave_exit_future.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    title=tk.Label(root,text="밝은 미래를 향해!",
    font=("나눔고딕",24,"bold"),
    bg="#f4e6bd")
    title.place(x=70,y=35)
    child=tk.Label(root,text='아이:"통과! 미래의 꿈을 펼쳐보자!"',
    font=("나눔고딕",14,"bold"),
    bg="#f4e6bd")
    child.place(x=560,y=500)
    mom=tk.Label(root,text='엄마:"우리 함께 미래로 나아가자!"',
    font=("나눔고딕",14,"bold"),
    bg="#f4e6bd")
    mom.place(x=560,y=550)
    add_previous_button("이전",show_exit,y=550)

show_child_safety()
root.mainloop() 