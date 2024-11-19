import tkinter as tk
from tkinter import ttk, messagebox

# Creación de la ventana principal al inicio del script
root = tk.Tk()
root.title("Registro")
root.geometry("400x500")

# Lista para almacenar los usuarios
usuarios = []

def crear_widgets():
    global nombre, edad, genero_var, lista_usuarios

    # Creación de etiqueta y campo de entrada para el nombre
    tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
    nombre = tk.Entry(root)
    nombre.grid(row=0, column=1, padx=5, pady=5)

    # Creación de etiqueta y escala para la edad
    tk.Label(root, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
    edad = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
    edad.grid(row=1, column=1, padx=5, pady=5)

    # Creación de etiqueta y botones de radio para el género
    tk.Label(root, text="Género:").grid(row=2, column=0, padx=5, pady=5)
    genero_var = tk.StringVar(value="masculino")
    tk.Radiobutton(root, text="Masculino", variable=genero_var, value="masculino").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(root, text="Femenino", variable=genero_var, value="femenino").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(root, text="Otro", variable=genero_var, value="otro").grid(row=4, column=1, sticky="w")

    # Botón para añadir usuario
    tk.Button(root, text="Añadir Usuario", command=anadir_usuario).grid(row=5, column=0, columnspan=2, pady=10)

    # Lista para mostrar usuarios y barra de desplazamiento
    lista_usuarios = tk.Listbox(root, width=50, height=10)
    lista_usuarios.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
    scrollbar = tk.Scrollbar(root, orient="vertical")
    scrollbar.grid(row=6, column=2, sticky="ns")
    lista_usuarios.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=lista_usuarios.yview)

    # Botón para eliminar usuario
    tk.Button(root, text="Eliminar Usuario", command=eliminar_usuario).grid(row=7, column=0, columnspan=2, pady=5)

    # Botón para salir de la aplicación
    tk.Button(root, text="Salir", command=root.quit).grid(row=8, column=0, columnspan=2, pady=5)

    # Creación del menú
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=filemenu)
    filemenu.add_command(label="Guardar Lista", command=guardar_lista)
    filemenu.add_command(label="Cargar Lista", command=cargar_lista)

def eliminar_usuario():
    try:
        index = lista_usuarios.curselection()[0]
        lista_usuarios.delete(index)
        usuarios.pop(index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un usuario para eliminar.")

def anadir_usuario():
    nombre_valor = nombre.get()
    edad_valor = edad.get()
    genero = genero_var.get()

    if nombre_valor:
        usuario = f"{nombre_valor} - {edad_valor} años - {genero}"
        usuarios.append(usuario)
        lista_usuarios.insert(tk.END, usuario)
        nombre.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un nombre.")

def guardar_lista():
    messagebox.showinfo("Información", "Lista guardada exitosamente.")

def cargar_lista():
    messagebox.showinfo("Información", "Lista cargada exitosamente.")

# Crear los widgets
crear_widgets()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()