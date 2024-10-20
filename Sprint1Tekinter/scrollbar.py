import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Texto con Scrollbar")
root.geometry("700x500")

# Crear un marco (frame) para contener el Text y la Scrollbar
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Crear el widget Text con un tamaño grande para acomodar texto largo
text_widget = tk.Text(frame, wrap=tk.WORD)
text_widget.grid(row=0, column=0, sticky="nsew")

# Crear la barra de desplazamiento vertical
scroll_vert = ttk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
scroll_vert.grid(row=0, column=1, sticky="ns")

# Configurar el Text para que funcione con la Scrollbar
text_widget.config(yscrollcommand=scroll_vert.set)

# Configurar el frame para que se expanda correctamente
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Agregar texto largo al widget Text
long_text = """Un final electrizante
Redactado por: GM Alex Colovic

En un final muy emocionante y tenso, con tres equipos luchando por convertirse en campeones
de España,fue el equipo DuoBeniajan Costa Cálida el que consiguió el título, siendo el único
de los tres que logró ganar su encuentro.
DuoBeniajan venció a Magic Extremadura por 4-2. En los primeros cuatro tableros, los jugadores
hicieron tablas, pero en los últimos dos, el GM José Francisco Cuenca Jiménez y el MI Marcos 
Camacho Collados lograron victorias clave. Lo notable es que ambos jugadores ganaron sus dos 
y tres últimas partidas, respectivamente, justo cuando más se necesitaba.

El equipo que lideró la mayor parte del campeonato, MyInvestor Casablanca, no pudo ganar su 
último encuentro contra FCC Medio Ambiente Benalmádena. El empate 3-3 no dejó satisfecho a nadie:
MyInvestor quedó segundo en la clasificación final, perdiendo el título, mientras que FCC Medio 
Ambiente Benalmádena terminó en séptimo lugar, lo que significó su descenso a primera división.

El GM Miguel Illescas Córdoba (MyInvestor) ganó su primera partida en el campeonato y la MI 
Sabrina Vega Gutiérrez (MyInvestor) consiguió su tercera victoria, pero las derrotas en el primer 
tablero, donde el GM Pranav (Benalmádena) venció al GM David Antón Guijarro, y en el quinto, donde
el MI Yingrui Lin (Benalmádena) superó al GM Pedro Antonio Ginés Esteo, llevaron a un empate 
en el match.

El tercer contendiente antes de la última ronda, C.A. Silla Integrant Collectius, perdió ante 
C.A. Solvay por 3.5-2.5. El GM Chitambaram Aravindh derrotó al GM Kiril Alekseenko y el 
MI Enrique Tejedor Fuente venció a Jesús Alberto Valera Raga, mientras que la única victoria 
para Silla la consiguió el GM Daniil Yuffa contra el GM Lance Henderson de La Fuente.

El último encuentro fue entre Andreu Paterna y Sestao Hotel Naval, y terminó en empate 3-3. 
El GM Shamsiddin Vokhidov y el MI Diego Macías Pino ganaron sus partidas por Andreu Paterna,
 mientras que el GM Abhimanyu Puranik y la MI Karina Ambartsumova lo hicieron por Sestao Hotel Naval.
...
"""
text_widget.insert(tk.END, long_text)

# Iniciar el bucle principal
root.mainloop()