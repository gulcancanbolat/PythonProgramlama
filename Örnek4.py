class Bilgisayar:
    model=""
    marka=""
    def __init__(self,marka= "lenovo", model="hp"):
        self.marka= marka
        self.model= model
#Nesne
laptop=Bilgisayar()
print("Marka:",laptop.marka)
print("Model:",laptop.model)

notebook= Bilgisayar("Asus", "Lenovo")
print("Marka:",notebook.marka)
print("Model:",notebook.model)
