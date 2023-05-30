class Çalışan():
     def __init__(self,isim,maaş,departman):
         print("Çalışan sınıfının init fonksiyonu")
         self.isim = isim
         self.maaş = maaş
         self.departman = departman
     def bilgilerigoster(self):
         print("Çalışan sınıfının bilgileri.....")
         print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
     def departman_degistir(self,yeni_departman):
         print("Departman değişiyor....")
         self.departman = yeni_departman

class Yönetici(Çalışan): # Çalışan sınıfından miras alıyoruz.
    pass
yönetici1 = Yönetici("Mehmet Baltacı",3000,"İnsan Kaynakları") # yönetici objesi
yönetici1.bilgilerigoster()
yönetici1.departman_degistir("Halkla İlişkiler")
yönetici1.bilgilerigoster()

class Yönetici(Çalışan):
     def zam_yap(self,zam_miktarı):
         print("Maaşa zam yapılıyor....")
         self.maaş += zam_miktarı

yönetici2 = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim") # yönetici objesi
yönetici2.bilgilerigoster()
yönetici2.zam_yap(500) # Ekstra eklediğimiz fonksiyonu da kullanabiliyoruz.
yönetici2.bilgilerigoster()