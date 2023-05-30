class Personel:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.__maas=maas #kapsüllendi
    #get metodu ile ulaşma
    def getMaas(self):
        print("Maaş bilgisine ulaşıldı")
        return self.__maas
    # set metodu ile güncelleme
    def setMaas(self,yeni_deger):
        print("Maaş bilgisi değiştirildi")
        self.__maas=yeni_deger

#nesne oluşturmak
personel1=Personel("Ali Yiğit","Yıldız",3000)

print("Personel")
print("Ad:",personel1.ad)
print("Soyad:",personel1.soyad)
#maaş güncellendi
personel1.setMaas(5000)
print("Maas:",personel1.getMaas()) #getMaas çağırıldı