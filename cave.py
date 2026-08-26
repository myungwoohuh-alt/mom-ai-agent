import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("동굴 탐사")
root.geometry("900x600")
image = Image.open("cave_entrance.png")
image = image.resize((900,600))
bg = ImageTk.PhotoImage(image)
label = tk.Label(root,image=bg)
label.pack()
check_text=tk.Label(root,text="들어가기 전에, 준비물 한번 확인해 볼까요?")
check_text.place(x=30,y=30)
computer = tk.Checkbutton(root,text="사용할 노트북이나 컴퓨터 있어요?")
computer.place(x=30,y=60)
internet = tk.Checkbutton(root,text="인터넷 연결되죠?")
internet.place(x=30,y=90)
chatgpt = tk.Checkbutton(root,text="휴대폰으로 ChatGpt 사용할 수 있죠?")
chatgpt.place(x=30,y=120)
def enter_cave():
    global bg
    check_text.destroy()
    computer.destroy()
    internet.destroy()
    chatgpt.destroy()
    ready.destroy()
    inside_image = Image.open("cave_inside.png")
    inside_image.resize((900,600))
    bg = ImageTk.PhotoImage(inside_image)
    label.config(image=bg)

    tool_text = tk.Label(root,text="이 동굴과 만나려면 인터넷 연결이 필요해. \n\n" 
    "그럼 인터넷에서 만나려면 어떤 도구가 필요할까?\n\n"
    "그게 바로 브라우저야."
    "아까 준비물 확인 때 Chrome 봤지?\n"
    "Chrome이 브라우저 중 하나야.\n\n"
    "여기서도 잘 연결되나 한 번 실행해 보자!",
    font=("Arial", 12),
    justify="left")
    tool_text.place(x=30,y=30)
ready=tk.Button(root,text="준비완료. 들어갑시다.",command=enter_cave)
ready.place(x=30,y=160)
root.mainloop()