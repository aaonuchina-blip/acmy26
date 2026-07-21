from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb
import requests
import json


def exchange_get():
    url = 'https://www.coingecko.com'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(data)

def exchange_upd():
    pass

Cryptocurrency = {
    'Bitcoin': 'BTC',
    'Ethereum': 'ETH',
    'BNB': 'BNB ',
    'XRP': 'XRP',
    'Solana':'SOL',
    'TRON':'TRX',
    'Hyperliquid': 'HYPE',
    'Dogecoin': 'DOGE',
    'Cardano': 'ADA'
}



window = Tk()
window.title("Курс обмена криптовалют к доллару")
window.geometry("360x420")



lbl_result = Label(window, text="Нажмите кнопку для загрузки курса", font=("Arial", 12), justify=LEFT)
lbl_result.pack(padx=10, pady=20)

button = Button(window, text="Обновить курс валют", command=exchange_get)
button.pack(padx=10, pady=10)

window.mainloop()
