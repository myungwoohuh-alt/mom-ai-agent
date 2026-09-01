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
def add_title(text):
    title=tk.Label(root,text=text,
    font=("Arial",24,"bold"))
    title.pack(pady=30)
def add_next_button(text,command,y=480):
    button=tk.Button(root,text=text,
    font=("Arial",12),command=command)
    button.place(x=600,y=y)
def add_previous_button(text,command,y=480):
    button=tk.Button(root,text=text,
    font=("Arial",12),command=command)
    button.place(x=70,y=y)
def add_message(text):
    message=tk.Label(root,text=text,
    font=("Arial",14),justify="left")
    message.pack(pady=20)
#--------------------------------
# 1. 겉 표지
#--------------------------------
def show_cover():
    clear_screen()
    image=Image.open("water_path_cave.png")
    image=image.resize((900,600))
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(root,image=photo)
    label.image=photo
    label.place(x=0,y=0)
    add_next_button("Go!",show_review,y=530)
#-------------------------------
# 2. 지나왔던 "준비단계" 돌아보기
#-------------------------------
def show_review():
    clear_screen()
    add_title("지나오면서 장착한 도구들 점검 한번 해볼까요?")



show_cover()
root.mainloop() 