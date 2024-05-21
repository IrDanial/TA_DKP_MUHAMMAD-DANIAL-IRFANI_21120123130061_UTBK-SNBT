import csv
import tkinter as tk

class snbt:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.data = self.load_data_from_csv('data.csv')

    def load_data_from_csv(self, filename):
        data = {}
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                email = row['email']
                data[email] = {
                    'nama': row['nama'],
                    'password': row['password'],
                    'role': row['role']
                }
        return data

    # Method untuk pengecekan kesesuaian input dengan data di dictionary yang telah kita buat
    def checkEmailPass(self):
        for value in self.data: # for-loop
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    # Method untuk proses login dalam console
    def login(self):
        get_data = self.checkEmailPass()
        if get_data:
            # main window
            resultWindow = tk.Tk() # GUI
            resultWindow.title("Portal SNPMB UTBK/SNBT 2023")

            # set window size
            resultWindow.geometry("450x400")  # Width x Height

            # label 1
            label1 = tk.Label(resultWindow, text="Selamat Datang, " + get_data['nama'])
            label1.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

            # label 2
            label2 = tk.Label(resultWindow, text="Anda telah terdaftar sebagai " + get_data['role'] + " UTBK/SNBT 2023")
            label2.grid(row=1, column=0, padx=10, pady=2, sticky="nw")

            # label 3
            label3 = tk.Label(resultWindow, text="Anda masuk sebagai: " + self.email)
            label3.grid(row=2, column=0, padx=10, pady=2, sticky="nw")

            # label 4
            label4 = tk.Label(resultWindow, text="Silahkan memilih Program studi:")
            label4.grid(row=3, column=0, padx=10, pady=2, sticky="nw")

            # Create a variable to hold the selected option
            dropdown_var1 = tk.StringVar(resultWindow)
            dropdown_var2 = tk.StringVar(resultWindow)
            dropdown_var3 = tk.StringVar(resultWindow)

            # Define the list of options
            options1 = ["Option 1", "Option 2", "Option 3", "Option 4"]
            options2 = ["Option 5", "Option 6", "Option 7", "Option 8"]
            options3 = ["Option 9", "Option 10", "Option 11", "Option 12"]

            # Set the default value of the dropdown
            dropdown_var1.set(options1[0])
            dropdown_var2.set(options2[0])
            dropdown_var3.set(options3[0])

            # Create the OptionMenu widget with colors and width
            dropdown_menu1 = tk.OptionMenu(resultWindow, dropdown_var1, *options1)
            dropdown_menu1.config(width=20, highlightthickness=1, highlightbackground="blue")
            dropdown_menu2 = tk.OptionMenu(resultWindow, dropdown_var2, *options2)
            dropdown_menu2.config(width=20, highlightthickness=1, highlightbackground="green")
            dropdown_menu3 = tk.OptionMenu(resultWindow, dropdown_var3, *options3)
            dropdown_menu3.config(width=20, highlightthickness=1, highlightbackground="yellow")

            # Position the OptionMenu widget in the window
            dropdown_menu1.grid(row=4, column=0, padx=5, pady=10, sticky="w")
            dropdown_menu2.grid(row=5, column=0, padx=5, pady=10, sticky="w")
            dropdown_menu3.grid(row=6, column=0, padx=5, pady=10, sticky="w")

            # login button
            login_button = tk.Button(resultWindow, text="Oke", command=lambda: self.result(dropdown_var1.get(), dropdown_var2.get(), dropdown_var3.get()))
            login_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")

            # Create a button to close the window
            close_button = tk.Button(resultWindow, text="Exit", command=resultWindow.destroy)
            close_button.grid(row=8, column=0, padx=10, pady=10, sticky="w")

            # Run the main event loop
            resultWindow.mainloop()

    # when oke button pressed
    def result(self, pil1, pil2, pil3):
        get_data = self.checkEmailPass()

        # gui
        resultWindow2 = tk.Tk()

        # gui declaration
        resultWindow2.title("Portal SNPMB UTBK/SNBT 2023")
        resultWindow2.geometry("450x400")

        label1 = tk.Label(resultWindow2, text="Hai, " + get_data['nama'])
        label1.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

        label2 = tk.Label(resultWindow2, text="Program Studi Pilihan anda yaitu: ")
        label2.grid(row=1, column=0, padx=10, pady=2, sticky="nw")
        label3 = tk.Label(resultWindow2, text="1. "+pil1)
        label3.grid(row=2, column=0, padx=10, pady=2, sticky="nw")

        label4 = tk.Label(resultWindow2, text="2. "+pil2)
        label4.grid(row=3, column=0, padx=10, pady=2, sticky="nw")

        label5 = tk.Label(resultWindow2, text="3. "+pil3)
        label5.grid(row=4, column=0, padx=10, pady=2, sticky="nw")

        close_button = tk.Button(resultWindow2, text="Exit", command=resultWindow2.destroy)
        close_button.grid(row=5, column=0, padx=10, pady=10, sticky="w")
