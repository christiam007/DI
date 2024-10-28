import tkinter as tk
from tkinter import messagebox
import threading
import requests
from PIL import Image
from io import BytesIO


class ControladorNotas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.configurar_eventos()

    def configurar_eventos(self):
        # Configurar botones
        self.vista.btn_agregar.config(command=self.agregar_nota)
        self.vista.btn_eliminar.config(command=self.eliminar_nota)
        self.vista.btn_guardar.config(command=self.guardar_notas)
        self.vista.btn_cargar.config(command=self.cargar_notas)
        self.vista.btn_descargar.config(command=self.descargar_imagen)

        # Configurar evento de clic
        self.vista.root.bind("<Button-1>", self.actualizar_coordenadas)

        # Cargar notas iniciales
        self.actualizar_listbox()

    def agregar_nota(self):
        nueva_nota = self.vista.entry_nota.get()
        if self.modelo.agregar_nota(nueva_nota):
            self.actualizar_listbox()
            self.vista.entry_nota.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una nota válida")

    def eliminar_nota(self):
        seleccion = self.vista.listbox.curselection()
        if seleccion:
            if self.modelo.eliminar_nota(seleccion[0]):
                self.actualizar_listbox()
        else:
            messagebox.showinfo("Info", "Por favor seleccione una nota para eliminar")

    def guardar_notas(self):
        if self.modelo.guardar_notas():
            messagebox.showinfo("Éxito", "Notas guardadas correctamente")
        else:
            messagebox.showerror("Error", "Error al guardar las notas")

    def cargar_notas(self):
        self.modelo.cargar_notas()
        self.actualizar_listbox()

    def descargar_imagen(self):
        def descarga():
            try:
                # URL de ejemplo de una imagen en GitHub
                url = "https://storage.googleapis.com/pod_public/1300/198006.jpg"
                response = requests.get(url)
                imagen = Image.open(BytesIO(response.content))
                imagen = imagen.resize((300, 300))  # Redimensionar imagen

                # Actualizar la interfaz en el hilo principal
                self.vista.root.after(0, lambda: self.vista.mostrar_imagen(imagen))
                messagebox.showinfo("Éxito", "Imagen descargada correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al descargar la imagen: {e}")

        # Iniciar la descarga en un hilo separado
        thread = threading.Thread(target=descarga)
        thread.start()

    def actualizar_coordenadas(self, event):
        # Ignorar clics en widgets
        if not isinstance(event.widget, tk.Button):
            self.vista.actualizar_coordenadas(event.x, event.y)

    def actualizar_listbox(self):
        self.vista.listbox.delete(0, tk.END)
        for nota in self.modelo.obtener_notas():
            self.vista.listbox.insert(tk.END, nota)