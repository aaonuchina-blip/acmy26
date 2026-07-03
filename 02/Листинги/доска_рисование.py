import tkinter as tk
from tkinter import *
from tkinter import colorchooser

def save_canvas():
    file_path = fd.asksaveasfilename(defaultextension='.png', filetypes=[('PNGfiles', '*.png')])
    if file_path: # Проверяем, был ли указан путь для сохранения
        x = window.winfo_rootx() + canvas.winfo_x()
        y = window.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
        mb.showinfo("Сохранено!", "Изображение успешно сохранено.")



def setcolor(event):
    global color
    color0, color1 = colorchooser.askcolor(initialcolor="#000000")
    color = color1

def savePosn(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    canvas.create_line((lastx, lasty, event.x, event.y), fill=color)
    savePosn(event)

def moveline(event):
    canvas.move(line1, 200, 0)


prog = Tk()
color = "black"
canvas = Canvas(prog, width=500, height=500, background= 'white' )
canvas.grid(column=0, row=0)


btn = tk.Button(text='Выбрать цвет')
btn.grid(column=1, row=0)
btn.bind("<Button-1>", setcolor)

canvas.bind("<Button-1>", savePosn)
canvas.bind("<B1-Motion>", addLine)

canvas.create_polygon(150, 200, 250, 100, 350, 200, fill = 'orange')
canvas.create_rectangle(150, 200, 350, 400, fill='blue', outline = 'grey')
line1 = canvas.create_line(150, 300, 350, 300, width=2)

btm = tk.Button(text="Передвинуть")
btm.grid(column=0, row=1)
btm.bind("<Button-1>", moveline)

Button(window, text="Сохранить холст", command=save_canvas).pack()
canvas.mainloop()