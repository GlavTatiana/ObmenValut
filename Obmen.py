from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def update_b_label(event):
    code=b_combobox.get()
    name=cur[code]
    b_label.config(text=name)

def update_b2_label(event):
    code=b2_combobox.get()
    name=cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code=t_combobox.get()
    name=cur[code]
    t_label.config(text=name)

cur={"EUR": "Евро","JPY": "Японская йена","GBP": "Британский фунт стерлингов",
"AUD": "Австралийский доллар","CAD": "Канадский доллар","CHF": "Швейцарский франк",
"CNY": "Китайский юань","RUB": "Российский рубль","KZT": "Казахстанский тенге",
"UZS": "Узбекский сум", "USD": "Американский доллар"}

def exchange():
    t_code = t_combobox.get().upper()
    b_code = b_combobox.get().upper()
    b2_code = b2_combobox.get().upper()
    if t_code and b_code and b2_code:
        try:
            response = requests.get(f"https://open.er-api.com/v6/latest/{b_code}")
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name=cur[t_code]
                b_name=cur[b_code]
                b2_name = cur[b2_code]
                mb.showinfo("Курс обмена",
                            f"Курс: {exchange_rate:.2f} {t_name}\n за 1 {b_name} \n за 1 {b2_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка {e}")
    else:
        mb.showwarning("Внимание!", "Вы не ввели код валюты")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("350x500")


Label(text="Базовая валюта").pack(padx=10,pady=10)
b_combobox=ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10,pady=10)
b_combobox.bind("<<ComboboxSelected>>",update_b_label)
b_label=ttk.Label()
b_label.pack(padx=10,pady=10)

Label(text="Вторая базовая валюта").pack(padx=10,pady=10)
b2_combobox=ttk.Combobox(values=list(cur.keys()))
b2_combobox.pack(padx=10,pady=10)
b2_combobox.bind("<<ComboboxSelected>>",update_b2_label)
b2_label=ttk.Label()
b2_label.pack(padx=10,pady=10)


Label(text="Целевая валюта").pack(padx=10,pady=10)
t_combobox=ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10,pady=10)
t_combobox.bind("<<ComboboxSelected>>",update_t_label)
t_label=ttk.Label()
t_label.pack(padx=10,pady=10)

Button(text="Получить курс обмена", command=exchange).pack()

window.mainloop()
