from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image, ImageTk, ImageGrab
from pygame.display import update

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x + 5, y + 5, fill=pen_color, outline=pen_color, width=width_pen)


def save_width():
    try:
        width_pen_new = int(n.get().strip())
        globals().update(width_pen=width_pen_new)
    except ValueError as e:
        mb.showerror("Ошибка", f'Укажите целое число')


def load_image():
    try:
        file_path = fd.askopenfilename(filetypes=[('Image files',
                                                   '*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if file_path:
            image = Image.open(file_path)
            image = image.resize((600, 400))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        mb.showerror('Ошибка', f"Не удалось загрузить: {e}")


def save_canvas():
    try:
        file_path = fd.asksaveasfilename(defaultextension='.png',
                                         filetypes=[('PNG files', '*.png')])
        if file_path:
            x = window.winfo_rootx()
            y = window.winfo_rooty()
            x1 = x + 600
            y1 = y + 400
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)
            mb.showinfo("Сохранено!", "Изображение успешно сохранено в PNG файл!")
    except Exception as e:
        mb.showerror("Ошибка", f'Не удалось сохранить: {e}')


def quit():
    window.destroy()


window = Tk()
window.title("Рисование на холсте")

pen_color = "red"
width_pen = 1
canvas = Canvas(window, width=600, height=400)

canvas.pack()
canvas.bind("<B1-Motion>", draw)
colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: globals().update(pen_color=c))

lbl1 = Label(window, text="Толщина линии: ", width=15, height=2)
lbl1.pack(side=LEFT)

n = Entry(window, width=5)
n.pack(side=LEFT)
width_btn = Button(window, text="Установить толщину", command=save_width)
width_btn.pack(side=LEFT, padx=10)

menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить изображение", command=load_image)
file_menu.add_command(label="Сохранить холст", command=save_canvas)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit)

window.mainloop()