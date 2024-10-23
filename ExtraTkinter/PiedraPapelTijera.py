import tkinter as tk
from tkinter import messagebox
import random

class PiedraPapelTijera:
    def __init__(self, master):
        """
        Constructor de la clase. Inicializa la ventana principal y las variables del juego.

        """
        self.master = master
        self.master.title("Piedra, Papel, Tijera")

        # Crear la barra de menús con las opciones de juego
        self.crear_barra_menu()

        # Variables para llevar el control del juego
        self.jugador1_puntos = 0
        self.jugador2_puntos = 0
        self.eleccion_jugador1 = None
        self.eleccion_jugador2 = None

        # Mostrar la pantalla de bienvenida
        self.mostrar_pantalla_inicial()

    def crear_barra_menu(self):
        """
        Crea la barra de menú con las opciones de juego:
        - Un Jugador (contra la computadora)
        - Dos Jugadores (modo multijugador)
        - Salir
        """
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        self.menu_juego = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Juego", menu=self.menu_juego)
        self.menu_juego.add_command(label="Un Jugador", command=self.iniciar_un_jugador)
        self.menu_juego.add_command(label="Dos Jugadores", command=self.iniciar_dos_jugadores)
        self.menu_juego.add_separator()
        self.menu_juego.add_command(label="Salir", command=self.master.quit)

    def mostrar_pantalla_inicial(self):
        """
        Muestra la pantalla de bienvenida con instrucciones para comenzar el juego
        """
        self.frame_inicial = tk.Frame(self.master)
        self.frame_inicial.pack(expand=True, pady=50)

        tk.Label(self.frame_inicial,
                text="Bienvenido a Piedra, Papel, Tijera",
                font=('Arial', 16, 'bold')).pack(pady=10)

        tk.Label(self.frame_inicial,
                text="Seleccione una opción del menú 'Juego' para comenzar",
                font=('Arial', 12)).pack(pady=5)

    def iniciar_un_jugador(self):
        """
        Inicia el modo de un jugador contra la computadora
        """
        self.modo_juego = "un_jugador"
        if hasattr(self, 'frame_inicial'):
            self.frame_inicial.pack_forget()
        self.crear_interfaz_juego()

    def iniciar_dos_jugadores(self):
        """
        Inicia el modo de dos jugadores
        """
        self.modo_juego = "dos_jugadores"
        if hasattr(self, 'frame_inicial'):
            self.frame_inicial.pack_forget()
        self.crear_interfaz_juego()

    def crear_interfaz_juego(self):
        """
        Crea la interfaz del juego con los botones y marcadores para ambos jugadores
        """
        self.frame_juego = tk.Frame(self.master)
        self.frame_juego.pack(pady=20)

        # Crear marcadores para ambos jugadores
        self.label_jugador1 = tk.Label(self.frame_juego, text="Jugador 1: 0", font=('Arial', 12))
        self.label_jugador1.pack()
        self.label_jugador2 = tk.Label(self.frame_juego, text="Jugador 2: 0", font=('Arial', 12))
        self.label_jugador2.pack()

        # Crear botones para el jugador 1
        self.frame_jugador1 = tk.Frame(self.frame_juego)
        self.frame_jugador1.pack(pady=10)
        tk.Label(self.frame_jugador1, text="Jugador 1:", font=('Arial', 10)).pack(side=tk.LEFT)

        opciones = ["Piedra", "Papel", "Tijera"]
        for opcion in opciones:
            tk.Button(self.frame_jugador1,
                     text=opcion,
                     command=lambda x=opcion: self.seleccion_jugador(x),
                     width=8).pack(side=tk.LEFT, padx=5)

        # Crear botones para el jugador 2 (solo en modo dos jugadores)
        if self.modo_juego == "dos_jugadores":
            self.frame_jugador2 = tk.Frame(self.frame_juego)
            self.frame_jugador2.pack(pady=10)
            tk.Label(self.frame_jugador2, text="Jugador 2:", font=('Arial', 10)).pack(side=tk.LEFT)

            for opcion in opciones:
                tk.Button(self.frame_jugador2,
                         text=opcion,
                         command=lambda x=opcion: self.seleccion_jugador2(x),
                         width=8).pack(side=tk.LEFT, padx=5)

    def seleccion_jugador(self, eleccion):
        """
        Procesa la selección del jugador 1

        """
        self.eleccion_jugador1 = eleccion
        if self.modo_juego == "un_jugador":
            # En modo un jugador, la computadora elige aleatoriamente
            self.eleccion_jugador2 = random.choice(["Piedra", "Papel", "Tijera"])
            self.jugar()
        else:
            self.verificar_selecciones()

    def seleccion_jugador2(self, eleccion):
        """
        Procesa la selección del jugador 2

        """
        self.eleccion_jugador2 = eleccion
        self.verificar_selecciones()

    def verificar_selecciones(self):
        """
        Verifica si ambos jugadores han hecho su elección para continuar el juego
        """
        if self.eleccion_jugador1 and self.eleccion_jugador2:
            self.jugar()

    def jugar(self):
        """
        Ejecuta una ronda del juego, determina el ganador y actualiza los puntajes
        """
        resultado = self.determinar_ganador(self.eleccion_jugador1, self.eleccion_jugador2)
        if resultado != "Empate":
            self.mostrar_resultado(self.eleccion_jugador1, self.eleccion_jugador2, resultado)
            self.actualizar_puntuacion(resultado)

        # Reiniciar elecciones para la siguiente ronda
        self.eleccion_jugador1 = None
        self.eleccion_jugador2 = None

        # Verificar si algún jugador ha ganado la partida
        if self.jugador1_puntos == 3 or self.jugador2_puntos == 3:
            self.finalizar_partida()

    def determinar_ganador(self, j1, j2):
        """
        Determina el ganador de una ronda según las reglas del juego

        """
        if j1 == j2:
            return "Empate"
        elif (j1 == "Piedra" and j2 == "Tijera") or \
             (j1 == "Papel" and j2 == "Piedra") or \
             (j1 == "Tijera" and j2 == "Papel"):
            return "Jugador 1"
        else:
            return "Jugador 2"

    def mostrar_resultado(self, j1, j2, resultado):
        """
        Muestra una ventana con el resultado de la ronda

        """
        mensaje = f"El jugador uno saca {j1}, el jugador dos saca {j2}. "
        if resultado != "Empate":
            mensaje += f"Gana el {resultado}."
        messagebox.showinfo("Resultado", mensaje)

    def actualizar_puntuacion(self, resultado):
        """
        Actualiza el marcador según el resultado de la ronda

        """
        if resultado == "Jugador 1":
            self.jugador1_puntos += 1
        elif resultado == "Jugador 2":
            self.jugador2_puntos += 1

        self.label_jugador1.config(text=f"Jugador 1: {self.jugador1_puntos}")
        self.label_jugador2.config(text=f"Jugador 2: {self.jugador2_puntos}")

    def finalizar_partida(self):
        """
        Muestra el ganador de la partida y reinicia el juego
        """
        ganador = "Jugador 1" if self.jugador1_puntos == 3 else "Jugador 2"
        messagebox.showinfo("Fin de la partida", f"¡{ganador} ha ganado la partida!")
        self.reiniciar_juego()

    def reiniciar_juego(self):
        """
        Reinicia todas las variables del juego y vuelve a la pantalla inicial
        """
        self.jugador1_puntos = 0
        self.jugador2_puntos = 0
        self.frame_juego.pack_forget()
        self.mostrar_pantalla_inicial()


# Punto de entrada del programa
if __name__ == "__main__":
    root = tk.Tk()
    juego = PiedraPapelTijera(root)
    root.mainloop()