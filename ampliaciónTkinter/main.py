import tkinter as tk
from modelo import NotasModel
from vista import VistaNotas
from controlador import ControladorNotas

def main():
    root = tk.Tk()
    modelo = NotasModel()
    vista = VistaNotas(root)
    controlador = ControladorNotas(modelo, vista)
    root.mainloop()

if __name__ == "__main__":
    main()