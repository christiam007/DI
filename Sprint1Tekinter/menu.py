import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def abrir_archivo():
    messagebox.showinfo("Abrir", "Función 'Abrir archivo' no implementada en este ejemplo.")

def salir():
    ventana.quit()

def acerca_de():
    messagebox.showinfo("Acerca de", "Ejemplo de menú en Tkinter\nCreado para el Ejercicio 9")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 9: Menu")
ventana.geometry("300x200")

# Crear la barra de menú
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear el menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Crear el menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)

# Añadir un widget al cuerpo de la ventana
etiqueta = ttk.Label(ventana, text="Ventana con menú")
etiqueta.pack(expand=True)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()