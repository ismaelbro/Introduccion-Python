import random
import os
import time
class Animal(object):
    def __init__(self, nombre):
        self.nombre = nombre
        self.genero = random.choice(["machito","hembrita"])
class Tamagochi(Animal):

    def __init__(self, nombre):
        Animal.__init__(self,nombre)
        self.felicidad = 10
        self.salud = 0
        self.hambre = 10

    def turno(self):
        self.felicidad -= 1
        self.hambre -= 1

    def alimentar(self):
        self.hambre +=2
        if(self.hambre > 10):
            self.hambre = 10
            self.salud +=2
    def jugar(self):
        self.felicidad += 3
        if(self.felicidad > 10):
            self.felicidad = 10
            self.salud += 2 

    def estado(self):
        estado = "vivo"
        if (self.hambre == 0 or self.salud == 10 or self.felicidad == 0):
            estado = "muerto"
        return estado

    def __str__(self):
        return 'Hola me llamo '+self.nombre+' y soy '+self.genero

print("\nJUEGO DE TAMAGOTCHI PYTHON\n")
nombre = input("Ingrese el nombre de su tamagotchi: ")
t = Tamagochi(nombre)
while(True):
    os.system("cls")
    print(t.estado())
    if(t.estado() == 'vivo'):
        print("\nJUEGO DE TAMAGOTCHI PYTHON\n")
        print(""+t.__str__())
        print("Salud: "+str(t.salud))
        print("Hambre: "+str(t.hambre))
        print("Felicidad: "+str(t.felicidad))
        while(True):
            try:
                print("\n1) Alimentar.")
                print("2) Jugar.")
                opcion = int(input("Opcion:"))
                if(opcion == 1):
                    print("Tu tamagochi ha comido")
                    t.turno()
                    t.alimentar()
                    time.sleep(1)
                    break 
                if(opcion == 2):
                    print("Tu tamagochi esta contento")
                    t.turno()
                    t.jugar()
                    time.sleep(1) 
                    break
            except:
                print("Escoja una de las dos opciones!!(1 ó 2)")
    else:
        print("Has perdido! ;-;")
        break