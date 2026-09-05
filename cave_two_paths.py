import tkinter as tk
from PIL import Image, ImageTk
root=tk.Tk()
root.title("두 갈래길 동굴")
root.geometry("900x600")
#--------------
#  공통기능
#--------------
def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()
def add_title(text,size=25,x=30,y=20):
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
def add_message(text,x=70,y=100,size=16):
    message=tk.Label(root,text=text,
    font=("나눔고딕",size), justify="left")
    message.place(x=x,y=y)
    #---------------------
    # 1.겉표지
    # --------------------
def show_cover():
    clear_screen()
    image=Image.open("two_paths_cover.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_next_button("탐사시작",show_review,x=800,y=530)
#---------------------
#2. 준비단계 돌아보기
#---------------------
def show_review():
    clear_screen()
    add_title("준비된 도구들 다시 살펴볼까요?",x=150,size=30)
    text=("'Python'은 어떤 일을 했었죠?\n\n"
    "'VS Code'에서는 무슨 작업을 했었나요?\n\n"
    "잘 기억나지 않으면, \n\n"
    "지난 '준비단계' 탐사에서 직접 확인해 보세요.")
    add_message(text,x=150,y=150,size=20)
    add_previous_button("이전",show_cover,x=150)
    add_next_button("직접 확인해 볼게요",show_run_check)
#-----------------------
# 3. 준비단계 코드 다시 반복 실행
#-----------------------
def show_run_check():
    clear_screen()
    add_title("지난번 작성된 코드 다시 실행해 볼까요?",x=100,size=27)
    text=("'VS Code'에서 지난 탐사 때 만들었던\n"
    "'hello_cave.py'를 열어 보세요.\n\n"
    "그리고 아래쪽 '터미널'에서\n"
    "'Python hello_cave.py'를\n\n"
    "입력하고 'Enter'로 실행합니다.\n\n"
    "내 닉네임과 엄마의 닉네임을 직접 입력해\n"
    "지난번처럼 동굴과 인사하며 소통되는지 확인해 보세요.")
    add_message(text,x=100,y=130,size=19)
    add_previous_button("이전",show_review,x=100)
    add_next_button("확인했어요",show_two_paths)
#-------------------------------
# 4. 두 갈래길 이미지
#-------------------------------
def show_two_paths():
    clear_screen()
    image=Image.open("two_paths_cave.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_run_check,y=530)
    add_next_button("어느 길로 갈까요?",show_choice_1,x=700,y=530)
#-----------------------------
# 5. 두 가지 선택-1.
#-----------------------------
def show_choice_1():
    clear_screen()
    add_title("우리는 일상에서 매일 선택을 합니다.",x=100,size=30)
    text=("이 길로 갈까, 가지 말까?\n\n"
    "이걸 지금 할까, 말까?\n\n"
    "밥을 먹을까, 말까?\n\n\n"
    "가만히 생각해 보면 하루에도 많은 순간,\n"
    "두 가지 중 하나를 선택하며 살아갑니다.")
    add_message(text,x=100,y=120,size=20)
    add_previous_button("이전",show_two_paths,x=100)
    add_next_button("그런데, 코딩에서는?",show_choice_2)
#-----------------------------
# 6. 두가지 선택-2.
#-----------------------------
def show_choice_2():
    clear_screen()
    add_title("두가지 중 하나 선택이 가능한가요?",x=100,size=30)
    text=("'네/아니요'\n"
    "아니면, 'Yes/No' 처럼 \n\n"
    "코딩에서는 어떤 조건이 제시되면\n"
    "한쪽 또는 다른 쪽으로 선택할 수 있습니다.\n\n"
    "그때 사용되는 가장 기본적인 코딩 표현이,\n"
    "'if'와 'else'입니다.")
    add_message(text,x=100, y=140, size=20)
    add_previous_button("이전",show_choice_1,x=100)
    add_next_button("직접 경험해 볼까요?",show_food_code)
#-----------------------------
# 7. 둘 중 하나 선택하는 코딩
#-----------------------------
def show_food_code():
    clear_screen()
    add_title("지금 밥 먹을까요?",x=100,size=30)
    text=("매우 간단한 '선택 구조'를 만들어 볼까요?\n\n"
    "'VS Code'의 창 왼쪽 위에있는 'File'을 클릭해,\n"
    "'Python'의 'new file'을 만드세요.\n\n"
    "새 파일 이름을 'choice.py'로 입력하면,\n"
    "좌측의 'Explorer'에 'choice.py'라고 보이게 됩니다.")
    add_message(text,x=100,y=150,size=20)
    add_previous_button("이전",show_choice_2,x=100)
    add_next_button("코드를 볼까요?",show_food_code_2)
#-----------------------------
# 8. 선택하는 코드 입력
#-----------------------------
def show_food_code_2():
    clear_screen()
    add_title("두 갈래 선택을 코드로 만들어 봅시다.",x=100,size=27)
    text=('answer=input("우리 지금 밥 먹을까요?(y/n):")\n\n'
    'if answer=="y":\n'
    'print("네. 배고파요.")\n\n'
    'else:\n'
    'print("아니요. 배불러요.")\n\n'
    "입력이 다 끝났으면 'Ctrl+S'를 눌러 저장합니다.")
    add_message(text, x=100,y=120,size=20)
    add_previous_button("이전",show_food_code,x=100)
    add_next_button("입력했어요",show_food_run)
#-----------------------------
# 9.직접실행
#-----------------------------
def show_food_run():
    clear_screen()
    add_title("직접 실행해 볼까요?",x=100,size=28)
    text=("아래쪽 '터미널' 반짝 거리는 곳에, \n"
    "'python choice.py'를\n"
    "입력하고 'Enter'를 누릅니다.\n\n"
    "한번은 'y'를 선택해 눌러보고,\n"
    "종료 후 다시 살행해서 'n'도 눌러 보세요.\n\n"
    "엄마도 직접 한번 해보세요.")
    add_message(text,x=100,y=140,size=20)
    add_previous_button("이전",show_food_code_2,x=100)
    add_next_button("양쪽 선택 다 해봤어요.",show_food_feeling)
#---------------------------------
# 10. 실행 후 느낌
#---------------------------------
def show_food_feeling():
    clear_screen()
    add_title("선택에 따라서 서로 다른 결과가 나타났죠?",x=100,size=28)
    text=("선택하는 'y'와 'n'의 결과로,\n"
    "서로 다른 답변들이 나오는 것을,\n"
    "직접 보셨죠?\n\n"
    "왜 그럴까 한번 생각해 보세요.\n\n"
    "이런 선택과 결과를 코드로 어떻게 표현했는지,\n"
    "동굴 탐사 중에도 계속 음미해 보세요.")
    add_message(text,x=100,y=140,size=20)
    add_previous_button("이전",show_food_run,x=100)
    add_next_button("동굴 안으로 더 나아가 볼까요?",show_door,x=600)
#----------------------------------
# 11. 첫 번째 동굴의 문
#----------------------------------
def show_door():
    clear_screen()
    image=Image.open("cave_door.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_previous_button("이전",show_food_feeling,y=530)
    add_next_button("문으로 더 가까이 가볼까요?",show_door_question,y=530)
#-----------------------------------
# 12. 문을 열 수 있는 동굴의 질문
#-----------------------------------
def show_door_question():
    clear_screen()
    add_title("동굴의 질문에 답하세요.",x=100,size=30)
    text=("이 문을 열 수 있는 키는 동굴의 질문에\n"
    "'네 / 아니요'로 바른 선택을 하는 겁니다.\n\n"
    "쉬잇! 조용히 들어보세요.\n"  
    "동굴이 질문하네요.\n\n"
    "Python이 스스로 코드를 만들어서 \n"
    "직접 작업할 수 있나요?\n\n"
    "먼저 마음 속으로 '네' 또는 '아니요'를 선택해 보세요.\n\n")
    add_message(text,x=100,y=120,size=20)
    add_previous_button("이전",show_door,x=100)
    add_next_button("선택했어요",show_door_code)
#-----------------------------------
# 13. 첫 번째 동굴 문 통과 선택 코드
#----------------------------------
def show_door_code():
    clear_screen()
    add_title("코드 작업으로 문을 열어 볼까요?",x=30,size=27)
    text=('answer=input("Python이 스스로 코드를 만들어서 직접 작업할 수 있나요?(y/n):")\n'
    'if answer == "n":\n'
    'print("철커덕! 문이 열렸습니다.")\n\n'
    'else:\n'
    'print("지나왔던 길들을 다시 한번 살펴보세요.")\n\n'
    "'Ctrl + S'로 저장하고 아래쪽 '터미널에서,\n"
    "'python choice.py'를 쓰고 'Enter'로 실행하세요.\n")
    add_message(text,x=30,y=130,size=18)
    add_previous_button("이전",show_door_question,x=30)
    add_next_button("실행해볼게요",show_door_result,x=700)
#--------------------------------------
# 14. 실제 선택
#--------------------------------------
def show_door_result():
    clear_screen()
    add_title("드디어 동굴 문이 열렸나요?",x=100,size=30)
    text=("직접 실행해 보셨죠?\n\n"
    "'n'을 선택했다면 문이 열렸을 겁니다.\n\n"
    "그런데 만약 'y'를 선택했다면 \n"
    "동굴 문이 안 열릴 겁니다.\n\n"
    "왜 동굴 문이 그렇게 침묵하고 안 열어 주었을까요?\n\n"
    "지나왔던 길의 의미를 되새겨 보고,\n"
    "다시 한번 질문에 도전하세요.")
    add_message(text,x=100,y=120,size=20)
    add_previous_button("이전",show_door_code,y=520,x=100)
    add_next_button("문을 통과했어요",show_history,y=520)
#----------------------------------------
# 15. 탐사 기록 
#----------------------------------------
def show_history():
    clear_screen()
    add_title("우리 '탐사 기록'을 남겨 볼까요?",x=70,size=30)
    text=("어떤 도구를 어떻게 사용했었는지 깜빡깜빡하죠?.\n"
    "'탐사 기록'이 있으면 좋겠죠?.\n\n"

    "'VS Code'의 왼쪽 위 'File'을 누르고,\n"
    "'history.txt'라는 '새 파일 이름'을 만듭니다.\n\n"

    "탐사하며 생각하고 느껴지는 것들의\n"
    "짧은 요약 노트입니다.\n\n"
    "탐사를 이어갈수록 경험따라 쌓여갈 겁니다.")
    add_message(text,y=120,size=20)
    add_previous_button("이전",show_door_result,x=70)
    add_next_button("계속 기록해 볼게요",show_history_write)
#---------------------------------------------
# 16. 탐사 기록 작성
#---------------------------------------------
def show_history_write():
    clear_screen()
    add_title("경험을 기록으로 남기세요",x=70,size=30)
    text=("탐사했던 경험들을,\n"
    "하나의 흐름처럼 느껴보세요.\n\n"
    "도구를 찾아서 사용 방법을 어떻게 배웠죠?.\n"
    "동굴과 처음 소통했던 순간도 기억나시죠?\n"
    "흐름따라 기억나는 순서대로 요약하세요.\n\n"
    "엄마도 느낌을 기록해두면 좋지 않을까요?\n"
    "일기쓰듯 하지 마시고 탐사 중에\n"
    "생각과 느낌을 그때그때 요약 기록해 두세요.")
    add_message(text,x=70,y=120,size=20)
    add_previous_button("이전",show_history,x=70)
    add_next_button("계속 기록 할게요",show_second_door)
#-----------------------------------------------
# 17. 두번째 동굴의 문
#---------------------------------------------
def show_second_door():
    clear_screen()
    add_title("또 다른 동굴의 문이 나왔네요!",x=100,y=50,size=30)
    text=("저번 것보다 더 단단하게\n"
    "이중으로 잠겨 있네요.\n\n"
    "이번에는 두가지를 물어 본다고 합니다.\n\n"
    "앞에서 한번 경험해 봤으니,\n"
    "마음 단단히 먹고 신중하게 미리 생각해 선택해 보세요.")
    add_message(text,x=100,y=160,size=20)
    add_previous_button("이전",show_history_write,x=100)
    add_next_button("첫 번째 질문",show_second_question_1)
#-----------------------------------------------
# 18. 동굴 문의 첫 번째 질문
#---------------------------------------------
def show_second_question_1():
    clear_screen()
    add_title("첫 번째 질문 선택하세요.",x=100,size=30)
    text=("지금까지 우리는 두 갈래 길 중\n"
    "하나를 선택하며 여기까지 왔습니다.\n\n"
    "동굴은 두 갈래길보다 많을 경우 어떻게 할건지,\n"
    "코드로 둘 이외의 다른 선택도 할 수 있느냐고 질문하네요.\n\n" 
    "'네 / 아니요' 둘 중 하나로 답하래요.\n\n"
    "엄마와도 잘 의논해서 선택할 방향을 결정하세요.")
    add_message(text,x=100,y=130,size=20)
    add_previous_button("이전",show_second_door,x=100)
    add_next_button("결정했어요",show_second_question_2)
#-----------------------------------------------
# 19. 동굴 문의 두 번째 질문
#----------------------------------------------
def show_second_question_2():
    clear_screen()
    add_title("두 번째 질문 선택하세요.",x=100,size=30)
    text=("지금까지 동굴은 우리가 코드로,\n"
    "미리 입력해 놓은 규칙으로만 말을 했습니다.\n\n"

    "그런데, 동굴은 이렇게 미리 정해진 것도 좋지만,\n"
    "그 이외의 다른 말들로 당신들과 소통하고 싶다네요.\n\n"

    "가능하다면 '네', 가능하지 않다면 '아니요'라고 답하래요.\n\n"
    "첫 질문처럼 엄마와 잘 의논해 보시고 선택하세요.")
    add_message(text,x=100,y=130,size=20)
    add_previous_button("이전",show_second_question_1,x=100)
    add_next_button("방향 결정 했어요",show_second_code_1)
#----------------------------------------------
# 20. 첫 번째 동굴 질문 코딩
#----------------------------------------------
def show_second_code_1():
    clear_screen()
    add_title("첫 번째 질문 상황을 코드로 만들어 봅시다.",x=50,size=28)
    text=("VS Code 위쪽 코드 작업 공간에 아래처럼 입력합니다.\n\n"
    'path=input("코딩에서도 두 갈래 이외의 다른 길이 있을까요?(y/n):")\n\n'
    'if path =="y":\n'
    'print("철커덕! 첫 번째 잠금이 풀렸습니다.")\n\n'
    'else:\n'
    'print("엄마와 다시한번 잘 의논해 보세요.")\n\n'
    "다 입력하고 꼼꼼하게 확인했으면 Ctrl+S로 꼭 저장부터 하세요.")
    add_message(text,x=50, y=100,size=18)
    add_previous_button("이전",show_second_question_2,x=50)
    add_next_button("저장했어요.", show_second_code_2,x=700)
#-------------------------------------------
# 21. 두 번째 동굴 질문 코딩
#--------------------------------------------
def show_second_code_2():
    clear_screen()
    add_title("두 번째 질문 상황도 코드로 만들어 봅시다.",x=50,size=28)
    text=("첫 번째 질문 상황 코딩에 이어서 계속 합니다.\n\n"
    'talk = input("미리 정해 놓지 않은 말들도 동굴이 할 수 있을까요?(y/n):")\n\n'
    'if talk == "y":\n'
    'print("철커덕! 두 번째 잠금도 풀렸습니다.")\n\n'
    'else:\n'
    'print("엄마와 다시한번 잘 의논해 보세요.")\n\n'
    "입력 끝났으면 검토 확인하고 반드시 저장하세요.")
    add_message(text,x=50,y=100,size=18)
    add_previous_button("이전", show_second_code_1,x=50)
    add_next_button("확인하고 저장까지 했어요", show_second_run)
#--------------------------------------------
# 22. 두 번째 동굴 문 선택 실행
#-------------------------------------------
def show_second_run():
    clear_screen()
    add_title("잠금을 풀고 동굴 문을 열어 볼까요?",x=100,size=28)
    text=("'VS Code' 아래쪽 '터미널'에\n"
    "'python choice.py'를 쓰고,\n"
    "직접 'Enter'로 실행해 봅니다.\n\n"
    "첫 번째 질문에 답하고,\n"
    "두 번째 질문에도 답해 보세요.\n\n"
    "반복해 보면서 주어지는 조건들과,\n"
    "선택에 따라서 결과가 달라지는 이 구조의\n"
    "의미를 이해하고 꼭 기억해 두어야 합니다.")
    add_message(text,x=100,y=130,size=20)
    add_previous_button("이전", show_second_code_2,x=100)
    add_next_button("이 구조의 의미를 이해했어요.", show_second_result)
#--------------------------------------------
# 23. 두 번째 동굴 문 통과
#-------------------------------------------
def show_second_result():
    clear_screen()
    add_title("두 번째 문도 열렸습니다!",x=100,size=28)
    text=("질문들에 다 '네'라고 선택했으면\n"
    "잠금들이 모두 풀렸을 겁니다.\n\n"
    "그런데, 선택한 두가지 외에도 또다른 길로\n"
    "갈 수있는 기회들이 있을 수 있잖아요?\n\n"
    "정해진 규칙을 따르는 소통이 효율적이긴 하지만,\n"
    "그 이외에 다양한 방법들이 필요하지 않을까요?")
    add_message(text,x=100,y=130,size=20)
    add_previous_button("이전", show_second_run,x=100)
    add_next_button("이어지는 동굴 탐사로",show_review_stage)
#---------------------------------------------
# 24. 두 갈래길 탐사 되돌아 보기
#---------------------------------------------
def show_review_stage():
    clear_screen()
    add_title("'두 갈래길'과 이어지는 동굴 탐사",x=100,size=28)
    text=("둘 중 하나라는 선택이 주는 구조가 떠오르나요?\n\n"
    "구조를 이해하며 왜 그런지 계속 원인을\n"
    "깊이 찾아가는 좋은 습관을 만들어 보세요.\n\n"
    "이어지는 다음 탐사에서 동굴이\n"
    "다양한 소통 할 수 있는 방법을 찾아 볼까요?\n\n"
    "지금 느껴지는 생각과 느낌을 꼭 'history'에 남기세요.\n\n"
    "엄마도 이번 탐사 기록을 꼭 남겨두세요?")
    add_message(text,x=100,y=120,size=18)
    add_previous_button("이전",show_second_result,x=100)

show_cover()
root.mainloop()     