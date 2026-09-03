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
def add_title(text):
    title=tk.Label(root,text=text,
    font=("Arial",24,"bold"))
    title.pack(pady=30)
def add_next_button(text,command,y=480):
    button=tk.Button(root,text=text,
    font=("Arial",12), command=command)
    button.place(x=600,y=y)
def add_previous_button(text,command,y=480):
    button=tk.Button(root,text=text,
    font=("Arial",12), command=command)
    button.place(x=70,y=y)
def add_message(text):
    message=tk.Label(root,text=text,
    font=("Arial",14), justify="left")
    message.pack(pady=20)
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
    add_next_button("탐사시작",show_review,y=530)
#---------------------
#2. 준비단계 돌아보기
#---------------------
def show_review():
    clear_screen()
    add_title("준비된 도구들 다시 살펴볼까요?")
    add_message("Python은 어떤 일을 했었죠?\n\n"
    "VS Code에서는 무슨 작업을 했었나요?\n\n"
    "잘 기억나지 않으면 \n"
    "지난 준비단계 탐사에서 직접 확인해 보세요.\n\n")
    add_previous_button("이전",show_cover)
    add_next_button("직접 확인해 볼게요",show_run_check)
#-----------------------
# 3. 준비단계 코드 다시 반복 실행
#-----------------------
def show_run_check():
    clear_screen()
    add_title("지난번 작성된 코드 다시 실행해 볼까요?")
    add_message("VS Code에서 지난 탐사 때 만들었던\n"
    "hello_cave.py를 열어 보세요.\n\n"
    "그리고 아래쪽 터미널에서\n\n"
    "Python hello_cave.py\n\n"
    "를 입력하고 Enter를 누릅니다.\n\n"
    "내 닉네임과 엄마의 닉네임을 직접 입력해\n"
    "지난번처럼 동굴과 인사하며 소통되는지 확인해 보세요.\n\n")
    add_previous_button("이전",show_review)
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
    add_next_button("어느 길로 갈까요?",show_choice_1,y=530)
#-----------------------------
# 5. 두 가지 선택-1.
#-----------------------------
def show_choice_1():
    clear_screen()
    add_title("우리는 일상에서 매일 선택을 합니다.")
    add_message("이 길로 갈까, 가지 말까?\n\n"
    "이걸 지금 할까, 말까?\n\n"
    "밥을 먹을까, 말까?\n\n"
    "가만히 생각해 보면 하루에도 수없이\n"
    "두 가지 중 하나를 선택하며 살아갑니다.\n\n")
    add_previous_button("이전",show_two_paths)
    add_next_button("그런데, 코딩에서는?",show_choice_2)
#-----------------------------
# 6. 두가지 선택-2.
#-----------------------------
def show_choice_2():
    clear_screen()
    add_title("코딩에서도 두가지 중 하나 선택이 가능한가요?")
    add_message("'네/아니요'\n"
    "아니면, 'Yes/No' 처럼 \n\n"
    "코딩에서는 어떤 조건이 제시되면\n"
    "한쪽 또는 다른 쪽으로 선택할 수 있습니다.\n\n"
    "그때 사용되는 가장 기본적인 코딩 표현이\n"
    "'if'와 'else'입니다.\n\n")
    add_previous_button("이전",show_choice_1)
    add_next_button("직접 경험해 볼까요?",show_food_code)
#-----------------------------
# 7. 둘 중 하나 선택하는 코딩
#-----------------------------
def show_food_code():
    clear_screen()
    add_title("지금 밥 먹을까요?")
    add_message("아주 간단한 사례로 선택 구조를 만들어 봅시다.\n\n"
    "먼저, 'VS Code'의 창 위에있는 'File'을 클릭해 'Python'의 'new file'을 만들고\n"
    "새 파일 이름을 'choice.py'로 만들면 좌측의 'Explorer'에 'choice.py'라고 보이게 됩니다.\n\n"
    "그런 다음, 위쪽에 있는 코드 작업창 공간에 다음 코드를 입력하세요.\n\n")
    add_previous_button("이전",show_choice_2)
    add_next_button("코드를 볼까요?",show_food_code_2)
#-----------------------------
# 8. 선택하는 코드 입력
#-----------------------------
def show_food_code_2():
    clear_screen()
    add_title("두 갈래 선택을 코드로 만들어 봅시다.")

    add_message('answer=input("우리 지금 밥 먹을까요?(y/n):")\n\n'
    'if answer=="y":\n'
    'print("네. 배고파요.")\n'

    'else:\n'
    'print("아니요. 배불러요.")\n\n'

    "입력이 다 끝났으면 Ctrl+S를 눌러 저장합니다.\n\n")
    add_previous_button("이전",show_food_code)
    add_next_button("입력했어요",show_food_run)
#-----------------------------
# 9.직접실행
#-----------------------------
def show_food_run():
    clear_screen()
    add_title("직접 실행해 볼까요?")
    add_message("아래쪽 터미널 반짝 거리는 곳에 \n\n"
    "'python choice.py'를\n\n"
    "입력하고 'Enter'를 누릅니다.\n\n"
    "한번은 'y'를 선택해 눌러보고,\n"
    "종료 후 다시 살행해서 'n'도 눌러 보세요.\n\n"
    "엄마도 직접 한번 해보세요.\n\n")
    add_previous_button("이전",show_food_code_2)
    add_next_button("양쪽 선택 다 해봤어요.",show_food_feeling)
#---------------------------------
# 10. 실행 후 느낌
#---------------------------------
def show_food_feeling():
    clear_screen()
    add_title("서로 다른 선택과 서로 다른 결과가 나타나죠?")

    add_message("내가 선택한 'y'와 'n'에 따라서\n"
    "서로 다른 답변이 나오는 것을 직접 보셨죠?\n\n"
    "어떤 생각과 느낌이 떠 오르나요?\n\n"

    "지금 이 동굴 탐사를 계속 할까요?\n\n"
    "마음 속으로 다시 한번 선택에 의한 결과를 음미해 보세요.\n\n")
    add_previous_button("이전",show_food_run)
    add_next_button("동굴 안으로 더 나아가 볼까요?",show_door)
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
    add_title("동굴의 질문에 답하세요.")
    add_message("이 문을 열 수 있는 키는 동굴의 질문에\n"
    "'네 / 아니요'로 바른 선택을 하는 겁니다.\n\n"
    "쉬잇! 조용히 들어보세요.\n"  
    "동굴이 질문하네요.\n\n"

    "Python이 스스로 코드를 만들어서 \n"
    "직접 작업할 수 있나요?\n\n"
    "먼저 마음 속으로 '네' 또는 '아니요'를 선택해 보세요.\n\n")
    add_previous_button("이전",show_door)
    add_next_button("선택했어요",show_door_code)
#-----------------------------------
# 13. 첫 번째 동굴 문 통과 선택 코드
#----------------------------------
def show_door_code():
    clear_screen()
    add_title("이번에는 코드 작업을 통해서 문을 열어봅시다.\n\n")
    add_message("'vs code' 위쪽 작업장에서 아래와 같이 코드 입력하세요.\n\n"
    'answer=input("Python이 스스로 코드를 만들어서 직접 작업할 수 있나요?(y/n):")\n\n'
    'if answer == "n":\n'
    'print("철컥! 문이 열렸습니다.")\n'
    'else:\n'
    'print("지나왔던 길들을 다시 한번 살펴보세요.")\n\n'
    "꼼꼼하게 확인하셨으면 'Ctrl + S' 를 눌러 꼭 저장합니다.\n\n"
    "저장 후 아래쪽 터미널에서 'python choice.py' 쓰고 'Enter'로 실행하세요.\n\n")
    add_previous_button("이전",show_door_question)
    add_next_button("실행해볼게요",show_door_result)
#--------------------------------------
# 14. 실제 선택
#--------------------------------------
def show_door_result():
    clear_screen()
    add_title("드디어 동굴 문이 열렸나요?")
    add_message("직접 실행해 보셨죠?\n\n"
    "'n'을 선택했다면 문이 열렸을 겁니다.\n\n"
    "그런데 만약 'y'를 선택했다면 \n"
    "동굴 문이 안 열릴 겁니다.\n\n"

    "왜 동굴 문이 그렇게 침묵하고 안 열어 준건지\n"
    "지나왔던 길을 다시 살펴보세요.\n\n"
    "바로 그 길에서 곰곰 생각하고 다시 한번 질문에 도전해 보세요.\n\n")
    add_previous_button("이전",show_door_code)
    add_next_button("문을 통과했어요",show_history)
#----------------------------------------
# 15. 탐사 기록 
#----------------------------------------
def show_history():
    clear_screen()
    add_title("우리 탐사 기록을 남겨 볼까요?")
    add_message("어떤 도구들을 어떻게 사용하며 여기까지 왔는지 깜빡깜빡하죠?.\n\n"
    "그래서 탐사 기록을 하면서 참고로 하시는게 도움될 겁니다.\n\n"

    "먼저 'VS Code'에서 새 파일을 하나 만들고\n"
    "'history.txt'라는 '새 파일 이름'을 만들어 줍니다.\n\n"
    "기억이 잘 안나면 지나왔던 '지금 밥 먹을까요?'제목의 컷을 참고하세요.\n\n"

    "이 파일은 탐사하며 직접 경험하며 생각하고\n"
    "느껴지는 것들의 짧은 요약 노트입니다.\n\n"
    "탐사 시간이 길어질수록 우리의 생각과 느낌이 경험따라 쌓여갈 겁니다.\n\n")
    add_previous_button("이전",show_door_result)
    add_next_button("계속 기록해 볼게요",show_history_write)
#---------------------------------------------
# 16. 탐사 기록 작성
#---------------------------------------------
def show_history_write():
    clear_screen()
    add_title("기억나는 순서대로 적어 보세요")
    add_message("준비단계부터 지금 여기까지 오면서 경험했던 과정들을\n"
    "영화를 보듯 하나의 흐름으로 연상해 봅니다.\n\n"
    "도구들을 찾아 장착하고 어떻게 사용 방법을 익혔는지 기억해 보세요.\n\n"
    "동굴과 소통했던 순간들 느낌과 떠오르는 생각같은 것들입니다.\n\n"
    "흐름을 따라서 기억나는 순서대로 짧게 요약해 쓰면 됩니다.\n\n"
    "엄마의 느낌도 한 문장으로 요약해 두면 좋은 경험과 추억이 될겁니다.\n\n"
    "일기쓰듯이 날짜 쓰지 마시고 가능한 탐사 과정 흐름에 따라서\n"
    "순간들 생각과 느낌을 그때그때 요약 기록해 두세요.\n\n")
    add_previous_button("이전",show_history)
    add_next_button("계속 기록 할게요",show_second_door)
#-----------------------------------------------
# 17. 두번째 동굴의 문
#---------------------------------------------
def show_second_door():
    clear_screen()
    add_title("또 한번 더 동굴의 문이 나왔네요!")


    add_message("저번 것보다 더 단단하게\n"
    "이중으로 잠겨 있네요.\n\n"
    "이번에는 동굴이 두가지 질문을 합니다.\n\n"
    "마음 단단히 먹고 신중하게 미리 생각해 선택해 보세요.\n\n")
    add_previous_button("이전",show_history_write)
    add_next_button("첫 번째 질문",show_second_question_1)
#-----------------------------------------------
# 18. 동굴 문의 첫 번째 질문
#---------------------------------------------
def show_second_question_1():
    clear_screen()
    add_title("첫 번째 질문 선택하세요")

    add_message("지금까지 우리는 두 갈래 길 중\n"
    "하나를 선택하며 여기까지 왔습니다.\n\n"

    "그런데 동굴은 두 갈래길보다 많으면 어떻게 할건지,\n"
    "코드로 둘 이외의 다른 선택도 할 수 있느냐고 질문하네요.\n\n"

    "'네 / 아니요' 둘 중 하나로 답하래요.\n\n"
    "필요하면 '휴대폰AI'에게도 물어보고 엄마와 상의해 미리 방향을 정하세요.\n\n")
    add_previous_button("이전",show_second_door)
    add_next_button("결정했어요",show_second_question_2)
#-----------------------------------------------
# 19. 동굴 문의 두 번째 질문
#----------------------------------------------
def show_second_question_2():
    clear_screen()
    add_title("두 번째 질문 선택하세요")
    add_message("지금까지 동굴은 우리가 코드로\n"
    "미리 입력해 놓은 규칙으로만 말을 했습니다.\n\n"

    "그런데 동굴은 이렇게 미리 정해진 것도 좋지만,\n"
    "그 이외의 다른 말들도 사람들처럼 당신들과 소통하고 싶다네요.\n\n"

    "가능하다면 '네', 가능하지 않다면 '아니요'라고 답하래요.\n\n"
    "이번에도 첫 질문처럼 상의해서 미리 방향을 정하세요.\n\n")
    add_previous_button("이전",show_second_question_1)
    add_next_button("방향 결정 했어요",show_second_code_1)
#----------------------------------------------
# 20. 첫 번째 동굴 질문 코딩
#----------------------------------------------
def show_second_code_1():
    clear_screen()
    add_title("첫 번째 질문 상황을 코드로 만들어 봅시다.")
    add_message("VS Code 위쪽 코드 작업 공간에 아래처럼 입력합니다.\n\n"
                
    'path=input("코딩에서도 두 갈래 이외의 다른 길이 있을까요?(y/n):")\n\n'
    'if path =="y":\n'
    'print("철커덕! 첫 번째 잠금이 풀렸습니다.")\n'

    'else:\n'
    'print("휴대폰 AI에게도 물어 보며 엄마와도 상의해 보세요.")\n\n'
    "다 입력하고 꼼꼼하게 확인했으면 Ctrl+S로 꼭 저장부터 하세요.\n\n")
    add_previous_button("이전",show_second_question_2)
    add_next_button("저장했어요.", show_second_code_2)
#-------------------------------------------
# 21. 두 번째 동굴 질문 코딩
#--------------------------------------------
def show_second_code_2():
    clear_screen()
    add_title("두 번째 질문 상황도 코드로 만들어 봅시다.")

    add_message("첫 번째 질문 상황 코딩에 이어서 계속 합니다.\n\n"
                
    'talk = input("미리 정해 놓지 않은 말들도 동굴이 할 수 있을까요?(y/n):")\n\n'
    'if talk == "y":\n'
    'print("철커덕! 두 번째 잠금도 풀렸습니다.")\n'

    'else:\n'
    'print("다른 방법이있는지 찾아보면서 상의해 보세요.")\n\n'
    "입력 끝났으면 검토 확인하고 반드시 저장하세요.\n\n")
    add_previous_button("이전", show_second_code_1)
    add_next_button("확인하고 저장까지 했어요", show_second_run)
#--------------------------------------------
# 22. 두 번째 동굴 문 선택 실행
#-------------------------------------------
def show_second_run():
    clear_screen()
    add_title("두 개의 잠금을 풀고 동굴 문을 열어 볼까요?")

    add_message("VS Code 아래쪽 터미널에서\n"
    "반짝거리는 곳에 'python choice.py'를 쓰고 'Enter'로 실행해 봅니다.\n\n"

    "첫 번째 질문에 직접 답하고,\n"
    "두 번째 질문에도 직접 답해 보세요.\n\n"

    "여러 번 반복해 보면서 주어지는 조건들과\n"
    "이에따라서 선택하는 결과가 달라지는 이 구조를 깊이 기억해 두어야 합니다.\n\n")
    add_previous_button("이전", show_second_code_2)
    add_next_button("이 구조의 의미를 이해했어요.", show_second_result)
#--------------------------------------------
# 23. 두 번째 동굴 문 통과
#-------------------------------------------
def show_second_result():
    clear_screen()
    add_title("드디어 두 번째 문도 열렸습니다!")
    add_message("두 가지 질문들에 '네'라고 선택했으면\n"
    "두 개의 잠금이 모두 풀렸을 겁니다.\n\n"

    "그런데, 우리가 선택한 둘 사이에는 또다른 길들로\n"
    "갈 수있는 수많은 기회들이 있을 수 있잖아요?\n\n"

    "군대처럼 정해진 규칙에 따르는 것이 효율적이긴 하지만,\n"
    "그 이외에는 자유롭고 다양한 소통 방식들이 필요해야 하지 않을까요?\n\n")
    add_previous_button("이전", show_second_run)
    add_next_button("이어지는 동굴 탐사로",show_review_stage)
#---------------------------------------------
# 24. 두 갈래길 탐사 되돌아 보기
#---------------------------------------------
def show_review_stage():
    clear_screen()
    add_title("두 갈래길 경험과 이어지는 다음 동굴 탐사로")
    add_message("둘 중 하나라는 선택이 주는 의미와 구조가 쉽게 떠오르나요?\n\n"
    "둘이라는 양극단 사이에도 찾을수록 수많은 길들이 있지 않을까요?\n\n"

    "구조를 이해하며 계속 깊이 원인을 찾아가는 좋은 습관들이 나침반입니다.\n\n"
    "'history'에 요약 기록들이 쌓여가면 변화되어가는 자신의 습관도 느낄 수 있어요.\n\n"
    
    "앞으로 이어지는 동굴 탐사에서\n"
    "자유롭고 다양한 소통까지 할 수있게 동굴에게 방법 찾아줍시다.\n\n"
    "그래서 엄마와 함께 동굴의 협조로 미래로 통하는 여정을 성공적으로 끝내세요.\n\n"
    "지금 이 순간 느껴지는 생각과 느낌을 꼭 'history'에 남기세요.\n\n"
    "엄마도 엄마의 생각과 느낌을 남겨주시면 도움되지 않을까요?\n\n")
    add_previous_button("이전",show_second_result)

show_cover()
root.mainloop()     