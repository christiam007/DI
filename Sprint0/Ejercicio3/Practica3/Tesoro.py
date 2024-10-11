import random


class Tesoro:
    def __init__(self):
        self.beneficios = ['aumento de ataque', 'aumento de defensa', 'restauración de salud']

    def encontrar_tesoro(self, heroe):
        beneficio = random.choice(self.beneficios)
        print(f"Héroe ha encontrado un tesoro: {beneficio}.")

        if beneficio == 'aumento de ataque':
            heroe.ataque += 10
            print(f"El ataque de {heroe.nombre_heroe} aumenta a {heroe.ataque}.")
        elif beneficio == 'aumento de defensa':
            heroe.defensa += 10
            print(f"La defensa de {heroe.nombre_heroe} aumenta a {heroe.defensa}.")
        elif beneficio == 'restauración de salud':
            heroe.salud = heroe.salud_maxima
            print(f"La salud de {heroe.nombre_heroe} ha sido restaurada a {heroe.salud}.")
