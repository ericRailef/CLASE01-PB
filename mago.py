
#Crear clase Mago
class Mago:

    def __init__(self, nombre, vida, mana, nivel):
        self.nombre = nombre
        self.vida = vida
        self.mana = mana
        self.nivel = nivel

    #Método para crear otro mago

    def atacar(self, objetivo):
        #El ataque cuesta 10 puntos de mana
        if self.mana >= 10:

            dano = 20

            self.mana -=10
            # self.mana = self.mana -10
            objetivo.vida -= dano

            #La vida no puede ser menor a 0
            if objetivo.vida < 0:
                objetivo.vida = 0

            print(self.nombre, "atacó a", objetivo.nombre)
            print("Daño realizado", dano)
            print("Vida de ", objetivo.nombre, ":", objetivo.vida)
            print("Mana de", self.nombre, ":", self.mana)
        else:
            print(self.nombre, "No tienes suficiente maná")

    def subir_nivel(self):
        self.nivel += 1
        print(self.nombre, "Subió de nivel", self.nivel)
        
magoUno = Mago("Gandalf", 100, 50, 5)
magoDos = Mago("Merlin", 80, 40, 3)

magoUno.atacar(magoDos)

magoUno.subir_nivel()

        
        