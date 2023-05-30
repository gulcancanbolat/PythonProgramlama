class Sekil:
    def alan_hesapla(self):
        pass

    def cevre_hesapla(self):
        pass


class Ucgen(Sekil):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def cesit_belirle(self):
        if self.a == self.b == self.c:
            return "Eşkenar üçgen"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "İkizkenar üçgen"
        else:
            return "Çeşitkenar üçgen"

    def alan_hesapla(self):
        s = (self.a + self.b + self.c) / 2
        alan = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return alan

    def cevre_hesapla(self):
        cevre = self.a + self.b + self.c
        return cevre


class Dikdortgen(Sekil):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def kare_kontrol(self):
        if self.a == self.b:
            return True
        else:
            return False

    def alan_hesapla(self):
        alan = self.a * self.b
        return alan

    def cevre_hesapla(self):
        cevre = 2 * (self.a + self.b)
        return cevre


# Örnek kullanım
ucgen1 = Ucgen(3, 4, 5)
print("Üçgenin çeşidi:", ucgen1.cesit_belirle())
print("Üçgenin alanı:", ucgen1.alan_hesapla())
print("Üçgenin çevresi:", ucgen1.cevre_hesapla())

dikdortgen1= Dikdortgen(5,10)
print("Dikdörtgenin alanı:", dikdortgen1.alan_hesapla())
print("Dikdörtgenin çevresi:", dikdortgen1.cevre_hesapla())