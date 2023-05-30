class Çalışan():
    def __init__(self, isim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgilerigoster(self):
        print("Çalışan sınıfının bilgileri.....")
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim, self.maas, self.departman))

    def departman_degistir(self, yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman


class Yonetici(Çalışan):
    def __init__(self, isim, maas, departman, kisi_sayisi):  # Sorumlu olduğu kişi sayısı
        super().__init__(isim, maas, departman)  # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz.
        print("Yönetici sınıfının init fonksiyonu")

        self.kisi_sayisi = kisi_sayisi  #Ekstra özelliği de kendimiz yazıyoruz.

    def bilgilerigoster(self):
        print("Yönetici sınıfının bilgileri.....")

        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim, self.maas, self.departman, self.kisi_sayisi))

    def zam_yap(self, zam_miktari):
        print("Maaşa zam yapılıyor....")

        self.maas += zam_miktari

c=Yonetici("Oğuz Artıran",3000,"İnsan Kaynakları",4)
c.bilgilerigoster()
