from tkinter import *
import bmi_class

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('Kalkulator BMI')
        self.geometry('600x300')
        self.config(bg='#686e70')

        # variabel untuk jenis kelamin
        self.genderVar = IntVar()
        
        # frame utama
        self.frame = Frame(self, padx=10, pady=10)
        self.frame.pack(expand=True)

        # widget untuk baris pertama, label nama dan entry nama
        self.nama_label = Label(self.frame, text="Masukkan nama")
        self.nama_label.grid(row=1, column=1)
        self.nama_entry = Entry(self.frame)
        self.nama_entry.grid(row=1, column=2, pady=5)

        # widget untuk baris kedua, label umur dan entry umur
        self.umur_label = Label(self.frame, text="Masukkan umur (2 - 100)")
        self.umur_label.grid(row=2, column=1)
        self.umur_entry = Entry(self.frame)
        self.umur_entry.grid(row=2, column=2, pady=5)

        # widget untuk baris ketiga, label kelamin dan radio button kelamin (disatukan menggunakan frame2)
        self.gender_label = Label(self.frame, text='Pilih jenis kelamin')
        self.gender_label.grid(row=3, column=1)

        self.frame2 = Frame(self.frame)
        self.frame2.grid(row=3, column=2, pady=5)
        self.pria_rb = Radiobutton(self.frame2, text = 'Pria', variable = self.genderVar, value = 1)
        self.pria_rb.pack(side=LEFT)
        self.wanita_rb = Radiobutton(self.frame2, text = 'Wanita', variable = self.genderVar, value = 2)
        self.wanita_rb.pack(side=RIGHT)

        # widget untuk baris keempat, label tinggi dan entry tinggi
        self.tinggi_label = Label(self.frame, text="Masukkan tinggi badan (cm)  ")
        self.tinggi_label.grid(row=4, column=1)
        self.tinggi_entry = Entry(self.frame)
        self.tinggi_entry.grid(row=4, column=2, pady=5)

        # widget untuk baris kelima, label berat dan entry berat
        self.berat_label = Label(self.frame, text="Masukkan berat badan (kg)  ")
        self.berat_label.grid(row=5, column=1)
        self.berat_entry = Entry(self.frame)
        self.berat_entry.grid(row=5, column=2, pady=5)

        # widget untuk baris keenam, tombol hitung, reset, dan exit (disatukan menggunakan frame3)
        self.frame3 = Frame(self.frame)
        self.frame3.grid(row=6, columnspan=3, pady=10)
        self.hitung_btn = Button(self.frame3, text='Hitung', command=self.hitung)
        self.hitung_btn.pack(side=LEFT)
        self.reset_btn = Button(self.frame3, text='Reset', command=self.reset_entry)
        self.reset_btn.pack(side=LEFT)
        self.exit_btn = Button(self.frame3, text='Exit', command=lambda:self.destroy())
        self.exit_btn.pack(side=LEFT)

        # frame untuk gambar dan hasil kalkulasi BMI
        self.frame4 = Frame(self.frame)
        self.frame4.grid(row=1, rowspan=6, column=3, padx=5)

        self.BMIImage = PhotoImage(file='gambar/normal_man.png')
        self.BMIImage_label = Label(self.frame4, image=self.BMIImage)
        self.BMIImage_label.pack()

        # variabel untuk hasil BMI
        self.hasilBMI_var = StringVar(value='-')
        self.hasilBMI_label = Label(self.frame4, textvariable=self.hasilBMI_var)
        self.hasilBMI_label.pack()

    # method untuk reset seluruh entry
    def reset_entry(self):
        self.nama_entry.delete(0,'end')
        self.umur_entry.delete(0,'end')
        self.genderVar.set(None)
        self.tinggi_entry.delete(0,'end')
        self.berat_entry.delete(0,'end')
        self.BMIImage.configure(file='gambar/normal_man.png')
        self.hasilBMI_var.set("-")

    # method untuk menghitung dan menampilkan hasil perhitungan BMI
    def hitung(self):
        gender = 'Pria' if self.genderVar.get() == 1 else 'Wanita'
        umur = int(self.umur_entry.get())
        if umur >= 2 and umur <= 20:
            user = bmi_class.Child(
                self.nama_entry.get(),
                umur,
                gender,
                int(self.tinggi_entry.get()),
                int(self.berat_entry.get())
            )
        else:
            user = bmi_class.Adult(
                self.nama_entry.get(),
                umur,
                gender,
                int(self.tinggi_entry.get()),
                int(self.berat_entry.get())
            )

        self.BMIImage.configure(file=user.gambar)
        self.hasilBMI_var.set(f"Nilai BMI: {user.bmi}")

GUI().mainloop()