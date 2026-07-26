import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import os

crypto_data = []
titles = []

def prog_info():
    messagebox.showinfo('О программе',
                        "Просмотр популярных криптовалют с ресурса\n https://www.coingecko.com/\n Tkinter + API ")

def find_curr():
    global crypto_data, titles
    # url = "https://coingecko.com"
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20Tether%2C%20usdt%2C%20tron%2C%20bnb%2C%20solana%2C%20whitebit%2C%20xrp%2C%20Hyperliquid%2C%20&names=Bitcoin&symbols=btc&include_tokens=all'
    headers ={'x-cg-pro-api-key: CG-Cs2CGnxLfiTEhkNccfmP4b35'}

    try:
        response = requests.get(url)
        response.raise_for_status()
        crypto_data = response.json()

        titles = [f"{coin['name']} ({coin['symbol'].upper()})" for coin in crypto_data]
        combo["values"] = titles
        combo.current(0)
        show_prod(None)
        messagebox.showinfo("Успех", "Данные о криптовалютах успешно обновлены!")
    except Exception as e:
        messagebox.showerror(
            "Ошибка", f"Не удалось загрузить данные.\nПроверьте API-ключ или сеть.\n{e}"
        )

def show_prod(event):
    selected_index = combo.current()
    if selected_index == -1:
        return
    coin = crypto_data[selected_index]

    info_text = (
        f"Название: {coin['name']}\n"
        f"Текущая цена: ${coin['current_price']:,}\n"
    )
    label.config(text=info_text)

    try:
        img_response = requests.get(coin["image"])
        img_data = img_response.content
        img_stream = BytesIO(img_data)
        img = Image.open(img_stream)
        img = img.resize((150, 150), Image.Resampling.LANCZOS)

        l_img.image = ImageTk.PhotoImage(img)
        l_img.config(image=l_img.image)
    except Exception:
        l_img.config(image="", text="[Нет иконки]")

root = Tk()
root.geometry('400x400')
root.title('Курс криптовалют')
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu2 = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Выход", command=root.destroy)
filemenu2.add_command(label="О программе", command=prog_info)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=filemenu2)

combo = ttk.Combobox(root, width=50, values=titles, state="readonly")
combo.pack(padx=10, pady=15)
combo.bind("<<ComboboxSelected>>", show_prod)

label = ttk.Label(root, font=('Arial', 15, 'bold'), justify=CENTER)
label.pack(pady=10)
l_img = ttk.Label(root)
l_img.pack(pady=10)
b_enter= Button(root, text='Загрузить/обновить криптовалюты', command=find_curr)
b_enter.pack(pady=10)

root.mainloop()