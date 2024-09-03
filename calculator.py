from tkinter import *

"""Initialize the main window"""
Calculator = Tk()
Calculator.title("Calculator")
Calculator.geometry("315x420")
Calculator.resizable(False, False)
Calculator.configure(bg="#17161b")

"""Variable to hold the expression"""
showvalue = StringVar()
showvalue.set("")

# Function to update the input field
def show(value):
    current_value = showvalue.get()
    if value == "=":
        try:
            """Evaluate the expression"""
            result = str(eval(current_value))
            showvalue.set(result)
        except Exception as e:
            """Show error message"""
            showvalue.set("Not Valid")
    else:
        """Append the value to the current input"""
        new_value = current_value + str(value)
        showvalue.set(new_value)

""" Function to clear the input field"""
def clear():
    showvalue.set("")

"""Entry widget for showing the input and result"""

Entry(Calculator, textvariable=showvalue, bg="#17161b", foreground="white", font="verdana 30 bold").pack(ipady=14)

"""Creating buttons and adding them to the window"""
Button(Calculator, text="AC", width=3, height=1, font=("verdana", 20, "bold"), bd="4", fg="black", bg="#40eff5", borderwidth=6,border=9, command=clear).place(x=2, y=80)
Button(Calculator, text="/", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="black", bg="#40eff5", borderwidth=6,border=9, command=lambda: show("/")).place(x=80, y=80)
Button(Calculator, text="%", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="black", bg="#40eff5", borderwidth=6,border=9, command=lambda: show('%')).place(x=158, y=80)
Button(Calculator, text="*", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#faae34", borderwidth=6,border=9, command=lambda: show('*')).place(x=238, y=80)

Button(Calculator, text="7", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(7)).place(x=2, y=148)
Button(Calculator, text="8", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(8)).place(x=80, y=148)
Button(Calculator, text="9", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(9)).place(x=158, y=148)
Button(Calculator, text="-", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#faae34", borderwidth=6,border=9, command=lambda: show("-")).place(x=238, y=148)

Button(Calculator, text="4", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(4)).place(x=2, y=216)
Button(Calculator, text="5", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(5)).place(x=80, y=216)
Button(Calculator, text="6", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(6)).place(x=158, y=216)
Button(Calculator, text="+", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#faae34", borderwidth=6,border=9, command=lambda: show('+')).place(x=238, y=216)

Button(Calculator, text="1", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(1)).place(x=2, y=284)
Button(Calculator, text="2", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(2)).place(x=80, y=284)
Button(Calculator, text="3", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(3)).place(x=158, y=284)
Button(Calculator, text="=", width=3, height=3, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#faae34", borderwidth=6,border=9, command=lambda: show('=')).place(x=238, y=284)

Button(Calculator, text="0", width=7, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6,border=9, command=lambda: show(0)).place(x=2, y=352)
Button(Calculator, text=".", width=3, height=1, font=("verdana", 20, "bold"), bd="1", fg="white", bg="#27282e", borderwidth=6, border=9,command=lambda: show('.')).place(x=158, y=352)

""" Run the main event loop"""
Calculator.mainloop()

















