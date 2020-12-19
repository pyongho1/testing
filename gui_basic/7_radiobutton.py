from tkinter import *

root = Tk()
root.title("Yong GUI")
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="Hamburger",
                          value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="Cheese Hamburger",
                          value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chicken Hamburger",
                          value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()


drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Cola", value="cola", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(
    root, text="Sprite", value="sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # 햄버거 중 선택된 라디오 항몫의 값 (value)
    print(drink_var.get())


btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop()  # 창이 닫히지 않게
