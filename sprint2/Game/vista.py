import tkinter as tk
from PIL import Image, ImageTk


class MenuPrincipal:
    def __init__(self, root, iniciar_juego_callback, mostrar_estadisticas_callback, salir_callback):
        # Configuración inicial
        self.root = root
        self.root.configure(bg="#2C3E50")
        self.iniciar_juego_callback = iniciar_juego_callback
        self.mostrar_estadisticas_callback = mostrar_estadisticas_callback
        self.salir_callback = salir_callback

        self._crear_interfaz_principal()

    def _crear_interfaz_principal(self):
        """Crea y configura los elementos principales de la interfaz"""
        # Frame principal
        self.frame = tk.Frame(self.root, bg="#2C3E50", padx=40, pady=30)
        self.frame.pack(expand=True)

        # Título del juego
        self._crear_titulo()

        # Configuración de botones
        estilo_boton = self._obtener_estilo_boton()
        self._crear_botones(estilo_boton)

    def _crear_titulo(self):
        """Crea y configura el título del juego"""
        self.etiqueta_titulo = tk.Label(
            self.frame,
            text="🎮 Memory Game 🎮",
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=20
        )
        self.etiqueta_titulo.pack()

    def _obtener_estilo_boton(self):
        """Define el estilo común para todos los botones"""
        return {
            'font': ('Helvetica', 12, 'bold'),
            'width': 15,
            'pady': 8,
            'bd': 0,
            'borderwidth': 0,
        }

    def _crear_botones(self, estilo_boton):
        """Crea los botones del menú principal"""
        # Botón Jugar
        self.boton_inicio = tk.Button(
            self.frame,
            text="▶️ Jugar",
            command=self.iniciar_juego_callback,
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            **estilo_boton
        )
        self.boton_inicio.pack(pady=10)

        # Botón Estadísticas
        self.boton_estadisticas = tk.Button(
            self.frame,
            text="📊 Estadísticas",
            command=self.mostrar_estadisticas_callback,
            bg="#2ECC71",
            fg="white",
            activebackground="#27AE60",
            activeforeground="white",
            **estilo_boton
        )
        self.boton_estadisticas.pack(pady=10)

        # Botón Salir
        self.boton_salir = tk.Button(
            self.frame,
            text="🚪 Salir",
            command=self.salir_callback,
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            **estilo_boton
        )
        self.boton_salir.pack(pady=10)

    def pedir_nombre_jugador(self):
        """Muestra diálogo para ingresar nombre del jugador"""
        # Configuración de la ventana
        ventana_nombre = self._crear_ventana_nombre()

        # Crear elementos de la interfaz
        marco_principal = self._crear_marco_nombre(ventana_nombre)
        entrada_nombre = self._crear_elementos_nombre(marco_principal)

        # Variable para el nombre
        nombre_jugador = tk.StringVar()

        # Configurar acciones
        def confirmar_nombre():
            nombre = entrada_nombre.get().strip()
            if nombre:
                nombre_jugador.set(nombre)
                ventana_nombre.destroy()

        # Botón confirmar
        self._crear_boton_confirmar(marco_principal, confirmar_nombre)

        # Vincular tecla Enter
        entrada_nombre.bind('<Return>', lambda e: confirmar_nombre())

        # Esperar y retornar
        ventana_nombre.wait_window()
        return nombre_jugador.get() if nombre_jugador.get() else None

    def _crear_ventana_nombre(self):
        """Crea y configura la ventana de diálogo"""
        ventana_nombre = tk.Toplevel(self.root)
        ventana_nombre.title("Nombre del Jugador")
        ventana_nombre.configure(bg="#2C3E50")
        ventana_nombre.transient(self.root)
        ventana_nombre.grab_set()

        # Centrar ventana
        ancho, alto = 350, 200
        x = self.root.winfo_x() + (self.root.winfo_width() - ancho) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - alto) // 2
        ventana_nombre.geometry(f"{ancho}x{alto}+{x}+{y}")

        return ventana_nombre

    def _crear_marco_nombre(self, ventana):
        """Crea el marco principal para el diálogo de nombre"""
        marco = tk.Frame(ventana, bg="#2C3E50", padx=20, pady=20)
        marco.pack(expand=True, fill='both')

        tk.Label(
            marco,
            text="👤 Ingresa tu Nombre",
            font=("Helvetica", 16, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=10
        ).pack()

        return marco

    def _crear_elementos_nombre(self, marco):
        """Crea los elementos de entrada de nombre"""
        marco_entrada = tk.Frame(marco, bg="#2C3E50")
        marco_entrada.pack(pady=10)

        entrada_nombre = tk.Entry(
            marco_entrada,
            font=("Helvetica", 12),
            width=25,
            justify='center',
            bg="white",
            fg="#2C3E50",
            insertbackground="#2C3E50"
        )
        entrada_nombre.pack(pady=(0, 5))
        entrada_nombre.focus()

        # Línea decorativa
        canvas = tk.Canvas(
            marco_entrada,
            height=2,
            width=200,
            bg="#2C3E50",
            highlightthickness=0
        )
        canvas.pack()
        canvas.create_line(0, 1, 200, 1, fill="#3498DB", width=2, smooth=True)

        return entrada_nombre

    def _crear_boton_confirmar(self, marco, comando):
        """Crea el botón de confirmación"""
        tk.Button(
            marco,
            text="Confirmar",
            command=comando,
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            activeforeground="white",
            font=("Helvetica", 12, "bold"),
            bd=0,
            padx=20,
            pady=5,
            cursor="hand2"
        ).pack(pady=15)


class VistaJuego:
    def __init__(self, root, modelo_juego, controlador_juego):
        self.root = root
        self.modelo_juego = modelo_juego
        self.controlador_juego = controlador_juego

        # Inicialización de componentes
        self._inicializar_componentes()

    def _inicializar_componentes(self):
        """Inicializa los componentes principales del juego"""
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Estructuras de datos
        self.cartas_volteadas = []
        self.botones = []
        self.cartas_emparejadas = []

        # Crear elementos UI
        self._crear_etiquetas()

    def _crear_etiquetas(self):
        """Crea las etiquetas de tiempo y movimientos"""
        self.etiqueta_tiempo = tk.Label(
            self.frame,
            text="Tiempo: 0s",
            font=("Arial", 14)
        )
        self.etiqueta_tiempo.grid(row=10, column=0, columnspan=2, pady=10)

        self.etiqueta_movimientos = tk.Label(
            self.frame,
            text="Movimientos: 0",
            font=("Arial", 14)
        )
        self.etiqueta_movimientos.grid(row=10, column=2, columnspan=2, pady=10)

    def crear_tablero(self):
        """Crea el tablero de juego"""
        num_cartas = len(self.modelo_juego.tablero)

        for fila in range(self.modelo_juego.filas):
            for columna in range(self.modelo_juego.columnas):
                indice = fila * self.modelo_juego.columnas + columna
                if indice < num_cartas:
                    self._crear_carta(fila, columna, indice)

        self._configurar_grid()

    def _crear_carta(self, fila, columna, indice):
        """Crea un botón de carta individual"""
        boton_carta = tk.Button(
            self.frame,
            text="",
            image=self.controlador_juego.imagen_oculta,
            width=100,
            height=100,
            compound='center',
            command=lambda idx=indice: self.controlador_juego.al_hacer_clic_carta(idx)
        )
        boton_carta.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")
        self.botones.append(boton_carta)

    def _configurar_grid(self):
        """Configura el grid del tablero"""
        for i in range(self.modelo_juego.filas):
            self.frame.grid_rowconfigure(i, weight=1, uniform="equal")
        for j in range(self.modelo_juego.columnas):
            self.frame.grid_columnconfigure(j, weight=1, uniform="equal")

    def actualizar_tablero(self, seleccionadas, emparejadas=False):
        """Actualiza el estado visual de las cartas"""
        for indice, valor_carta in seleccionadas:
            if emparejadas:
                self._marcar_carta_emparejada(indice)
            else:
                self._mostrar_carta(indice, valor_carta)

    def _marcar_carta_emparejada(self, indice):
        """Marca una carta como emparejada"""
        self.botones[indice].config(state="disabled", relief="sunken")
        self.cartas_emparejadas.append(indice)

    def _mostrar_carta(self, indice, valor_carta):
        """Muestra la imagen o valor de una carta"""
        if self.controlador_juego.imagenes and valor_carta < len(self.controlador_juego.imagenes):
            self._mostrar_imagen_carta(indice, valor_carta)
        else:
            self.botones[indice].config(text=f"Carta {valor_carta + 1}")

    def _mostrar_imagen_carta(self, indice, valor_carta):
        """Muestra la imagen de una carta"""
        img = self.controlador_juego.imagenes[valor_carta].resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        self.botones[indice].config(image=img_tk, text="", relief="sunken")
        self.botones[indice].image = img_tk

    def reiniciar_cartas(self, indice_carta1, indice_carta2):
        """Oculta las cartas no emparejadas"""
        for indice in [indice_carta1, indice_carta2]:
            self.botones[indice].config(
                text="",
                image=self.controlador_juego.imagen_oculta,
                relief="raised"
            )

    def actualizar_tiempo(self, tiempo):
        """Actualiza el contador de tiempo"""
        self.etiqueta_tiempo.config(text=f"Tiempo: {tiempo}s")

    def actualizar_movimientos(self, movimientos):
        """Actualiza el contador de movimientos"""
        self.etiqueta_movimientos.config(text=f"Movimientos: {movimientos}")