class Hesap:
    def __init__(self, adSoyad, hesapNo, Bakiye):
        self. adSoyad = adSoyad
        self. hesapNo = hesapNo
        self. Bakiye = Bakiye

    def GorBakiye (self):
        print("Hesap bakiyesi:", self. Bakiye)

    def ParaYatir (self, miktar):
        self. Bakiye += miktar
        print(miktar, "TL hesaba yatırıldı. Yeni bakiye:", self. Bakiye)

    def ParaCek (self, miktar):
        if self. Bakiye >= miktar:
            self. Bakiye -= miktar
            print(miktar, "TL çekildi. Yeni bakiye:", self. Bakiye)
        else:
            print("Yetersiz bakiye. Çekme işlemi gerçekleştirilemedi.")
# Hesap örneği oluşturma
hesap1 = Hesap ("Ahmet Yılmaz", "123456789", 1000)
hesap2= Hesap("Ayşe Can", "987654321", 2000)

# Hesap bilgilerini görüntüleme
hesap1. GorBakiye ()
hesap2. GorBakiye ()

# Para yatırma işlemi
hesap1. ParaYatir (500)
hesap2. GorBakiye ()
# Para çekme işlemi
hesap1. ParaCek (2000)
hesap1. ParaCek (200)
hesap2. ParaCek (2000)