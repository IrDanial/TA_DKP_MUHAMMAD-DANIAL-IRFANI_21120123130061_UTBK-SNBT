import csv
import tkinter as tk
#test

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

    def checkEmailPass(self):
        for value in self.data: # for-loop
            if value == self.email:
                get_data_user = self.data[value]
                if self.password == get_data_user['password']:
                    return get_data_user
                else:
                    return False

    def login(self):
        get_data = self.checkEmailPass()
        if get_data:
            resultWindow = tk.Tk() # GUI
            resultWindow.title("Portal SNPMB UTBK/SNBT 2023 UNDIP")

            resultWindow.geometry("450x400")  # Width x Height

            label1 = tk.Label(resultWindow, text="Selamat Datang, " + get_data['nama'])
            label1.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

            label2 = tk.Label(resultWindow, text="Anda telah terdaftar sebagai " + get_data['role'] + " UTBK/SNBT 2023 Universitas Diponegoro")
            label2.grid(row=1, column=0, padx=10, pady=2, sticky="nw")

            label3 = tk.Label(resultWindow, text="Anda masuk sebagai: " + self.email)
            label3.grid(row=2, column=0, padx=10, pady=2, sticky="nw")

            label4 = tk.Label(resultWindow, text="Silahkan memilih Program studi:")
            label4.grid(row=3, column=0, padx=10, pady=2, sticky="nw")

            dropdown_var1 = tk.StringVar(resultWindow)
            dropdown_var2 = tk.StringVar(resultWindow)
            dropdown_var3 = tk.StringVar(resultWindow)

            options1 = ["Arsitektur (Saintek)", "Teknik Sipil (Saintek)", "Perencanaan Wilayah Kota (Saintek)", "Teknik Geologi (Saintek)",
                        "Teknik Komputer (Saintek)", "Teknik Geodesi (Saintek)", "Teknik Perkapalan (Saintek)", "Teknik Lingkungan (Saintek)", 
                        "Teknik Elektro (Saintek)", "Teknik Kimia (Saintek)", "Teknik Mesin (Saintek)", "Teknik Industri (Saintek)",
                        "Kedokteran (Saintek)", "Farmasi (Saintek)", "Kedokteran Gigi (Saintek)", "Keperawatan (Saintek)", "Gizi (Saintek)"]
            
            options2 = ["Administrasi Bisnis (Soshum)", "Administrasi Publik (Soshum)", "Hubungan Internasional (Soshum)", 
                        "Ilmu Pemerintahan (Soshum)", "Manajemen (Soshum)", "Ilmu Ekonomi (Soshum)", 
                        "Ekonomi Islam (Soshum)", "Akuntansi (Soshum)", "Ilmu Hukum (Soshum)"]
            
            options3 = ["Teknik Infrastruktur Sipil dan Arsitektur (Vokasi)", "Perencanaan Tata Ruang dan Pertanahan (Vokasi)", "Akuntansi Perpajakan (Vokasi)", "Manajemen dan Administrasi Logistik (Vokasi)",
                        "Teknologi Rekayasa Kimia Industri (Vokasi)", "Rekayasa Perancangan Mekanik (Vokasi)", "Teknologi Rekayasa Otomasi (Vokasi)",
                        "Teknologi Rekayasa Konstruksi Perkapalan (Vokasi)", "Teknik Listrik Industri (Vokasi)", "Bahasa Asing Terapan (Vokasi)",
                        "Informasi dan Humas (Vokasi)"]

            dropdown_var1.set(options1[0])
            dropdown_var2.set(options2[0])
            dropdown_var3.set(options3[0])

            dropdown_menu1 = tk.OptionMenu(resultWindow, dropdown_var1, *options1)
            dropdown_menu1.config(width=40, highlightthickness=1, highlightbackground="blue")
            dropdown_menu2 = tk.OptionMenu(resultWindow, dropdown_var2, *options2)
            dropdown_menu2.config(width=40, highlightthickness=1, highlightbackground="green")
            dropdown_menu3 = tk.OptionMenu(resultWindow, dropdown_var3, *options3)
            dropdown_menu3.config(width=40, highlightthickness=1, highlightbackground="yellow")

            dropdown_menu1.grid(row=4, column=0, padx=5, pady=10, sticky="w")
            dropdown_menu2.grid(row=5, column=0, padx=5, pady=10, sticky="w")
            dropdown_menu3.grid(row=6, column=0, padx=5, pady=10, sticky="w")

            login_button = tk.Button(resultWindow, text="Oke", command=lambda: self.result(dropdown_var1.get(), 
                                                                                           dropdown_var2.get(), 
                                                                                           dropdown_var3.get()))
            login_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")

            close_button = tk.Button(resultWindow, text="Exit", command=resultWindow.destroy)
            close_button.grid(row=8, column=0, padx=10, pady=10, sticky="w")

            resultWindow.mainloop()

    def result(self, pil1, pil2, pil3):
        get_data = self.checkEmailPass()

        resultWindow2 = tk.Tk()

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
