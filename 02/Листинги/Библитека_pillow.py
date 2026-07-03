# Просмотр изображений
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

def quit():
    window.destroy()

def open_image():
    try:
        file = fd.askopenfilename()
        if file: # Проверяем, был ли выбран файл
            img = Image.open(file)
            imgconv = img

# Адаптируем размер изображения под размер окна
        window_width = 500
        window_height = 500
        img.thumbnail((window_width, window_height))

        imgtk = ImageTk.PhotoImage(img)

    # Обновляем изображение на метке
        l.configure(image=imgtk)
        l.image = imgtk # Сохраняем ссылку на изображение

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден")
    except OSError: messagebox.showerror("Ошибка", "Не удалось открыть файл, возможно, это не изображение")
    except Exception as e:\
        messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

window = Tk()
window.title("PHOTO")
window.geometry("500x500")
mainmenu = Menu(window)
window.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=open)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=quit)
mainmenu.add_cascade(label="Файл", menu=filemenu)
window.mainloop()