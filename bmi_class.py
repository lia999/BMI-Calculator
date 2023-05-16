import csv

# base class, sebuah orang (person). Satu orang punya nama, umur, gender,
# tinggi, dan berat badan

class Person:
    def __init__(self, nama, umur, gender, tinggi, berat):
        self.nama = nama
        self.umur = umur
        self.gender = gender
        self.tinggi = tinggi
        self.berat = berat
        self.bmi = self.hitungBMI()
    
    def hitungBMI(self):
        return round(self.berat / (self.tinggi/100)**2, 2)


class Adult(Person):
    def __init__(self, nama, umur, gender, tinggi, berat):
        super().__init__(nama, umur, gender, tinggi, berat)
        
        self.kategori = self.kategorisasi()
        self.gambar = self.ambil_gambar()

    def kategorisasi(self):
        if self.bmi <= 18.5:
            return "Underweight"
        elif self.bmi > 18.5 and self.bmi <= 24.9:
            return "Normal"
        elif self.bmi > 24.9 and self.bmi <= 29.9:
            return "Overweight"
        elif self.bmi > 29.9:
            return "Obesitas"

    def ambil_gambar(self):
        if self.gender == "Pria":
            if self.kategori == "Underweight":
                return "gambar/underweight_man.png"
            elif self.kategori == "Normal":
                return "gambar/normal_man.png"
            elif self.kategori == "Overweight":
                return "gambar/overweight_man.png"
            elif self.kategori == "Obesitas":
                return "gambar/obesity_man.png"
        elif self.gender == "Wanita":
            if self.kategori == "Underweight":
                return "gambar/underweight_woman.png"
            elif self.kategori == "Normal":
                return "gambar/normal_woman.png"
            elif self.kategori == "Overweight":
                return "gambar/overweight_woman.png"
            elif self.kategori == "Obesitas":
                return "gambar/obesity_woman.png"


class Child(Person):
    def __init__(self, nama, umur, gender, tinggi, berat):
        super().__init__(nama, umur, gender, tinggi, berat)
    
        self.kategori = self.kategorisasi()
        self.gambar = self.ambil_gambar()

    def kategorisasi(self):
        if self.gender == "Pria":
            BMIChartFile = open('dataBMIChild/male.csv')
        elif self.gender == "Wanita":
            BMIChartFile = open('dataBMIChild/female.csv')
    
        csv_reader = csv.DictReader(BMIChartFile, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0: line_count += 1     # skip baris pertama (baris header)
            if int(row["Age"]) == self.umur:
                if self.bmi <= float(row["P5"]):
                    return "Underweight"
                elif self.bmi > float(row["P5"]) and self.bmi <= float(row["P85"]):
                    return "Normal"
                elif self.bmi > float(row["P85"]) and self.bmi <= float(row["P95"]):
                    return "Overweight"
                elif self.bmi > float(row["P95"]):
                    return "Obesitas"
    
    def ambil_gambar(self):
        if self.gender == "Pria":
            if self.kategori == "Underweight":
                return "gambar/underweight_man.png"
            elif self.kategori == "Normal":
                return "gambar/normal_man.png"
            elif self.kategori == "Overweight":
                return "gambar/overweight_man.png"
            elif self.kategori == "Obesitas":
                return "gambar/obesity_man.png"
        elif self.gender == "Wanita":
            if self.kategori == "Underweight":
                return "gambar/underweight_woman.png"
            elif self.kategori == "Normal":
                return "gambar/normal_woman.png"
            elif self.kategori == "Overweight":
                return "gambar/overweight_woman.png"
            elif self.kategori == "Obesitas":
                return "gambar/obesity_woman.png"
