import tkinter as tk

# Función para cambiar el color de fondo según la opción seleccionada
def cambiar_color():
    color_seleccionado = color.get()  # Obtiene el valor seleccionado (rojo, verde o azul)
    ventana.config(bg=color_seleccionado)  # Cambia el color de fondo de la ventana

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Elige tu color favorito")
ventana.geometry("300x200")

# Variable para almacenar el valor del color seleccionado
color = tk.StringVar()
color.set(" ")  # Valor por defecto

# Crear los botones de opción (Radiobutton)
radio1=tk.Radiobutton(ventana, text="Rojo", variable=color, value="red", command=cambiar_color)
radio1.pack(pady=5)
radio2=tk.Radiobutton(ventana, text="Verde", variable=color, value="green", command=cambiar_color)
radio2.pack(pady=5)
radio3=tk.Radiobutton(ventana, text="Azul", variable=color, value="blue", command=cambiar_color)
radio3.pack(pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
