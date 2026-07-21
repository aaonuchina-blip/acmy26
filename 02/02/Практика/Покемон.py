from http.client import responses
import requests #работает с запросами json
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import os


def prog_info():
    messagebox.showinfo('О программе',
                        "Просмотр Покемонов\n Сайт https://pokeapi.co/\n Tkinter + API ")


def get_pokemon_data(number):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'  # Получаем адрес
    responce = requests.get(url)
    responce.raise_for_status()
    return responce.json()


def load_image(url):
    responce = requests.get(url)
    responce.raise_for_status()
    img = Image.open(BytesIO(responce.content))
    img.thumbnail((250, 250))
    return ImageTk.PhotoImage(img)


def get_pokemon():
    try:
        number = pokemon_spin.get() #Получаем номер из спинбокса
        data = get_pokemon_data(number) #Получаем json
        # print(data['sprites']['other']['official-artwork']['front_default'])
        img_url = data['sprites']['other']['official-artwork']['front_default'] #ссылка на изображение

        photo = load_image(img_url)
        top = tk.Toplevel(root)
        top.title(data['name'].capitalize())
        top.geometry('320x450')

        l_img = ttk.Label(top,image=photo)
        l_img.image = photo
        l_img.pack(pady=10)
        info = f"""
            Имя: {data['name'].capitalize()}
            Рост: {data['height']}
            Вес: {data['weight']}
            Опыт: {data['base_experience']}
"""
        l_info = ttk.Label(top, text=info, font = 'Arial 16', justify=LEFT)
        l_info.pack(pady=5)
    except Exception as err:
        messagebox.showerror('Ошибка', f'Ошибка запроса API {err}')
    finally:
        progress.stop()
        button.config(state=tk.NORMAL)

def start_loading():
    button.config(state=tk.DISABLED)
    progress.start(10)
    root.after(1000, get_pokemon)

def end_prog():
    root.destroy()

root = Tk()
root.geometry('450x300')
root.title('Покемоны')

label = ttk.Label(root, text= "Номер покемона")
label.pack(pady=10)

pokemon_spin= ttk.Spinbox(from_=1, to=1000, width=5)
pokemon_spin.set(1)
pokemon_spin.pack(pady=10)

button = ttk.Button(text='Загрузить покемона', command=start_loading)
button.pack(padx=10,pady=10)

progress = ttk.Progressbar(mode='indeterminate', length=300)
progress.pack(padx=10,pady=10)

mainmenu = Menu(root)
root.config(menu=mainmenu)
filemenu = Menu(mainmenu, tearoff=0)
filemenu2 = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Загрузить", command=start_loading)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=end_prog)
filemenu2.add_command(label="О программе", command=prog_info)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=filemenu2)


root.mainloop()

