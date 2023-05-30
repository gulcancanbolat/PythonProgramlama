class Personel:
    def personel_ozellikleri(self):
        print("Personel Özellikleri")
    def bilgi(self):
        print("Personel Bilgileri x")
class Yonetici:
    def yonetici_ozellikleri(self):
        print("Yönetici Özellikleri")
    def bilgi(self):
        print("Personel Bilgileri")
class Mudur (Personel,Yonetici):
    pass
class GenelMudur (Personel,Yonetici):
    pass
class Cayci(Personel):
    pass
#nesne oluşturmak
mudur=Mudur()
mudur.personel_ozellikleri()
mudur.yonetici_ozellikleri()
mudur.bilgi()