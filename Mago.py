class Mago: 
    def __init__(self, nombre: str, mana: int, poder: str, vida:int ):
        self.nombre = nombre
        self.mana = mana
        self.poder = poder
        self.vida = vida 

    def info_mago(self):

        print("Nombre: ", self.nombre)
        print("Mana: ", self.mana)
        print("Poder: ", self.poder)
        print("Vida: ", self.vida)

    def ataque(self, conflicto):

        if self.mana >= 100:
            daño = 300
            self.mana -= 50
            conflicto.vida -= daño
            

        if conflicto.vida < 0:
            conflicto = 0

            print(self.nombre, "Se realizo un ataque a ", conflicto.nombre)
            print("Daño realizado ", self.daño)
            print(" vida  ", self.poder)
            print("a ", self.mana)






mago1 = Mago(nombre= "Ralf", mana= 200, poder=200, vida=150)
mago2 = Mago(nombre= "Rey", mana= 150, poder=200, vida=150)

mago1.info_mago()
mago2.info_mago()
mago1.ataque(conflicto=mago2)


