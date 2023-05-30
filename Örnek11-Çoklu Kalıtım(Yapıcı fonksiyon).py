class Personel:
    def __init__(self):
        self.maas="1000"
        print(self.maas)
class Yonetici:
    def __init__(self):
        self.maas="2000"
        print(self.maas)
class Mudur(Personel,Yonetici):
    def __init__(self):
        Yonetici.__init__(self)
class GenelMudur(Personel,Yonetici):
    pass
class Cayci(Personel):
    pass
#nesne oluşturmak
mudur=Mudur()
