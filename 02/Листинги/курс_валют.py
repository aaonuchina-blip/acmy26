import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

from requests.packages import target


def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text = name)

def exchange():
    target_code =target_combobox.get()
    base_code = base_combobox.get()

    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()

            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base = currencies[base_code]
                target = currencies[target_code]
                currency_name = currencies[code]
                mb.showinfo("Курс обмена", f"Курс  {exchange_rate:.lf}{target} за 1 {base}")
            else:
                mb.showerror("Ошибка",f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f'Ошибка {e}')

        else:
            mb.showwarning("Внимание", "Выберите коды валют")


currencies = {
    'EUR':"Евро",
    'JPY':"Японская йена",
    'GBP':"Британский фунт стерлингов",
    'AUD':"Австралийский доллар",
    'CAD':"Канадский доллар",
    'CHF':"Швейцарский франк",
    'CNY':"Китайский юань",
    'RUB':"Российский рубль",
    'KZT':"Казахстанскй тенге",
    'UZS':"Узбекский сум"
}
window = Tk()
window.title('Курс обмена валюты к доллару')
window.geometry('360x180')

Label(text="Базовая валюта: ").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)

Label(text='Целевая валюта: ').pack(pady=5, padx=10)
target_combobox=ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(pady=10, padx=10)

window.mainloop()


# p = pprint.PrettyPrinter(indent=4)
# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)

# print(data)
