

# => Code to show a Progress Bar
'''import math
import pandas_datareader as web
import colorama


def progress_bar(progress, total, color=colorama.Fore.LIGHTYELLOW_EX):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"{color}\r|{bar}| {percent:.2f}%", end="\r")
    if progress == total:
        print(f"{colorama.Fore.GREEN}\r|{bar}| {percent:.2f}%", end="\r")


numbers = [x * 5 for x in range(2000, 3000)]
results = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    results.append(math.factorial(x))
    progress_bar(i + 1, len(numbers))

print(colorama.Fore.RESET)'''


"""tickers = ["AAPL", "FB", "TSLA", "NVDA", "GS", "WFC"]
closing_prices = []

progress_bar(0, len(tickers))
for index, ticker in enumerate(tickers):
    last_price = web.DataReader(ticker, "yahoo").iloc[-1]['Close']
    closing_prices.append(last_price)
    progress_bar(index + 1, len(tickers))"""


# => Code to shutdown API (Windows OS)
'''
import os
from tkinter import *

def desligar():
    return os.system('shutdown /s /t1')

def reiniciar():
    return os.system('shutdown /r /t 1')

def sair():
    return os.system('shutdown -l')

master =Tk()
master.geometry('120x150')

master.configure(bg='maroon')

Button(master,text='Desligar', command=desligar).place(x=20, y=20)
Button(master,text='Reiniciar', command=reiniciar).place(x=19, y=50)
Button(master,text='Sair', command=sair).place(x=32, y=80)

mainloop()'''