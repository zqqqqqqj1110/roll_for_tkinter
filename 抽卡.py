import random
import tkinter

#随机数100以内，10抽保底

window = tkinter.Tk()
window.title("抽卡界面")
window.geometry("1500x500")

count = 0
def guess():
    global count,l
    x = random.randint(1, 100)
    if x <= (5 + count):
        k = tkinter.Label(window, image = five)
        count = 0
        l = tkinter.Label(window,
                          text="恭喜！",
                          width=15,
                          height=2,
                          font=("Arial", 30),
                          )
        l.pack(side=tkinter.LEFT)
    elif x > 5 and x <= 15:
        k = tkinter.Label(window, image = four_1)
        count += 10
    elif x > 15 and x <= 25:
        k = tkinter.Label(window, image = four_2)
        count += 10
    elif x > 25 and x <= 35:
        k = tkinter.Label(window, image = four_3)
        count += 10
    else:
        k = tkinter.Label(window, image = three)
        count += 10
    k.pack(side=tkinter.LEFT)

five = tkinter.PhotoImage(file = "可莉.png")
four_1 = tkinter.PhotoImage(file = "班尼特.png")
four_2 = tkinter.PhotoImage(file = "行秋.png")
four_3 = tkinter.PhotoImage(file = "早柚.png")
three = tkinter.PhotoImage(file = "讨龙.png")


welcome = tkinter.Label(window,
             text = "欢迎！",
             bg = "yellow",
             width = 15,
             height = 2,
             font=("Arial", 30),
             )
welcome.pack()

b = tkinter.Button(window,
                   text = "开抽！",
                   width = 15,
                   height = 2,
                   font = ("Arial", 12),
                   command = guess,
                   )
b.pack()

window.mainloop()