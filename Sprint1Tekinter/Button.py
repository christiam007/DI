import tkinter as tk
from tkinter import ttk

def mostrar_mensaje():
    etiqueta.config(text="¡Has presionado el botón!")

def cerrar_ventana():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 2: Button")
ventana.geometry("300x200")

# Crear una etiqueta para mostrar el mensaje
etiqueta = ttk.Label(ventana, text="")
etiqueta.pack(pady=20)

# Crear el primer botón: Mostrar mensaje
boton_mensaje = ttk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=10)

# Crear el segundo botón: Cerrar ventana
boton_cerrar = ttk.Button(ventana, text="Cerrar Ventana", command=cerrar_ventana)
boton_cerrar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()