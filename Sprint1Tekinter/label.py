import tkinter as tk
from tkinter import ttk

def cambiar_texto():
    etiqueta_variable.config(text="¡¡¡¡¡¡¡¡Has hecho clic en el botón!!!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 1: Label")
ventana.geometry("300x200")

# Primera etiqueta: mensaje de bienvenida
etiqueta_bienvenida = ttk.Label(ventana, text="¡Bienvenido a mi aplicación!")
etiqueta_bienvenida.pack(pady=10)

# Segunda etiqueta: tu nombre
etiqueta_nombre = ttk.Label(ventana, text="Mi nombre es Christian")
etiqueta_nombre.pack(pady=10)

# Tercera etiqueta: cambiará con el botón
etiqueta_variable = ttk.Label(ventana, text="Esta etiqueta cambiará")
etiqueta_variable.pack(pady=10)

# Botón para cambiar el texto de la tercera etiqueta
boton_cambiar = ttk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton_cambiar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()