from tkinter import *
from pygame.display import message_box


def summa():
    num1 = int(n1.get().strip())
    num2 = int(n2.get().strip())
    num3 = int(n3.get().strip())
    res_sum = num1 + num2 + num3
    message_box('Ответ', f'{res_sum}')


def multi():
    num1 = int(n1.get().strip())
    num2 = int(n2.get().strip())
    num3 = int(n3.get().strip())
    res_multi = num1 * num2 * num3
    message_box('Ответ', f'{res_multi}')



root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

X = 450 #задаем ширину окна root
Y = 250 # начало координат левый верхний угол экрана

root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2-400}+'
              f'{HEIGHT // 2 - Y // 2 -300}') #адаптивное размещение окна root  в центре экрана на любом мониторе

root.title('Калькулятор')

n1 = Entry(root)
n1.config(width=20, justify='center', font=('Arial', 15))
n1.pack()

n2 = Entry(root)
n2.config(width=20, justify='center', font=('Arial', 15))
n2.pack()

n3 = Entry(root)
n3.config(width=20, justify='center', font=('Arial', 15))
n3.pack()

summa_btn = Button(root)
summa_btn.config(width=20, text='Сложить три числа', justify ='center',
             font=('Arial', 11), command = summa)
summa_btn.pack(pady=5)

multi_btn = Button(root)
multi_btn.config(width=20, text='Умножить три числа', justify ='center',
             font=('Arial', 11), command = multi)
multi_btn.pack()
num1 = ''
num2 = ''
num3 = ''

root.mainloop()