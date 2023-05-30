class Araba:
    marka=""
    model=""
    renk=""
    def __init__(self,marka= "Toyota", model="Yaris",renk="Mavi"):
        self.marka= marka
        self.model= model
        self.renk=renk

    def start(self):
        print("araç çalıştırıldı.")

    def stop(self):
        print("araç durduruldu.")

araba1=Araba()
print("Arabanın markası:",araba1.marka)
print("Arabanın modeli:",araba1.model)
print("Arabanın rengi:",araba1.renk)
araba1.start()
araba1.stop()
araba2=Araba("Opel","Corsa","Kırmızı")
print("Arabanın markası:",araba2.marka)
print("Arabanın modeli:",araba2.model)
print("Arabanın rengi:",araba2.renk)
araba2.stop()
araba2.start()