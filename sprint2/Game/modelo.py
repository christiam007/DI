from datetime import datetime
import os
import random



class ConfiguracionTablero:
    """Define la configuración del tablero según dificultad"""

    def __init__(self, num_pares, dimensiones):
        self.num_pares = num_pares
        self.dimensiones = dimensiones


class Dificultad:
    """Constantes para niveles de dificultad"""
    FACIL = "facil"
    MEDIO = "medio"
    DIFICIL = "dificil"

    def get_config(dificultad: str):
        """Obtiene la configuración según nivel de dificultad"""
        configuraciones = {
            "facil": ConfiguracionTablero(8, (4, 4)),  # 16 cartas
            "medio": ConfiguracionTablero(18, (6, 6)),  # 36 cartas
            "dificil": ConfiguracionTablero(32, (8, 8))  # 64 cartas
        }
        if dificultad not in configuraciones:
            raise ValueError(f"Dificultad {dificultad} no reconocida")
        return configuraciones[dificultad]


class GestorPuntajes:
    """Maneja la persistencia y ordenamiento de puntajes"""
    ARCHIVO_PUNTAJES = "ranking.txt"
    MAX_PUNTAJES = 3

    def cargar():
        """Carga puntajes desde archivo"""
        puntajes = {"facil": [], "medio": [], "dificil": []}

        if not os.path.exists(GestorPuntajes.ARCHIVO_PUNTAJES):
            return puntajes

        with open(GestorPuntajes.ARCHIVO_PUNTAJES, "r") as archivo:
            for linea in archivo:
                nombre, dificultad, movimientos, tiempo, fecha = linea.strip().split(",")
                puntajes[dificultad].append({
                    "nombre": nombre,
                    "dificultad": dificultad,
                    "movimientos": int(movimientos),
                    "tiempo_tomado": int(tiempo),
                    "fecha": fecha
                })

        return GestorPuntajes._ordenar_todos(puntajes)

    def guardar(nombre: str, dificultad: str, movimientos: int, tiempo: int):
        """Guarda un nuevo puntaje en el archivo"""
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"{nombre},{dificultad},{movimientos},{tiempo},{fecha}\n"

        with open(GestorPuntajes.ARCHIVO_PUNTAJES, "a") as archivo:
            archivo.write(linea)

    def _ordenar_todos(puntajes):
        """Ordena los puntajes de todas las dificultades"""
        for dificultad in puntajes:
            puntajes[dificultad] = GestorPuntajes._ordenar_dificultad(puntajes[dificultad])
        return puntajes


    def _ordenar_dificultad(puntajes):
        """Ordena los puntajes de una dificultad específica"""
        return sorted(
            puntajes,
            key=lambda x: (x['movimientos'], x['tiempo_tomado'])
        )[:GestorPuntajes.MAX_PUNTAJES]


class ModeloJuego:
    """Modelo principal del juego de memoria"""

    def __init__(self, dificultad: str):
        self.dificultad = dificultad
        self.tiempo_iniciado = False
        self.tiempo_transcurrido = 0
        self.puntajes = GestorPuntajes.cargar()

        config = Dificultad.get_config(dificultad)
        self.tablero = self._generar_tablero(config.num_pares)
        self.filas, self.columnas = config.dimensiones

    def _generar_tablero(self, num_pares):
        """Genera un tablero aleatorio con pares de cartas"""
        cartas = [i for i in range(num_pares)] * 2
        random.shuffle(cartas)
        return cartas

    def iniciar_temporizador(self):
        """Inicia el conteo del tiempo de juego"""
        if not self.tiempo_iniciado:
            self.tiempo_iniciado = True
            self.tiempo_transcurrido = 0

    def actualizar_temporizador(self):
        """Actualiza y retorna el tiempo transcurrido"""
        if self.tiempo_iniciado:
            self.tiempo_transcurrido += 1
        return self.tiempo_transcurrido

    def guardar_puntaje(self, nombre_jugador, movimientos, tiempo_tomado):
        """Guarda el puntaje del jugador"""
        GestorPuntajes.guardar(nombre_jugador, self.dificultad, movimientos, tiempo_tomado)

        self.puntajes[self.dificultad].append({
            "nombre": nombre_jugador,
            "dificultad": self.dificultad,
            "movimientos": movimientos,
            "tiempo_tomado": tiempo_tomado,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        self.puntajes = GestorPuntajes._ordenar_todos(self.puntajes)