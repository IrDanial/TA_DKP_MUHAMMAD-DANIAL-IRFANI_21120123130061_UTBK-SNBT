# variabel, function-method, if-else, for-loop, OOP, GUI
import tkinter as tk
from tkinter import messagebox
from class1 import snbt

def handle_login(): # function
    email = email_entry.get() # variabel
    password = password_entry.get()

    loginfo = snbt(email, password) # OOP
    if loginfo.checkEmailPass(): #if-else
        loginfo.login()

loginWindow = tk.Tk() # GUI
loginWindow.title("Portal SNPMB UTBK/SNBT 2023 UNDIP")

loginWindow.geometry("450x300")  # Width x Height

email_label = tk.Label(loginWindow, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(loginWindow, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(loginWindow, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(loginWindow, show="*", width=30)
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_button = tk.Button(loginWindow, text="Login", command=handle_login)
login_button.grid(row=2, columnspan=1, padx=10, pady=10)

close_button = tk.Button(loginWindow, text="Exit", command=loginWindow.destroy)
close_button.grid(row=2, columnspan=3, padx=10, pady=10)

loginWindow.mainloop()
