class Personel:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.__maas=maas #kapsüllendi
#nesne oluşturmak
personel1=Personel("Ali Yiğit","Yıldız",3000)

print("Personel")
print("Ad:",personel1.ad)
print("Soyad:",personel1.soyad)
print("Maas:",personel1.maas) #ulaşılamaz