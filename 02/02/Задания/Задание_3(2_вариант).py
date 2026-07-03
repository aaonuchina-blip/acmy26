from tkinter import *
from tkinter import messagebox as mb


def summ():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return # Возвращаемся из функции, если ввод некорректен

    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return

    slag1 = int(s1)
    slag2 = int(s2)
    slag3 = int(s3)
    summa = slag1 + slag2 + slag3

    m1['text']= f"{s1} + {s2} + {s3}= {str(summa)}"
    answer = mb.askretrycancel(title="Вопрос", message="Посчитать еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text']= ""
    else:
        window.destroy()

def multi():
    s1 = e1.get()
    if not s1.lstrip('-').isdigit():
        mb.showerror("Ошибка", "В первое поле должно быть введено число")
        return

    s2 = e2.get()
    if not s2.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return
    s3 = e3.get()
    if not s3.lstrip('-').isdigit():
        mb.showerror("Ошибка", "Во второе поле должно быть введено число")
        return

    num1 = int(s1)
    num2 = int(s2)
    num3 = int(s3)
    mult = num1 * num2 * num3

    m1['text'] = f"{s1} * {s2} * {s3}= {str(mult)}"
    answer = mb.askretrycancel(title="Вопрос", message="Посчитать еще три числа?")
    if answer:
        e1.delete(0, END)
        e2.delete(0, END)
        m1['text'] = ""
    else:
        window.destroy()

window = Tk()
window.title("Калькулятор")
window.geometry('500x250')

m = Label(height=3, text="Введи три числа и нажми на кнопку для вычисления суммы или произведения")
m.pack()
e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()
e3 = Entry()
e3.pack()
b = Button(text="Сложить три числа",width=17, command=summ)
b.pack()
d = Button(text="Умножить три числа", width=17, command=multi)
d.pack()
m1 = Label(height=3)
m1.pack()
window.mainloop()