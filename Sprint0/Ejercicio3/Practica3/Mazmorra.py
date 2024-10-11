from Heroe import Heroe
from Tesoro import Tesoro
import random
import time

from Monstruo import Monstruo


class Mazmorra:
    def __init__(self, heroe):
        self.heroe = heroe
        # Lista de monstruos ahora usando la clase Monstruo
        self.monstruos = [Monstruo("Orco"), Monstruo("Dragón")]
        self.tesoro = Tesoro()

    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos:
            if not self.heroe.esta_vivo():
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            self.enfrentar_enemigo(monstruo)

        if self.heroe.esta_vivo():
            print(f"¡{self.heroe.nombre_heroe} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")
        else:
            print("Héroe ha sido derrotado en la mazmorra.")

    def enfrentar_enemigo(self, enemigo):
        print(f"Te has encontrado con un {enemigo.nombre_monstruo}.")
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input()

            if opcion == "1":
                self.heroe.atacar(enemigo)
                if enemigo.esta_vivo():
                    enemigo.atacar(self.heroe)
            elif opcion == "2":
                self.heroe.defenderse()
                enemigo.atacar(self.heroe)
                self.heroe.reset_defensa()
            elif opcion == "3":
                self.heroe.curarse()
                enemigo.atacar(self.heroe)
            else:
                print("Opción no válida.")

        if self.heroe.esta_vivo():
            print(f"¡Has derrotado a {enemigo.nombre_monstruo}!")
            self.buscar_tesoro()

    def buscar_tesoro(self):
        print("Buscando tesoro...")
        time.sleep(2)  # Simula el tiempo de búsqueda
        self.tesoro.encontrar_tesoro(self.heroe)

