import tkinter as tk
import random_pw_gen


window = tk.Tk()
window.title("caycat95's Random Password Generator")
window.minsize(700, 200)


def button_click():
    length = int(entry.get())
    password = random_pw_gen.generate_password(length)
    password_label.config(text=password)


instruction_label = tk.Label(window, text=("Enter the desired length of" +
                             " your random password:  "))
instruction_label.pack()
entry = tk.Entry(width=10)
entry.pack()
button = tk.Button(text="Generate random password", command=button_click)
button.pack()
label = tk.Label(window, text="Generated password:")
label.pack()
password_label = tk.Label(window)
password_label.pack()
window.mainloop()
