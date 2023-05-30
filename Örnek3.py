class Kedi:
    ad="Mırmır"
    yas= 0

    def miyav(self):
        print("Merhaba Ben: {}, Miyav!!!".format(self.ad))

    def yaslan(self):
        self.yas+=1
        print("Yaşım Arttı:", self.yas)
#nesne
kedi1=Kedi()
kedi2=Kedi()
kedi1.miyav()
kedi2.miyav()
#nesne
kedi3=Kedi()
kedi3.ad="Lila"
kedi3.miyav()




