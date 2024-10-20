import tkinter as tk
from tkinter import ttk


def dibujar_formas():
    # Limpiar el canvas
    canvas.delete("all")

    try:
        # Obtener coordenadas para el círculo
        cx = int(entrada_cx.get())
        cy = int(entrada_cy.get())
        radio = int(entrada_radio.get())

        # Obtener coordenadas para el rectángulo
        rx1 = int(entrada_rx1.get())
        ry1 = int(entrada_ry1.get())
        rx2 = int(entrada_rx2.get())
        ry2 = int(entrada_ry2.get())

        # Dibujar círculo
        canvas.create_oval(cx - radio, cy - radio, cx + radio, cy + radio, fill="red")

        # Dibujar rectángulo
        canvas.create_rectangle(rx1, ry1, rx2, ry2, fill="blue")

        etiqueta_resultado.config(text="Formas dibujadas con éxito")
    except ValueError:
        etiqueta_resultado.config(text="Por favor, ingrese valores numéricos válidos")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 7: Canvas")
ventana.geometry("400x500")

# Crear un frame para los controles
frame_controles = ttk.Frame(ventana, padding="10")
frame_controles.pack(fill=tk.X)

# Entradas para el círculo
ttk.Label(frame_controles, text="Círculo (cx, cy, radio):").grid(row=0, column=0, columnspan=3)
entrada_cx = ttk.Entry(frame_controles, width=5)
entrada_cx.grid(row=1, column=0)
entrada_cy = ttk.Entry(frame_controles, width=5)
entrada_cy.grid(row=1, column=1)
entrada_radio = ttk.Entry(frame_controles, width=5)
entrada_radio.grid(row=1, column=2)

# Entradas para el rectángulo
ttk.Label(frame_controles, text="Rectángulo (x1, y1, x2, y2):").grid(row=2, column=0, columnspan=4)
entrada_rx1 = ttk.Entry(frame_controles, width=5)
entrada_rx1.grid(row=3, column=0)
entrada_ry1 = ttk.Entry(frame_controles, width=5)
entrada_ry1.grid(row=3, column=1)
entrada_rx2 = ttk.Entry(frame_controles, width=5)
entrada_rx2.grid(row=3, column=2)
entrada_ry2 = ttk.Entry(frame_controles, width=5)
entrada_ry2.grid(row=3, column=3)

# Botón para dibujar
boton_dibujar = ttk.Button(frame_controles, text="Dibujar", command=dibujar_formas)
boton_dibujar.grid(row=4, column=0, columnspan=4, pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(frame_controles, text="")
etiqueta_resultado.grid(row=5, column=0, columnspan=4)

# Crear el canvas
canvas = tk.Canvas(ventana, width=300, height=300, bg="white")
canvas.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()