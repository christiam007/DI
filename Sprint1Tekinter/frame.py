import tkinter as tk
from tkinter import ttk

def mostrar_contenido():
    contenido = entrada.get()
    etiqueta_resultado.config(text=f"Contenido: {contenido}")

def borrar_contenido():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="Contenido: ")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 8: Frame")
ventana.geometry("300x200")

# Crear el Frame superior
frame_superior = ttk.Frame(ventana, padding="10")
frame_superior.pack(fill=tk.X)

# Añadir widgets al Frame superior
etiqueta1 = ttk.Label(frame_superior, text="Etiqueta 1")
etiqueta1.grid(row=0, column=0, padx=5, pady=5)

etiqueta2 = ttk.Label(frame_superior, text="Etiqueta 2")
etiqueta2.grid(row=0, column=1, padx=5, pady=5)

entrada = ttk.Entry(frame_superior)
entrada.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Crear el Frame inferior
frame_inferior = ttk.Frame(ventana, padding="10")
frame_inferior.pack(fill=tk.X)

# Añadir widgets al Frame inferior
boton_mostrar = ttk.Button(frame_inferior, text="Mostrar", command=mostrar_contenido)
boton_mostrar.grid(row=0, column=0, padx=5, pady=5)

boton_borrar = ttk.Button(frame_inferior, text="Borrar", command=borrar_contenido)
boton_borrar.grid(row=0, column=1, padx=5, pady=5)

etiqueta_resultado = ttk.Label(frame_inferior, text="Contenido: ")
etiqueta_resultado.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()