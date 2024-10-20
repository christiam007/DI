import tkinter as tk
from tkinter import ttk

def saludar():
    nombre = entrada_nombre.get()
    if nombre:
        etiqueta_saludo.config(text=f"¡Hola, {nombre}! Bienvenido/a.")
    else:
        etiqueta_saludo.config(text="Por favor, ingresa tu nombre.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 3: Entry")
ventana.geometry("300x200")

# Crear y colocar la etiqueta para instrucciones
etiqueta_instruccion = ttk.Label(ventana, text="Ingresa tu nombre:")
etiqueta_instruccion.pack(pady=10)

# Crear y colocar el campo de entrada
entrada_nombre = ttk.Entry(ventana)
entrada_nombre.pack(pady=5)

# Crear y colocar el botón de saludo
boton_saludar = ttk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.pack(pady=10)

# Crear y colocar la etiqueta para mostrar el saludo
etiqueta_saludo = ttk.Label(ventana, text="")
etiqueta_saludo.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()