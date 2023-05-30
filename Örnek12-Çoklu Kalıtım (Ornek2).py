class Personel:
    def personel_bilgi(self):
        print("Personel Bilgisi")
class Yonetici:
    def yonetici_bilgi(self):
        print("Yonetici Bilgisi")
class Mudur(Personel,Yonetici):
    def mudur_bilgi(self):
        print("Mudur Bilgisi")
class GenelMudur (Mudur):
    pass
class Cayci (Personel):
    pass
#nesne oluşturmak
gm=GenelMudur()
gm.personel_bilgi()
gm.yonetici_bilgi()
gm.mudur_bilgi()