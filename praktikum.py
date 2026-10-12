class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def __str__(self):
        return f"Persegi Panjang,panjang {self.panjang}, lebar {self.lebar} cm"

input_panjang = int(input("masukkan panjang (cm):"))
if input_panjang <= 0:
    print("tidak boleh nol atau negatif")
    exit()
input_lebar = int(input("masukkan lebar (cm):"))
if input_lebar <= 0:
    print("tidak boleh nol atau negatif")
    exit()

PP = PersegiPanjang(input_panjang, input_lebar)

print(PP)
print("keliling:", PP.hitung_keliling(), "cm")
print("luas:", PP.hitung_luas(), "cm²")