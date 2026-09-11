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
    "계속 진행하면 위 안내와 아래 사항에 동의한 것으로 간주합니다.\n\n",size=20,x=70,y=120)
    add_message("* 개인정보는 입력하거나 공개하지 않습니다.\n" 
    "* 비밀번호와 API Key는 다른 사람에게 보여주지 않습니다.\n"
    "* 모르는 파일이나 프로그램은 함부로 설치하지 않습니다.\n"
    "* 결제나 비용이 발생하는 작업은 보호자와 함께 확인하고 승인합니다.\n"
    "* 'AI'의 답변은 틀릴 수 있으니 중요한 내용은 한 번 더 확인합니다.",size=18,x=70,y=260)
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
    "각각 자신의 느낌을 'trip.txt'에 요약 정리해 놓았죠?\n\n"
    "혹시 빠진 것들이 있을지 모르니,\n"
    "지금이라도 잊어버리기 전에 빨리 기록으로 남기세요.\n\n"
    "기록할 때 먼저 (아이)와(엄마)라고 꼭 앞에 쓰고,\n"
    "서로 다른 각각의 생각과 느낌을 요약해 보세요.\n\n"
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
    "'탐사기록' 정리를 충분히 도와줄 수 있다고 하네요.\n\n"
    "자세히 안내할테니 잘 따라오라고 합니다.\n\n"
    "먼저, 이러한 목표를 도와줄 'record_agent.py'라는\n" 
    "새 파일을 'VS Code'에서 만들어야만 합니다.\n\n"
    "이 파일은 'trip.txt'의 우리 기록을 'LLM'과 함께,\n"
    "분류 정리해 각각의 새파일에 저장해 준다고 하네요.",size=18,y=130)
    add_previous_button("이전",show_first_step)
    add_next_button("새파일 만들었어요.",show_structure)
#--------------------------------------------
# 6:  이 구조와 의미를 알아볼까요.
#--------------------------------------------
def show_structure():
    clear_screen()
    add_title("왜 이렇게 하는지 구조와 의미를 알아볼까요?\n\n",size=28)
    add_message("'LLM'에게 'trip.txt'에 기록된 탐사기록을,\n"
    "각각 분류해서 계속 사용할 수 있게 해달라고 부탁했어요.\n\n"
    "그래서, 우리는 'LLM'이 이러한 작업할 쉽게할 수 있는,\n"
    "새파일 'record_agent.py'를 만들었습니다.\n\n"
    "이 파일은 'trip.txt.'의 우리기록들을\n"
    "'LLM'에게 분류해 정리를 부탁한 뒤 결과를\n"
    "다시 각각의 새파일에 저장하도록 연결한다고 하네요.\n\n"
    "이렇게 목표를 주면 여러 작업을 이어서 수행하는,\n"
    "작은 'AI Agent'의 형태를 우리가 직접 만들어 볼 겁니다.",size=18,y=130)
    add_previous_button("이전",show_new_tool,y=510)
    add_next_button("만들어 보고 싶어요!",show_prompt_1,y=510)
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
    "3. '(아이)와 (엄마)의 기록'을 각각 나누어 정리합니다.\n\n"
    "4. '새로운 파일'에 각각 정리한 내용을 저장합니다.\n\n"
    "이렇게 중간에서 여러가지 일을하는 'Python 파일'입니다.",size=18,y=110)
    add_previous_button("이전",show_structure)
    add_next_button("어떻게 부탁하죠?",show_prompt_2)
#---------------------------------------------
# 8: 프롬프트
#---------------------------------------------
def show_prompt_2():
    clear_screen()
    add_title("'LLM'에게 어떻게 부탁하는게 효율적일까요?",size=28)
    add_message("'LLM'에게 부탁할 때는 자세하고 분명하게\n"
    "무엇을 원하는지 알려주는 것이 중요한 요령입니다.\n\n"
    "즉, '우리 탐사기록을 정리해 주세요.'보다는,\n\n"
    "'trip.txt의 탐사기록 읽고,\n"
    "(아이)와 (엄마) 기록 구분 정리한 뒤,\n"
    "각각 다른 파일로 저장해 주세요.'라고 하면,\n"
    "부탁한 일이 훨씬 정확하고 분명해 집니다.\n\n"
    "'LLM'이 부탁하는 것을 더 잘 이해할 수있게\n"
    "구체적으로 질문하고 부탁하는 것이,\n"
    "바로 효율적으로 '프롬프트(prompt)'하는 방법입니다.",size=18,y=110)
    add_previous_button("이전",show_prompt_1,y=520)
    add_next_button("효율적 '프롬프트' 이해했습니다.",show_code_1,x=550,y=520)
#----------------------------------------------
# 9: 그러면 어떠한 방향으로 코딩해야 실행이 잘 될까요?
#----------------------------------------------    
def show_code_1():
    clear_screen()
    add_title("흐름에따라 구조적으로 간결하게 코딩하세요.",size=28)
    add_message("먼저, 코드를 몰라도 흐름의 내용은 알고있으니,\n"
    "스스로 어떻게 구조를 기획하는게 효과적일지 생각해 보세요.\n\n"
    "여러가지 방법이 있겠지만, 'LLM'에게 추천해 달라고 부탁하니.\n"
    "자기는 아래와 같이 코딩을 하고 싶다고 합니다.\n\n"
    "1. 작업 시작하려면 'record_agent.py'를 코딩으로 불러냅니다.\n" 
    "2. 그러면, '탐사기록'인 'trip.txt'를 읽고 'LLM'에게 전달 합니다.\n"
    "3. 'LLM'은 (아이)와 (엄마) 기록을 분류하고 정리합니다.\n"
    "4. 'LLM'이 두 사람 각각의 새파일을 만들어 따로따로 정리시킵니다.\n"
    "5. 누군가 'Python'의 '터미널'에서 '실행'을 요청하면 보여줍니다.\n\n"
    "복잡한 것들도 구조적으로 흐름따라 요약하면 간결하게 정리된다고합니다.",size=18)
    add_previous_button("이전",show_prompt_2,y=530) 
    add_next_button("구조가 중요하네요!",show_code_2,y=530)
#-------------------------------------------------------
# 10: 도식처럼 탐사기록/Python file/LLM 관계 보여주는 이미지
#------------------------------------------------------

#--------------------------------------------------------
# 11: 'record_agent.py' 불러내는 코딩
#---------------------------------------------------------
def show_code_2():
    clear_screen()
    add_title("코드 암기하지 말고 흐름과 구조를 느껴보세요.",size=26)
    add_message("새파일 'record_agent.py'를 열고 'VS Code 위쪽 작업창에,\n"
    "아래 코드를 '4칸 띄여쓰기'한 것이나 점 하나까지 정확히 입력하세요.\n\n",size=18,y=110)
    add_message("from openai import OpenAI\n"
    "from dotenv import load_dotenv\n\n"
    "load_dotenv()\n"
        "client=OpenAI()\n\n"
        "with open(\"trip.txt\",\"r\",encoding=\"utf-8\")as file:\n"
        "     trip=file.read()\n\n", size=14,y=200)
    add_message("여기까지는 'trip.txt'에 있는 '탐사기록'을\n"
    "'record_agent.py'에게 사용할 수있도록 불러오는 코딩입니다.\n"
    "참고로 마지막 줄처럼 안으로 4칸 '들여쓰기'를 똑같이 하세요.",size=18,y=400)
    add_previous_button("이전",show_prompt_2,y=530)
    add_next_button("다음 코딩은?",show_code_3,x=700,y=530)
#-------------------------------------------
# 12: 'LLM'에게 실제로 부탁하는 코딩_1.
#------------------------------------------- 
def show_code_3():
    clear_screen()
    add_title("'프롬프트'로 직접 'LLM'에게 일을 부탁해 볼까요?",size=26)
    add_message("바로 전 코딩에 추가해서 본격적으로 쭉 이어갑니다.\n\n",size=18,y=100)
    add_message("def organize_record(person):\n"
    "prompt=f\"\"\"\n"
    "다음은 아이와 엄마가 함께한 탐사 기록입니다.\n\n"
    "{trip}\n\n"
    "각 기록 앞에 적힌 (아이)와 (엄마)를 기준으로\n"
    "{person}의 기록만 찾아 정리해 주세요.\n\n" 
    "이 기록에 없는 사실은 새로 만들지 마세요.\n"
    "다음 순서로 쉽고 자연스럽게 정리해 주세요.\n\n"
    "기억에 남는 것:\n"
    "느껴지는 것:\n"
    "새롭게 알게된 것:\n"
    "미래에 해보고 싶는 것:\n",size=14,y=170)
    add_previous_button("이전",show_code_2,y=540)
    add_next_button("'LLM'과 연결",show_code_4,x=700,y=540)
#-------------------------------------------------
# 13: 'LLM'에게 실제로 부탁하는 코딩_2.
#------------------------------------------------
def show_code_4():
    clear_screen()
    add_title("계속 추가해서 코딩 이어갑니다.",size=26)
    add_message('    response=client.responses.create(\n'
    '        model="gpt-5-mini",\n'
    '        input=prompt\n'
    '        )\n'
    '    return response.output_text\n\n'
    'child_record=organize_record("아이")\n'
    'mom_record=organize_record("엄마")\n\n'
    'with open("child_journey.txt","w",encoding="utf-8") as file:\n'
    '    file.write(child_record)\n\n'
    'with open("mom_journey.txt","w",encoding="utf-8") as file:\n'
    '    file.write(mom_record)\n\n'
    'print("탐사 기록 정리가 끝났습니다!")\n'
    'print("child_journey.txt")\n'
    'print("mom_journey.txt")',size=14,y=100)
    add_previous_button("이전",show_code_3,y=540)
    add_next_button("코딩 끝났어요.",show_run_agent,y=540)
#--------------------------------------------------
# 14: 그럼 한 번 실행해 볼까요?
#-------------------------------------------------
def show_run_agent():
    clear_screen()
    add_title("이제 직접 실행해 볼까요?",size=28)
    add_message("'Ctrl+S'로 저장한 후 아래 '터미널'에서\n"
    "'python record_agent.py'라고 쓰고 직접 'Enter'로 실행하세요.\n\n"
    "잠시 기다리는 동안 우리가 코딩한 프로그램이,\n"
    "우리 '탐사기록'을  다 읽고,\n"
    "'LLM'에게 어떻게 해달라고 정리를 부탁한,\n"
    "결과들이 두 사람 각각의 새 파일에 저장됩니다.\n\n"
    "(아이)와 (엄마) 각각의 파일을 열어서,\n"
    "어떤 일들이 벌어졌는지 봐야겠죠?",size=18,y=140)
    add_previous_button("이전",show_code_4)
    add_next_button("보고 싶어요!",show_agent_result)
#--------------------------------------------------
# 15: 두 사람의 새로운 파일
#--------------------------------------------------
def show_agent_result():
    clear_screen()
    add_title("새로운 파일이 생겼나요?",size=28)
    add_message("'VS Code'의 왼쪽 파일 목록을 살펴보세요.\n\n"
    "'child_journey.txt'와,\n"
    "'mom_journey.txt'라는,\n"
    "(아이)와 (엄마)의 새로운 파일들이 보이나요?\n\n"
    "각각 하나씩 클릭해서 열어보시고 나서,\n"
    "탐사하는 동안의 생각과 느낌의 기록들이\n"
    "어떻게 정리되어 있는지 살펴보세요.\n\n"
    "지나온 흐름과 구조를 되돌아보며\n"
    "비교하면서 보면 또다른 느낌이 들겁니다.",size=18,y=140)
    add_previous_button("이전",show_run_agent)
    add_next_button("신기해요.",show_agent_difference)
def show_agent_difference():
    clear_screen()
    add_title("",size=28)
    add_message("",size=18,y=140)
#------------------------------------------------------
# 16: 코딩 후 이와 관련된 변화와 에이전트 역할 관련 이미지 컷
#-------------------------------------------------------

#-----------------------------------------------------
# 17: 예전 'LLM'과 무엇이 달라졌나요?
#------------------------------------------------





 

show_child_safety()
root.mainloop()