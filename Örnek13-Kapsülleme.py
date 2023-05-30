class Personel:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
#nesne oluşturmak
personel1=Personel("Ali Yiğit","Yıldız",3000)

#Değiştirme işlemi
personel1.ad="Berrak Betül"
personel1.soyad="Yıldız"
personel1.maas=3500

print("Personel")
print("Ad:",personel1.ad)
print("Soyad:",personel1.soyad)
print("Maas:",personel1.maas) 