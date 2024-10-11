import time


class Heroe:
    INCREMENTO_SALUD = 10
    nombre_heroe = ''
    ataque = 0
    defensa = 0
    salud = 0
    salud_maxima = 0

    def __init__(self, nombre_heroe):
        self.nombre_heroe = nombre_heroe
        self.ataque = 30
        self.defensa = 20
        self.salud_maxima = 100
        self.salud = self.salud_maxima

    def atacar(self, enemigo):
        self.danio = self.ataque - enemigo.defensa
        if enemigo.defensa > self.danio:
            print(f'El enemigo ha bloqueado el ataque')
        else:
            enemigo.recibir_danio(self.danio)
            print(f'Heroe ataca a {enemigo.nombre_monstruo}')
            print(f'El enemigo {enemigo.nombre_monstruo} ha recibido {self.danio} puntos de daño')

    def curarse(self):
        self.salud = self.salud + self.INCREMENTO_SALUD
        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima
        print(f'Heroe se ha curado. Salud actual: {self.salud}')

    def defenderse(self):
        self.defensa += 5

        print(f'Heroe se defiende.Defensa aumentada temporalmente a {self.defensa}')

    def reset_defensa(self):
        self.defensa -= 5
        print(f'La defensa aumentada de {self.nombre_heroe} vuelve a la normalidad')

    def recibir_danio(self, danio):
        self.salud -= danio

    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            print(f'{self.nombre_heroe} ha muerto')
            return False








