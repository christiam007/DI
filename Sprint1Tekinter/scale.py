import tkinter as tk
from tkinter import ttk

def actualizar_etiqueta(valor):
    etiqueta_valor.config(text=f"Valor seleccionado: {int(float(valor))}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 11: Scale")
ventana.geometry("300x200")

# Crear un frame para organizar los widgets
frame = ttk.Frame(ventana, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Crear la barra deslizante (Scale)
barra_deslizante = ttk.Scale(frame,from_=0, to=100, orient=tk.HORIZONTAL, length=200, command=actualizar_etiqueta)
barra_deslizante.pack(pady=20)

# Crear la etiqueta para mostrar el valor
etiqueta_valor = ttk.Label(frame, text="Valor seleccionado: 0")
etiqueta_valor.pack()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()