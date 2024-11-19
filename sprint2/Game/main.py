import sys
import tkinter as tk
from tkinter import messagebox

from controlador import ControladorJuego

def main():
    # Creamos la ventana usando Tkinter
    root = tk.Tk()
    root.title("Juego de Memoria")

    controlador = ControladorJuego(root)

    root.mainloop()

    # Implementa método de finalización del programa
    def cerrar():
        if messagebox.askokcancel("Salir", "¿Deseas salir del juego?"):
            try:
                root.quit()
                root.destroy()
                sys.exit(0)
            except:
                sys.exit(0)

    # Configura método de cierre de aplicación
    root.protocol("WM_DELETE_WINDOW", cerrar)


    controlador = ControladorJuego(root)


    # Inicia ciclo principal de eventos
    try:
        root.mainloop()
    except KeyboardInterrupt:
        cerrar()
    except Exception as error:
        print(f"Error inesperado: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()