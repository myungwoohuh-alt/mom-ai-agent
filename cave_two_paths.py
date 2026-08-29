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
    "지난 준비단계 탐사에서 직접 확인해 보세요.")
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
    "지난번처럼 동굴과 인사하며 소통되는지 확인해 보세요.")
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



show_cover()
root.mainloop()     