import time


class Monstruo:
    nombre_monstruo = ''
    ataque = 0
    defensa = 0
    salud = 0

    def __init__(self, nombre_monstruo):
        self.nombre_monstruo = nombre_monstruo
        self.ataque = 20
        self.defensa = 10
        self.salud = 100

    def atacar(self, heroe):
        self.danio = self.ataque - heroe.defensa
        if heroe.defensa > self.danio:
            print(f'El Heroe ha bloqueado el ataque')
        else:
            heroe.recibir_danio(self.danio)
            print(f'El monstruo ataca a {heroe.nombre_heroe}')
            print(f'El heroe {heroe.nombre_heroe} ha recibido {self.danio} puntos de daño')

    def recibir_danio(self, danio):
        self.salud -= danio

    def esta_vivo(self):
        if self.salud > 0:
            return True
        else:
            print(f'{self.nombre_monstruo} ha muerto')
            return False








