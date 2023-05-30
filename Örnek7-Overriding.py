class Çalışan():
    def __init__(self, isim, maaş, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


class Yonetici(Çalışan):
    def __init__(self, isim, maas, departman, kisi_sayisi):  # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi  # Yeni eklenen özellik

    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self, zam_miktari):
        print("Maaşa zam yapılıyor....")

        self.maas += zam_miktari

a = Yonetici("Mustafa Murat Coşkun",3000,"Bilişim",10) #Yönetici sınıfının init fonksiyonu. Override edildi.
b = Yonetici("Serhat Say",2500,"Pazarlama",5)
a.bilgilerigoster()
b.bilgilerigoster()
