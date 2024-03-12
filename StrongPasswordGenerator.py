import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

window = tk.Tk()
label_header = ttk.Label(text="Conversor de monedas €<=>$")
label_dollar = ttk.Label(text="Valor actual del $: ")
dollar_value = ttk.Entry()
label_euro_amount = ttk.Label(text="Cantidad de €: ")
euro_amount = ttk.Entry()
label_dollar_amount = ttk.Label(text="Cantidad de $: ")
dollar_amount = ttk.Entry()

url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_kAuM2KrWRTGkizfH4saZFT1CAlPOXdYpMRyV80eb&currencies=EUR%2CUSD%2CCAD&base_currency=EUR"

def get_dollar_value():
    response = requests.get(url)
    json_response = response.json()
    return json_response['data']['USD']

actual_dollar_value = get_dollar_value()

def calculate_values():
    first_value = str(euro_amount.get())
    second_value = str(dollar_amount.get())
    
    if(first_value == "" and second_value == ""):
        messagebox.showerror("Error campo vacio","No puede dejar los cuadros de entrada de números vacíos")
    elif((first_value != "" and first_value.isnumeric) and second_value == ""):
        dollar_amount.insert(0, float(euro_amount.get())/actual_dollar_value)
    elif(first_value == "" and (second_value != "" and second_value.isnumeric)):
        euro_amount.insert(0, actual_dollar_value*float(dollar_amount.get()))
    else:
         euro_amount.insert(0, actual_dollar_value*float(dollar_amount.get()))
         
button_calc = ttk.Button(text="Convertir", command=calculate_values)

def config_app():
    window.title("Conversor €<=>$")
    window.config(width=400, height=400)
    
    label_header.place(x=110, y=20)
    label_dollar.place(x=20, y=50)
    dollar_value.place(x=120, y=50)
    dollar_value.insert(0, actual_dollar_value)
    label_euro_amount.place(x=20, y=80)
    euro_amount.place(x=120, y=80)
    label_dollar_amount.place(x=20, y=110)
    dollar_amount.place(x=120, y=110)
    button_calc.place(x=150, y=140)

print(euro_amount.get())

config_app()
window.mainloop()