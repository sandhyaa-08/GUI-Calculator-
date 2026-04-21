from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="black")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def calculate():
    global equation
    try:
        result = str(eval(equation))
        label_result.config(text=result)
        equation = result
    except:
        label_result.config(text="Error")
        equation = ""

def erase():
    global equation
    equation = equation[:-1]   # last character remove
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text="")

frame = Frame(root, bg="#030303")
frame.place(relx=0.5, rely=0.5, anchor="center")


label_result = Label(frame, width=14, height=2, font=("Arial", 28, "bold"),
                     bg="#2a2d36", fg="white", anchor="e")
label_result.grid(row=0, column=0, columnspan=4, pady=10)

btn_style = {"width": 5, "height": 2, "font": ("Arial", 16, "bold"), "bd": 0}

# Row 1
Button(frame, text="⌫", bg="#2a2d36", fg="#fc7474",command=erase, **btn_style).grid(row=1, column=0, padx=5, pady=5)

Button(frame, text="AC", bg="#2a2d36", fg="#fc7474", command=clear, **btn_style).grid(row=1, column=1, padx=5, pady=5)
Button(frame, text="%", bg="#2a2d36", fg="white", command=lambda: show("%"), **btn_style).grid(row=1, column=2, padx=5, pady=5)
Button(frame, text="/", bg="#fc7474", fg="white", command=lambda: show("/"), **btn_style).grid(row=1, column=3, padx=5, pady=5)


Button(frame, text="7", bg="#2a2d36", fg="white", command=lambda: show("7"), **btn_style).grid(row=2, column=0, padx=5, pady=5)
Button(frame, text="8", bg="#2a2d36", fg="white", command=lambda: show("8"), **btn_style).grid(row=2, column=1, padx=5, pady=5)
Button(frame, text="9", bg="#2a2d36", fg="white", command=lambda: show("9"), **btn_style).grid(row=2, column=2, padx=5, pady=5)
Button(frame, text="*", bg="#fc7474", fg="white", command=lambda: show("*"), **btn_style).grid(row=2, column=3, padx=5, pady=5)


Button(frame, text="4", bg="#2a2d36", fg="white", command=lambda: show("4"), **btn_style).grid(row=3, column=0, padx=5, pady=5)
Button(frame, text="5", bg="#2a2d36", fg="white", command=lambda: show("5"), **btn_style).grid(row=3, column=1, padx=5, pady=5)
Button(frame, text="6", bg="#2a2d36", fg="white", command=lambda: show("6"), **btn_style).grid(row=3, column=2, padx=5, pady=5)
Button(frame, text="+", bg="#fc7474", fg="white", command=lambda: show("+"), **btn_style).grid(row=3, column=3, padx=5, pady=5)


Button(frame, text="1", bg="#2a2d36", fg="white", command=lambda: show("1"), **btn_style).grid(row=4, column=0, padx=5, pady=5)
Button(frame, text="2", bg="#2a2d36", fg="white", command=lambda: show("2"), **btn_style).grid(row=4, column=1, padx=5, pady=5)
Button(frame, text="3", bg="#2a2d36", fg="white", command=lambda: show("3"), **btn_style).grid(row=4, column=2, padx=5, pady=5)
Button(frame, text="-", bg="#fc7474", fg="white", command=lambda: show("-"), **btn_style).grid(row=4, column=3, padx=5, pady=5)


Button(frame, text="0", bg="#2a2d36", fg="white", command=lambda: show("0"), **btn_style).grid(row=5, column=0, columnspan=2, sticky="we", padx=5, pady=5)
Button(frame, text=".", bg="#2a2d36", fg="white", command=lambda: show("."), **btn_style).grid(row=5, column=2, padx=5, pady=5)
Button(frame, text="=", bg="#fc7474", fg="white", command=calculate, **btn_style).grid(row=5, column=3, sticky="ns", padx=5, pady=5)


root.mainloop()
