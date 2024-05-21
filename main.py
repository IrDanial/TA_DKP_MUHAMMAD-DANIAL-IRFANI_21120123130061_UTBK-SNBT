# variabel, function-method, if-else, for-loop, OOP, GUI
import tkinter as tk
from tkinter import messagebox
from class1 import snbt

def handle_login(): # function
    email = email_entry.get() # variabel
    password = password_entry.get()

    login_info = snbt(email, password) # OOP
    if login_info.checkEmailPass(): #if-else
        login_info.login()
    else:
        messagebox.showerror("Login Gagal", "Email atau Password salah!")

# main window
loginWindow = tk.Tk() # GUI
loginWindow.title("Portal SNPMB UTBK/SNBT 2023")

# set window size
loginWindow.geometry("450x300")  # Width x Height

# labels and entry fields
email_label = tk.Label(loginWindow, text="Email:")
email_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
email_entry = tk.Entry(loginWindow, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)
# password
password_label = tk.Label(loginWindow, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(loginWindow, show="*", width=30)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# login button
login_button = tk.Button(loginWindow, text="Login", command=handle_login)
login_button.grid(row=2, columnspan=1, padx=10, pady=10)

# Create a button to close the window
close_button = tk.Button(loginWindow, text="Exit", command=loginWindow.destroy)
close_button.grid(row=2, columnspan=3, padx=10, pady=10)

# main event loop
loginWindow.mainloop()
