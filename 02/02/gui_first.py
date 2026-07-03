from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg

def start():
    global alarm_time
    alarm_time = alarm.get().strip() #считываем символы из виджета Entry alarm
    messagebox.showinfo('Предупржедение',
                        f'Будильник установлен на {alarm_time}')

def stop():
    global alarm_time
    alarm_time = ''
    alarm.delete(0, END)
    pg.mixer.music.stop()
    messagebox.showinfo('Предупреждение', 'Будильник отключен')


def tick():
    global alarm_time
    curr_time = strftime('%H:%M:%S') #текущее время в строковом
    if alarm_time == curr_time or alarm_time == strftime('%H:%M') or alarm_time == strftime('%H'):
        alarm_time = ''
        pg.mixer.music.play()
    current_time.config(text=curr_time) # меем значение Label на текущее
    current_time.after(1000,tick) #вызывает tick один раз в секунду


pg.mixer.init() #подключение библиотеку pgame
pg.mixer.music.load('alarm-clock.mp3') #загрузка мелодии
pg.mixer.music.set_volume(.5) #установка грмкости

root = Tk() #создаем окно
WIDTH = root.winfo_screenwidth() #получаем ширину монитора в пикселях
HEIGHT = root.winfo_screenheight() #получаем высоту монитора в пикселях
# print(WIDTH, HEIGHT)
X = 450 #задаем ширину окна root
Y = 250 # начало координат левый верхний угол экрана
# root.geometry('450x250+400+200') #задали размер окна и его размещение на экране
root.geometry(f'{X}x{Y}+{WIDTH // 2 - X // 2-400}+'
              f'{HEIGHT // 2 - Y // 2 -300}') #адаптивное размещение окна root  в центре экрана на любом мониторе
current_time = Label(root, text = '00:00:00')
# current_time.pack(side=TOP) #по умолчанию вверху текст размещвется в окне LEFT RIGHT TOP BOTTOM
root.title('Будильник')
root.config(bg ='black')
current_time.config(font=('Arial', 50), fg='lime', bg= 'black')
current_time.pack()
alarm = Entry(root, )
alarm.cofnig(width=10, justify='center', font=('Arial', 20))
alarm.pack()

start_btn = Button(root)
start_btn.config(width=10, text='Включить', justify ='center',
             font=('Arial', 11), command = start)
start_btn.pack(pady=10)

stop_btn = Button(root)
stop_btn.config(width=10, text='Вылючить', justify ='center',
            font=('Arial', 11), command=stop)
stop_btn.pack()
alarm_time = ''

tick()
root.mainloop()