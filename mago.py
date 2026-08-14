

class Mago:
    def __init__(self, nombre, vida, mana, nivel):
        self.nombre = nombre
        self.vida = vida
        self.mana = mana
        self.nivel = nivel

    #Método para atacar a otro mago
    def atacar(self, objetivo):
        #el ataque cuesta 10 de mana
        if self.mana >= 10:
            dano = 20
            self.mana -=10
            objetivo.vida -= dano

            #la vida no puede ser negativa
            if objetivo.vida < 0:
             objetivo.vida = 0

            print(self.nombre, "atacó a ", objetivo.nombre)
            print("Daño realizado", dano)
            print("Vida de ", objetivo.nombre, ":", objetivo.vida)
            print("Mana de ", self.nombre, ":", self.mana)

    def subir_nivel(self):
       self.nivel+=1
    #    self.nivel = self.nivel + 1

       print(self.nombre, "subió de nivel", self.nivel)

magoUno = Mago("Gandalf", 100, 50, 5)
magoDos = Mago("Sauron", 80, 40, 3)

magoUno.atacar(magoDos)

magoUno.subir_nivel()