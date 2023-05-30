class Hayvan:
    def __init__(self, ad , yas, ozellik):
        self.ad = ad
        self.yas = yas
        self.ozellik = ozellik

    def Gor(self):
        print("Hayvanın adı:", self.ad)
        print("Hayvanın yaşı:", self.yas)
        print("Hayvanın türü:", self.ozellik)

    def YasArtir(self):
        self.yas += 1
        print("Hayvanın yaşı bir yıl artırıldı. Yeni yaş:", self.yas)
# Hayvan örneği oluşturma
hayvan1 = Hayvan("Köpük", 3, "Köpek")

# Hayvan bilgilerini görüntüleme
hayvan1.Gor()

# Hayvanın yaşını artırma
hayvan1.YasArtir()
