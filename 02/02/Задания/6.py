import requests
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
                        "Просмотр популярных криптовалют с ресурса\n https://www.coingecko.com/\n Tkinter + API ")

def find_curr():

    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20Tether%2C%20usdt%2C%20tron%2C%20bnb%2C%20solana%2C%20whitebit%2C%20xrp%2C%20Hyperliquid%2C%20&names=Bitcoin&symbols=btc&include_tokens=all'
    headers ={'x-cg-pro-api-key: CG-Cs2CGnxLfiTEhkNccfmP4b35'}

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()




root = Tk()
root.geometry('700x600')
root.title('Курс криптовалют')
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu2 = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Выход", command=root.destroy)
filemenu2.add_command(label="О программе", command=prog_info)

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=filemenu2)
combo = ttk.Combobox(root, width=50, values=titles)
combo.pack(padx=10, pady=5)
combo.bind("<<ComboboxSelected>>", show_prod)


label = ttk.Label(root, font=('Arial', 10, 'bold'), justify=CENTER)
label.pack(pady=10)
l_img = ttk.Label(root)
l_img.pack(pady=10)

b_enter= Button(root, text='Загрузить криптовалюту', command=find_curr)
b_enter.pack(pady=10)



root.mainloop()