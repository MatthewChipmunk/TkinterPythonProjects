from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.configure(background="black")
inp = StringVar()
expression = ''


def clear():
    global expression
    expression = ''
    inp.set('')


def update(t):
    global expression
    expression += t
    inp.set(expression)


def evaluate(exp):
    global expression
    print(exp)
    try:
        expression = str(eval(expression))
        inp.set(expression)
    except:
        messagebox.showerror('Error')

# ===============================================================================
Entry(root, font=('arial', 20, 'bold'), textvariable=inp,
      bg="powder blue", justify='right', borderwidth=5).grid(columnspan=4)

Button(root, padx=10, pady=10, fg="grey", font=('arial', 20, 'bold'),
       text="C", command=clear).grid(row=1, column=0)

# ===============================================================================
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="7", bg="powder blue", command=lambda: update('7')).grid(row=2, column=0)

Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="8", bg="powder blue", command=lambda: update('8')).grid(row=2, column=1)

Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="9", bg="powder blue", command=lambda: update('9')).grid(row=2, column=2)

Button(root, padx=10, pady=10, fg="orange", font=('arial', 20, 'bold'),
       text="/", bg="powder blue", command=lambda: update('/')).grid(row=2, column=3)
# ===============================================================================
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="4", bg="powder blue", command=lambda: update('4')).grid(row=3, column=0)

Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="5", bg="powder blue", command=lambda: update('5')).grid(row=3, column=1)

Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="6", bg="powder blue", command=lambda: update('6')).grid(row=3, column=2)
Button(root, padx=10, pady=10, fg="orange", font=('arial', 20, 'bold'),
       text="*", bg="powder blue", command=lambda: update('*')).grid(row=3, column=3)
# ===============================================================================
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="1", bg="powder blue", command=lambda: update('1')).grid(row=4, column=0)
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="2", bg="powder blue", command=lambda: update('2')).grid(row=4, column=1)
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="3", bg="powder blue", command=lambda: update('3')).grid(row=4, column=2)
Button(root, padx=10, pady=10, fg="orange", font=('arial', 20, 'bold'),
       text="-", bg="powder blue", command=lambda: update('-')).grid(row=4, column=3)

# ===============================================================================
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text="0", bg="powder blue", command=lambda: update('0')).grid(row=5, column=0)
Button(root, padx=10, pady=10, fg="black", font=('arial', 20, 'bold'),
       text=".", bg="powder blue", command=lambda: update('.')).grid(row=5, column=1)
Button(root, padx=10, pady=10, fg="orange", font=('arial', 20, 'bold'),
       text="=", bg="powder blue", command=lambda: evaluate(expression)).grid(row=5, column=2)
Button(root, padx=10, pady=10, fg="orange", font=('arial', 20, 'bold'),
       text="+", bg="powder blue", command=lambda: update('+')).grid(row=5, column=3)

root.mainloop()
