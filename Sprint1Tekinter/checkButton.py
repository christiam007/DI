import tkinter as tk
from tkinter import ttk


def actualizar_etiqueta():
    aficiones_seleccionadas = []
    if leer_var.get():
        aficiones_seleccionadas.append("Leer")
    if deporte_var.get():
        aficiones_seleccionadas.append("Deporte")
    if musica_var.get():
        aficiones_seleccionadas.append("Música")

    if aficiones_seleccionadas:
        etiqueta_resultado.config(text="Aficiones seleccionadas: " + ", ".join(aficiones_seleccionadas))
    else:
        etiqueta_resultado.config(text="Ninguna afición seleccionada")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 4: Checkbutton")
ventana.geometry("300x200")

# Variables de control para los Checkbuttons
leer_var = tk.BooleanVar()
deporte_var = tk.BooleanVar()
musica_var = tk.BooleanVar()

# Crear los Checkbuttons
check_leer = ttk.Checkbutton(ventana, text="Leer", variable=leer_var, command=actualizar_etiqueta)
check_leer.pack(pady=5)

check_deporte = ttk.Checkbutton(ventana, text="Deporte", variable=deporte_var, command=actualizar_etiqueta)
check_deporte.pack(pady=5)

check_musica = ttk.Checkbutton(ventana, text="Música", variable=musica_var, command=actualizar_etiqueta)
check_musica.pack(pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="Ninguna afición seleccionada")
etiqueta_resultado.pack(pady=20)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()