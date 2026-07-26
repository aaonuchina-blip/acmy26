import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageTk
from io import BytesIO
import os

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20Tether%2C%20usdt%2C%20tron%2C%20bnb%2C%20solana%2C%20whitebit%2C%20xrp%2C%20Hyperliquid%2C%20&names=Bitcoin&symbols=btc&include_tokens=all' \

headers ={'x-cg-pro-api-key: CG-Cs2CGnxLfiTEhkNccfmP4b35'}

response = requests.get(url)
response.raise_for_status()
data = response.json()

print(data)
