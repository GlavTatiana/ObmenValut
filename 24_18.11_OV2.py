from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk



def exchange():
    code=combobox.get().upper()
    if code:
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            data=response.json()
            if code in data["rates"]:
                exchange_rate=data["rates"][code]
                cur_name=popular_cur[code]
                mb.showinfo("Курс обмена",
                            f"Курс к доллару: {exchange_rate:.2f} {cur_name} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", e)
    else:
        mb.showwarning("Внимание!", "Вы не ввели код валюты")


def update_label(event):
    code=combobox.get()
    name=popular_cur[code]
    cur_label["text"]=name



#popular_cur = ["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT","UZS"]
popular_cur = {"EUR": "Евро","JPY": "Японская йена","GBP": "Британский фунт стерлингов",
"AUD": "Австралийский доллар","CAD": "Канадский доллар","CHF": "Швейцарский франк",
"CNY": "Китайский юань","RUB": "Российский рубль","KZT": "Казахстанский тенге","UZS": "Узбекский сум"}

window=Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты: ").pack()

entry = Entry()
entry.pack()

Button(text="Получить курс обмена", command=exchange).pack()

window.mainloop()
