import tkinter as tk
from PIL import Image,ImageTk
root=tk.Tk()
root.title("밝은 미래로!")
root.geometry("900x600")
#----------------------
# 공통기능
#----------------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
def add_title(text,size=28,x=70,y=20):
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
    image=Image.open("cave_journey_cover.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_child_safety,y=530)
    add_next_button("Go!",show_look_back,x=750,y=530)
#--------------------------------
# 3: 첫걸음
#-------------------------------
def show_look_back():
    clear_screen()
    add_title("동굴 밖으로 나오니 무엇이 달라 졌나요?")
    add_message("'미래로 통하는 동굴' 탐사를 끝내니,\n" 
    "뭔가 많이 달라진 기분 안들어요?\n\n"
    "일단, 동굴 입구에 처음 들어갔을 때,\n"
    "생소했던 유용한 도구들을 이미 많이 갖고 있잖아요?\n\n"
    "또한, 지나왔던 동굴 길들과 물길의 구조들이,\n"
    "어느새 하나의 흐름으로 연결되어 그려지지 않나요?\n\n"
    "'AI Agent'가 정리해준 '탐사기록'과 함께,\n"
    "다시 한번 지나온 길들을 떠 올려 보면 어떨까요?")
    add_previous_button("이전",show_cover)
    add_next_button("회상해 볼까요?",show_first_tools) 
#---------------------------------
# 4: '준비단계' 회고
#--------------------------------
def show_first_tools():
    clear_screen()
    add_title("'도구방'에서 부터 많이 당황했었어요.")
    add_message("뭐가 뭔지도 잘 몰라서,\n"
    "처음으로 동굴의 도움을 많이 받았었죠.\n\n"
    "'Python'이 무엇인지도,\n"
    "'VS Code'가 무엇인지도,\n"
    "'새로운 파일'을 어떻게 만드는지도 몰랐었어요.\n\n"
    "하지만, 동굴의 도움과 휴대폰 'ChatGPT'에게 물어보면서,\n"
    "직접 '다운로드'해서 설치하고, 입력한 다음 저장하고,\n"
    "'터미널'에서 반복 실행하면서 많이 익숙해 졌었어요.",y=130)
    add_previous_button("이전",show_look_back)
    add_next_button("자신감이 생겼었어요.",show_if_agent_image)
#-------------------------------------------------------------------------
# 5. 구조 흐름 이미지 컷 ; if,else---if,elif,else---'LLM'---Ai Agent 이 순서로.
#-------------------------------------------------------------------------
def show_if_agent_image():
    clear_screen()
    image=Image.open("step5_if_llm_agent.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_first_tools,y=530)
    add_next_button("흐름의 구조가 잘 보여요",show_two_paths,x=630,y=530)
#--------------------------------
# 6: '두 갈래길' 회고
#---------------------------------
def show_two_paths():
    clear_screen()
    add_title("선택에 따라 달라지는 구조를 알게 됐어요.")
    add_message("'두갈래길'에서는 두가지 조건 중에서\n"
    "하나를 선택하는 조건에 따라 결과가\n"
    "달라질 수밖에 없습니다.\n\n"
    "'if'와 'else'라는 코드로 직접 코딩하면서,\n"
    "이런 방법으로 표현한다는 것을 알게 됐어요.\n\n"
    "코드는 단순히 외우는 것이 아니라,\n"
    "생각하고 있는 구조를 논리적으로\n"
    "코딩하는 방법이라고 느껴졌습니다.",size=20,y=140)
    add_previous_button("이전",show_first_tools,y=520)
    add_next_button("구조를 알기 시작했어요.",show_water_path,y=520)
#-------------------------------------
# 7: 물길탐사 회고
#-----------------------------------
def show_water_path():
    clear_screen()
    add_title("LLM'이라는 새도구를 마련했어요.")
    add_message("두가지 조건이 넘는 경우에 새로운 코드,\n"
    "'elif'를 사용하면 쉽게 표현할 수 있다는 것도 알았어요.\n\n"
    "또한, 무엇보다도 가장 인상 깊었던 경험은,\n"
    "동굴의 요청으로 'LLM'이라는 도구를 마련해 준 일입니다.\n\n"
    "프로그램에 따라 미리 정해놓은 답만 이야기하던 동굴에게\n"
    "자유롭고 다양한 대화를 할 수 있도록 만들어 주었기 때문입니다.\n\n"
    "동굴 밖의 더 넓은 'AI 세계'와 처음으로 연결된 순간이었죠.",y=130)
    add_previous_button("이전",show_two_paths)
    add_next_button("행복감을 함께 느꼈었어요.",show_agent_memory)
#-----------------------------------
# 8: 'Agent' 만들기 회고
#----------------------------------
def show_agent_memory():
    clear_screen()
    add_title("'AI'에게 우리가 할 일을 맡겨보았습니다.")
    add_message("먼저, 일을 할 수 있도록 새파일을 만들어 주었죠?\n\n"
    "이 파일이 우리 '탐사기록'을 읽고,\n"
    "'LLM'에게 분류와 정리 부탁한 결과를\n"
    "다시 각각 다른 파일에 저장하도록 코딩했었죠?\n\n"
    "아주 간단하고 작지만 'AI Agent'를,\n"
    "우리가 직접 만들어 그 결과까지 확인했었죠?\n\n"
    "단순하게 질문하고 답을 하는 단계를 넘어서,\n"
    "목표 정해주면 직접 일을 수행하며 도와주는 겁니다.",y=130)
    add_previous_button("이전",show_water_path)
    add_next_button("일하는게 매우 쉬워졌어요.",show_python_agent_image)
#----------------------------------------------------------------------------------
# 9:3 개의 중요한 'python file'과 그 역할 이미지 컷; choice.py/ app.py/ record_agent.py
#-----------------------------------------------------------------------------------
def show_python_agent_image():
    clear_screen()
    image=Image.open("step9_python_agent.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_agent_memory,y=530)
    add_next_button("'Python'파일들 구조 이해 됐어요.",show_learning_way,x=630,y=530)
#----------------------------------
# 10:가장 중요한 학습방식
#----------------------------------
def show_learning_way():
    clear_screen()
    add_title("코드를 전부 기억하고 있나요?")
    add_message("아마 아닐겁니다. 그래도 괜찮습니다.\n\n"
    "우리는 코드를 하나하나 외우려고 하는게 아닙니다.\n"
    "무엇이 어떻게 코딩되어 표현되는지 그 구조를 알면되니까요.\n\n"
    "그래서, 그 구조를 먼저 생각하게 질문을 던진 다음,\n"
    "실제 코드를 똑같이 쓰면서 전체 구조와 연결을 느끼도록 했습니다.\n\n"
    "코딩이 어렵거나 구조적인 부분 궁금하면,\n"
    "필요할 때마다 휴대폰 'AI'에게 물어 보면서 여기까지 왔잖아요?\n\n"
    "지금처럼 디지털화된 시대에 반드시 필요한 습관이기 때문입니다.")
    add_previous_button("이전",show_agent_memory,y=530)
    add_next_button("궁금할때 'AI'에게 물어볼게요.",show_two_records,x=600,y=530)
#---------------------------------
# 11: 아이와 엄마의 서로 다른 기록
#---------------------------------
def show_two_records():
    clear_screen()
    add_title("같이 함께했지만 서로의 경험은 달라요.")
    add_message("아이의 동굴 탐사에 보호자인 엄마도 함께 동행했었죠?\n\n"
    "하지만, 동굴 탐사 중에 떠오르는\n"
    "생각과 느낌은 서로 다를 수밖에 없습니다.\n\n"
    "그래서, 각각 두 사람의 탐사 과정을 기록들로 남겼었고,\n"
    "'AI 에이전트'를 직접 만들어 정리해 저장까지 했었죠?\n\n"
    "어느 것이 맞고 틀린 것이 중요한게 아니라,\n"
    "서로 다른 그 경험들이 가장 소중한 보물입니다.",y=130)
    add_previous_button("이전",show_learning_way,y=500)
    add_next_button("'탐사기록'이 더 소중해 졌어요.",show_keep_recording,x=600,y=500)
#--------------------------------
# 12:기록은 계속된다.
#--------------------------------
def show_keep_recording():
    clear_screen()
    add_title("동굴 밖에서도 계속 기록해 볼까요?")
    add_message("'미래로 통하는 동굴 탐사'가 다 끝났습니다.\n"
    "앞으로 펼쳐질 미래 세계가 조금이라도 더 느껴지십니까?\n\n"
    "미래로 나아가는 길은 저마다 다르겠지만,\n"
    "구조를 먼저 생각하고 그때마다 느껴지는 것들을,\n"
    "한줄로 요약해서 기록하는 습관을 꼭 만드세요.\n\n"
    "아마도 그러한 좋은 습관들이,\n"
    "미래에 쉽게 적응하며 아이의 꿈도 실현시켜주는,\n"
    "나침반같은 새로운 도구가 되지 않을까요?",y=130)
    add_previous_button("이전",show_two_records)
    add_next_button("꼭 기록 계속할게요.",show_share_record)
#--------------------------------
# 13: 나누고 싶은 것
#--------------------------------
def show_share_record():
    clear_screen()
    add_title("어떤 기록들은 다른 사람들과 나눌수록 좋아요.",size=27)
    add_message("혼자 느껴지는 긴 글들이나 간직하고 싶은\n"
    "기록들은 공개하지 말고 그대로 보관하세요.\n\n"
    "함께 같은 길을 걸어가는 다른 사람들과\n"
    "나누고 싶은 것들만 골라서 공개하면 됩니다.\n\n"
    "언젠가 '미래로 통하는 동굴 탐사'를\n"
    "경험한 아이와 엄마가 많아지면,\n\n"
    "'블로그'같은 새로운 공간에서,\n"
    "서로의 경험담들을 즐겁게 나눌 수 있습니다.\n\n"
    "그래서, 밝은 미래를 모두 함께 힘을 모아,\n"
    "펼쳐 나가면 더 좋지않을까요?",size=17,y=110)
    add_previous_button("이전",show_keep_recording,y=550)


show_child_safety()
root.mainloop()
