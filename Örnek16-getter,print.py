class Personel:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.__maas=maas #kapsüllendi
    #get metodu
    def getMaas(self):
        print("Maaş bilgisine ulaşıldı")
        return self.__maas
#nesne oluşturmak
personel1=Personel("Ali Yiğit","Yıldız",3000)

print("Personel")
print("Ad:",personel1.ad)
print("Soyad:",personel1.soyad)
print("Maas:",personel1.getMaas()) #getMaas çağırıldı