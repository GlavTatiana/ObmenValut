from tkinter import *
from tkinter import messagebox as mb
import requests
from tkinter import ttk


def exchange():
    code = combobox.get().upper()
    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена",
                            f"Курс к доллару: {exchange_rate} {code} за 1 доллар")
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
cur=["EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "RUB", "KZT","UZS"]
combobox=ttk.Combobox(values=cur)
combobox.pack(padx=10,pady=10)



Button(text="Получить курс обмена", command=exchange).pack()

window.mainloop()
