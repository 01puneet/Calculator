from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("500x550")
root.wm_iconbitmap("")
root.title("Calculator by Codemounts")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=5, pady=8, padx=8)

frame1 = Frame(root, bg="#1B4F72")
b = Button(frame1, text="7", font="lucida 25 bold",
           bg="silver", padx=10, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame1, text="8", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame1, text="9", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame1, text="+", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)
frame1.pack()

frame2 = Frame(root, bg="#1B4F72")
b = Button(frame2, text="4", font="lucida 25 bold",
           bg="silver", padx=14, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame2, text="5", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame2, text="6", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame2, text="-", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)
frame2.pack()

frame3 = Frame(root, bg="#1B4F72")
b = Button(frame3, text="1", font="lucida 25 bold",
           bg="silver", padx=13, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame3, text="2", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame3, text="3", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame3, text="*", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)
frame3.pack()

frame4 = Frame(root, bg="#1B4F72")
b = Button(frame4, text="C", font="lucida 25 bold",
           bg="silver", padx=11.5, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame4, text="0", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(frame4, text="=", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)
b = Button(frame4, text="/", font="lucida 25 bold",
           bg="silver", padx=15, pady=10)
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)
frame4.pack()
root.mainloop()
