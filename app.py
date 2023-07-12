import phonenumbers
from phonenumbers import geocoder
import tkinter as tk

def get_phone_info():
    phone_number = city_entry.get()
    country_code = country_var.get()
    if not phone_number.startswith('+'):
        phone_number = country_code + phone_number
    parsed_number = phonenumbers.parse(phone_number)
    phone_info = geocoder.description_for_number(parsed_number, "en")
    result_label['text'] = phone_info

root = tk.Tk()
root.title("LOCATE NUMBER")

phone_label = tk.Label(root, text='Enter phone number: ')
phone_label.grid(row=0, column=0, columnspan=2)

country_label = tk.Label(root, text='Select country code: ')
country_label.grid(row=1, column=0)

country_codes = ['+1', '+27', '+30', '+31', '+32', '+33', '+34', '+36', '+39', '+40', '+41', '+43', '+44', '+45', '+46', '+47', '+48', '+49', '+51', '+52', '+53', '+54', '+55', '+56', '+57', '+58']
country_var = tk.StringVar(root)
country_var.set(country_codes[0])
country_optionmenu = tk.OptionMenu(root, country_var, *country_codes)
country_optionmenu.grid(row=1, column=1)

city_entry = tk.Entry(root, width=50)
city_entry.grid(row=2, column=0, columnspan=2)

submit_button = tk.Button(root, text='Consultar', command=get_phone_info, width=10, height=2)
submit_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text='')
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

