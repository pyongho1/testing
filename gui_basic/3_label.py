from tkinter import *

root = Tk()
root.title("Yong GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

#photo = PhotoImage(file="gui_basic/img.png")
#label2 = Label(root, image=photo)
#label2.pack()


def change():
    label1.config(text="See you later")

    global photo2
    #photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="Click", command=change)
btn.pack()

root.mainloop()  # 창이 닫히지 않게
