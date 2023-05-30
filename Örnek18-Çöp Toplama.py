class Personel:
    def __init__(self,ad,soyad):
        self.__ad=ad
        self.__soyad=soyad
    def getAd(self):
        return self.__ad
    def setAd(self,yeni_deger):
        self.__ad=yeni_deger

    def getSoyad(self):
        return self.__soyad

    def setSoyad(self, yeni_deger):
        self.__soyad = yeni_deger
#nesne
personel1= Personel("Ahmet Yiğit","Yıldız")
print("Ekrana Yazdırma İşlemi")
print("Ad:",personel1.getAd())
print("Soyad:",personel1.getSoyad())
#Nesne yok etme
del personel1 #nesneyi tutan değişken silindi

print("\nYok edildikten sonra ulaşma işlemi")
print("Ad:",personel1.getAd())
print("Soyad:",personel1.getSoyad())