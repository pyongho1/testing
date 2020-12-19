from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Yong GUI")
root.geometry("640x480")

def btncmd():
    print(name.get())
    print(combobox.get())

nameLabel = Label(root, text="INSERT YOUR NAME BELOW")
nameLabel.pack()
name = Entry(root, width=30)
name.pack()

values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 32 까지의 숫자
combobox = ttk.Combobox(root, height=10, values=values)
combobox.pack()
combobox.set("SELECT THE DAY")  # 최초 목록 제목 설정

submit = Button(root, padx=10, pady=5, text="SUBMIT", command=btncmd)
submit.pack()

root.resizable(False, False)  # X and Y 값 변경불가

root.mainloop()  # 창이 닫히지 않게
