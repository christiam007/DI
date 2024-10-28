import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class VistaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Notas")
        self.root.geometry("600x800")
        self.setup_ui()

    def setup_ui(self):
        # Título
        self.titulo = ttk.Label(self.root, text="Gestor de Notas", font=('Helvetica', 16))
        self.titulo.pack(pady=10)

        # Frame para la entrada de notas
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(fill='x', padx=10)

        # Entry para nuevas notas
        self.entry_nota = ttk.Entry(self.frame_entrada)
        self.entry_nota.pack(side='left', fill='x', expand=True, padx=(0, 5))

        # Botón agregar
        self.btn_agregar = ttk.Button(self.frame_entrada, text="Agregar Nota")
        self.btn_agregar.pack(side='right')

        # Listbox para las notas
        self.frame_listbox = ttk.Frame(self.root)
        self.frame_listbox.pack(fill='both', expand=True, padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame_listbox)
        self.listbox.pack(side='left', fill='both', expand=True)

        # Scrollbar para el Listbox
        self.scrollbar = ttk.Scrollbar(self.frame_listbox)
        self.scrollbar.pack(side='right', fill='y')

        # Conectar scrollbar con listbox
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        # Frame para botones
        self.frame_botones = ttk.Frame(self.root)
        self.frame_botones.pack(fill='x', padx=10, pady=5)

        # Botones
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar Nota")
        self.btn_eliminar.pack(side='left', padx=5)

        self.btn_guardar = ttk.Button(self.frame_botones, text="Guardar Notas")
        self.btn_guardar.pack(side='left', padx=5)

        self.btn_cargar = ttk.Button(self.frame_botones, text="Cargar Notas")
        self.btn_cargar.pack(side='left', padx=5)

        self.btn_descargar = ttk.Button(self.frame_botones, text="Descargar Imagen")
        self.btn_descargar.pack(side='left', padx=5)

        # Label para coordenadas
        self.lbl_coordenadas = ttk.Label(self.root, text="Coordenadas: ")
        self.lbl_coordenadas.pack(pady=5)

        # Label para la imagen
        self.lbl_imagen = ttk.Label(self.root)
        self.lbl_imagen.pack(pady=10)

    def mostrar_imagen(self, imagen):
        self.imagen_tk = ImageTk.PhotoImage(imagen)
        self.lbl_imagen.config(image=self.imagen_tk)

    def actualizar_coordenadas(self, x, y):
        self.lbl_coordenadas.config(text=f"Coordenadas: x={x}, y={y}")