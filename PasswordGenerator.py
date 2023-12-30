# Created by Acas Saleem
# Github:
# Educational Purposes only
import tkinter as tk
from tkinter import *
from tkinter import ttk
import string
import secrets
import pyperclip


def GeneratePassword(x):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Generates a random 20 character password
    password = ''.join(secrets.choice(alphabet) for x in range(x))
    print("Generated Password:", password)
    pyperclip.copy(password)  # Copies to the clipboard
    return password


# Window
window = tk.Tk()
window.title('Password Generator')
window.geometry('500x250')

# title
title_label = ttk.Label(master=window, text='Password Generator', font='Calibri 24 bold')
title_label.pack()
# input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Generate', command=GeneratePassword(20))
title_label
entry.pack()
button.pack()
input_frame.pack()

# run
window.mainloop()
