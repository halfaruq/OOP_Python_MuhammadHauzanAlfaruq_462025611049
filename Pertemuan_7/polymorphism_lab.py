class hewan:
    def suara(self):
        print("ini suara hewan")
        
class kucing(hewan):
    def suara(self):
        print("meow!!!")
        
class anjing(hewan):
    def suara(self):
        print("guk gukk!")
        
def panggil_suara(hewan):
    hewan.suara()
    
panggil_suara(kucing())
panggil_suara(anjing())
        
