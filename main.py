import tkinter as tk
from tkinter import messagebox
import data
import search

def search_vin(vin:str, event=False):
    vin = vin.replace(' ', '')
    if vin != '':
        if 'ok' in vin.lower():
            result = search.check_vin(vin, vin_numbers_path)
            if result == 0:
                messagebox.showerror('Ошибка', 'Вин-номер не найден в базе.\n(OKxxxxxxxxxxxx)')
                data.play_sound(data.failed)
                return
            elif result == 1:
                messagebox.showerror('Ошибка', 'К этому вин-номеру не привязан iot.')
                data.play_sound(data.failed)
                return
            elif result == -1:
                messagebox.showerror('Ошибка', 'Не найден файл vin.json.\n(в этом файле хранятся все вин-номера самокатов)')
                data.play_sound(data.failed)
                return
            
            messagebox.showinfo('Самокат', str(result))
            data.play_sound(data.fox_unlock)
        else:
            data.play_sound(data.failed)
            messagebox.showerror('Ошибка', 'Неверный формат вин-номера.\n(OKxxxxxxxxxxxx)')
            data.play_sound(data.failed)
    else:
        data.play_sound(data.failed)
        messagebox.showerror('Ошибка', 'Вы не ввели вин-номер.\n(OKxxxxxxxxxxxx)')
        data.play_sound(data.failed)


root = tk.Tk()
root.title('iot search')
root.geometry('400x250')

title = tk.Label(root, text="Поиск iot'ов по вин-номеру")
title.pack(pady=(5, 15))

label = tk.Label(root, text="Вин-номер самоката:")
label.pack(pady=0)
search_input = tk.Entry(root, width=30)
search_input.pack(pady=0)

search_button = tk.Button(root, text='Поиск', command=lambda: search_vin(str(search_input.get())))
search_button.pack(pady=1)

vin_numbers_path = data.open_file()

search_input.bind("<Return>", lambda event: search_vin(str(search_input.get())))

root.mainloop()