import tkinter as tk
from tkinter import ttk

def mostrar_seleccion():
    seleccion = listbox_frutas.curselection()
    if seleccion:
        fruta = listbox_frutas.get(seleccion[0])
        etiqueta_resultado.config(text=f"Fruta seleccionada: {fruta}")
    else:
        etiqueta_resultado.config(text="Ninguna fruta seleccionada")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 6: Listbox")
ventana.geometry("300x300")

# Crear un frame para organizar los widgets
frame = ttk.Frame(ventana, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Crear y configurar el Listbox
listbox_frutas = tk.Listbox(frame, height=5)
listbox_frutas.pack(pady=10, fill=tk.X)

# Añadir frutas al Listbox
frutas = ["Manzana", "Banana", "Naranja"]
for fruta in frutas:
    listbox_frutas.insert(tk.END, fruta)

# Crear el botón para mostrar la selección
boton_mostrar = ttk.Button(frame, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack(pady=10)

# Crear la etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(frame, text="Ninguna fruta seleccionada")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()