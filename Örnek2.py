class kus:
    tur=""
    yas=0

    def ot(self):
        print("cik")

    def yaslan(self):
        self.yas+=1
        print("Yaşım arttı:",self.yas)

#nesne oluşturma
papagan=kus()
papagan.tur="Sarı"
papagan.yas=2
print("Kuşun türü=",papagan.tur)
print("Kuşun Yaşı=",papagan.yas)
papagan.ot()
papagan.yaslan()
papagan.ot()
