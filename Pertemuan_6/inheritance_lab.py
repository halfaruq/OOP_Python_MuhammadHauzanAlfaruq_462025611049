class Karakter:
    def __init__(self, nama, nyawa, kekuatan):
        self.nama = nama
        self.nyawa = nyawa
        self.kekuatan = kekuatan 

class Fighter(Karakter):
    def __init__(self, nama, nyawa, kekuatan, ketahanan):
        super().__init__(nama, nyawa, kekuatan)
        self.ketahanan = ketahanan
            
    def serangan_jarak_dekat(self, musuh):
        print(f" {self.nama} menyerang {musuh.nama} jarak dekat!")
        if (self.kekuatan + self.ketahanan) > (musuh.kekuatan + getattr(musuh, 'ketahanan', 0)):
            print(f"Hasil: {self.nama} menang!!!")
        else:
            print(f"Hasil: Serangan tertahan atau {musuh.nama} lebih kuat!")

class Mage(Karakter):
    def __init__(self, nama, nyawa, kekuatan, jarak=0):
        super().__init__(nama, nyawa, kekuatan)
        self.jarak = jarak
        
    def serangan_jarak_jauh(self, musuh):
        print(f"{self.nama} menembakkan sihir ke {musuh.nama}!")
        if self.jarak > getattr(musuh, 'jarak', 5):
            print(f"Hasil: {self.nama} menang dari jauh!!!")
        else:
            print(f"Hasil: Musuh terlalu dekat atau jangkauan kurang!")

class MageFighter(Fighter, Mage):
    def __init__(self, nama, nyawa, kekuatan, ketahanan, jarak):
        super().__init__(nama, nyawa, kekuatan, ketahanan)
        self.jarak = jarak

pahlawan1 = MageFighter("Asep", 100, 80, 50, 100)
musuh1 = Fighter("Monster", 100, 60, 20)

pahlawan1.serangan_jarak_dekat(musuh1)
pahlawan1.serangan_jarak_jauh(musuh1)
