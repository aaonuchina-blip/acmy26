from tkinter import *
import random
from tkinter import messagebox as mb
import time


def move_ball(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == "Up" and y1 > 0:
        canvas.move(ball, 0, -20)


def move_ball(event):
    key = event.keysym
    x1, y1, x2, y2 = canvas.coords(ball)
    if key == "Up" and y1 > 0:
        canvas.move(ball, 0, -20)
    elif key == "Down" and y2 < canvas.winfo_height():
        canvas.move(ball, 0, 20)
    elif key == "Left" and x1 > 0:
        canvas.move(ball, -20, 0)
    elif key == "Right" and x2 < canvas.winfo_width():
        canvas.move(ball, 20, 0)
    check_collision()

def check_collision():
    b = canvas.coords(ball)
    print(b)
    s = canvas.coords(square)
    print(s)
    if b[2] > s[0] and b[0] < s[2] and b[3] > s[1] and b[1] < s[3]:
        if b[0] < s[2]:
            print(f"b[0] < s[2] {b[0]} < {s[2]}")
        move_square()
        update_score()


def move_square():
    x1, y1 = (random.randint(0, 380),random.randint(0, 280))
    x2, y2 = x1 + 20, y1 + 20
    canvas.coords(square, x1, y1, x2, y2)


def update_score():
    global score, start_time
    score += 1
    score_label.config(text=f'Счет: {score}')
    if score >= 10:
        end_game()

def end_game():
    end_time = time.time()
    if end_time - start_time <= 30:
        mb.showinfo("Игра окончена", "Победа!")
    else:
        mb.showinfo("Игра окончена", "Время вышло!")
    if mb.askyesno("Игра окончена", "Хотите сыграть еще раз?"):
        start_game()
    else:
        window.destroy()

def start_game():
    global start_time, score
    score = 0
    score_label.config(text=f"Счет: {score}")
    start_time = time.time()
    move_square()

window = Tk()
window.title("Игра с шариком")
window.geometry("400x300")

canvas = Canvas(window, width=600, height=800)
canvas.pack()
score = 0
my_frame = Frame(window)
my_frame.pack(side='top',pady=20, padx=20)
score_label = Label(my_frame, text=f"Счет: {score}", font = ('Arial', 20, 'bold'))
score_label.pack(side="top", pady=10)

ball = canvas.create_oval(180, 180, 220, 220, fill="red")
square = canvas.create_rectangle(150, 150, 170, 170, fill="blue")




start_game()

window.bind("<KeyPress>", move_ball)
window.focus_set()

window.mainloop()