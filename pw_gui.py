import tkinter as tk
import random_pw_gen


window = tk.Tk()


def button_click():
    length = int(entry.get())
    password = random_pw_gen.generate_password(length)
    password_label.config(text=password)


entry = tk.Entry(width=10)
entry.pack()
button = tk.Button(text="Generate random password", command=button_click)
button.pack()
label = tk.Label(window, text="Generated password:")
label.pack()
password_label = tk.Label(window)
password_label.pack()
window.mainloop()
