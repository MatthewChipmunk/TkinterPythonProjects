from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Temperature converter')
e = ['Fahrenheit', 'Celsius']


def conv():
    if n.get() == '':
        messagebox.showinfo('Error', 'Please insert a number')
    else:
        new = Toplevel(root)
        if temp.get() == 'Celsius':

            x = (9 / 5 * int(n.get())) + 32
            Label(new, text=n.get() + " " + temp.get() + " is " + str(x) + " Fahrenheit").pack()

        else:
            x = 5/9*(int(n.get())-32)
            Label(new, text=n.get() + " " + temp.get() + " is " + str(x) + " Celsius").pack()


temp = StringVar()
n = StringVar()
temp.set(e[0])
Entry(root, textvariable=n).grid(row=0, column=0)
OptionMenu(root, temp, *e).grid(row=0, column=1)
Button(root, text='Convert', command=conv).grid(row=1, column=0)

root.mainloop()
