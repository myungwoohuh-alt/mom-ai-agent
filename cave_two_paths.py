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
    # 첫 표지
    # --------------------



    root.mainloop()     