import time
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("Yong GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)  # 10ms 마다 움직임
# progressbar.pack()


# def btncmd():
#     progressbar.stop()  # 작동 중지


# btn = Button(root, text="Pause", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # 1 ~ 100
        time.sleep(0.01)  # 0.01초 대기

        p_var2.set(i)  # progress bar의 값 설정
        progressbar2.update()  # UI 업데잍트
        print(p_var2.get())


btn = Button(root, text="Start", command=btncmd2)
btn.pack()

root.mainloop()  # 창이 닫히지 않게
