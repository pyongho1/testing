from tkinter import *

root = Tk()
root.title("Yong GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# Menu Frame
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheese burger").pack()
Button(frame_burger, text="Chicken burger").pack()

# Drink Frame
frame_drink = LabelFrame(root, text="Drinks")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Sprite").pack()


root.mainloop()  # 창이 닫히지 않게
