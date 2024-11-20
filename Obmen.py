from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk

def update_c_label(event):
    code=combobox.get()
    name=cur[code]
    c_label.config(text=name)

cur={"EUR": "Евро","JPY": "Японская йена","GBP": "Британский фунт стерлингов",
"AUD": "Австралийский доллар","CAD": "Канадский доллар","CHF": "Швейцарский франк",
"CNY": "Китайский юань","RUB": "Российский рубль","KZT": "Казахстанский тенге","UZS": "Узбекский сум"}

def exchange():
    code = combobox.get().upper()
    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                c_name=cur[code]
                mb.showinfo("Курс обмена",
                            f"Курс к доллару: {exchange_rate:.2f} {c_name} за 1 доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}")
    else:
        mb.showwarning("Внимание!", "Вы не ввели код валюты")


window = Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты: ").pack()


combobox=ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10,pady=10)
combobox.bind("<<ComboboxSelected>>",update_c_label)



c_label=ttk.Label()
c_label.pack(padx=10,pady=10)

Button(text="Получить курс обмена", command=exchange).pack()

window.mainloop()
