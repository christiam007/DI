import sys
import tkinter as tk
from io import BytesIO
from tkinter import simpledialog, messagebox
import threading
import requests
from PIL import Image, ImageTk


from modelo import ModeloJuego
from vista import VistaJuego, MenuPrincipal
from recursos import descargar_imagen


class ControladorJuego:
    def __init__(self, root):
        self.root = root
        self.nombre_jugador = ""
        self.dificultad = ""
        self.modelo_juego = None
        self.vista_juego = None
        self.seleccionadas = []
        self.contador_movimientos = 0
        self.tiempo_inicio = 0
        self.imagenes_cargadas = False

        # URLs de imágenes
        self.url_imagen_oculta = "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/fidee.png"
        self.urls_imagenes_por_dificultad = {
            "facil": [
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Adams.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Andreikin.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anton.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Christiansen.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Fedoseev.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Gelfand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Grischuk.jpg",
            ],
            "medio": [
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Adams.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Andreikin.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anton.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Christiansen.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Fedoseev.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Gelfand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Grischuk.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Morozevich.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/nakamura.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Nepomniachtchi.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/raport.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/topalov.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/julio.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Wang.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Nihal.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Pichot.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Navara.jpg",

            ],
            "dificil": [
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Adams.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Andreikin.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Anton.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Christiansen.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Fedoseev.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Gelfand.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Grischuk.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Morozevich.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/nakamura.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/Nepomniachtchi.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/raport.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/So.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/main/topalov.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Goryachkina.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Hou.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Ju.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Koneru.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Lagno.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Lei.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Mariya.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Muzychuk.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Yip.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Abrahamyan.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Ambartsumova.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Hoang.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Rapport.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Lazarne.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Be.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Calzetta.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Zhang.jpg",
                "https://raw.githubusercontent.com/christiam007/fotos-memory/refs/heads/main/Ryjanova.jpg",
            ]
        }
        self.imagenes = []

        # Creación e inicialización del menú principal
        self.menu_principal = MenuPrincipal(
            self.root,
            self.callback_iniciar_juego,
            self.mostrar_estadisticas,
            self.callback_salir  #
        )

    def callback_iniciar_juego(self):
        """
        Inicia el juego y muestra las opciones de dificultad disponibles para que el usuario seleccione.
        """

        self.modelo_juego = None
        self.vista_juego = None
        self.seleccionadas = []
        self.contador_movimientos = 0
        self.tiempo_inicio = 0
        self.imagenes_cargadas = False
        self.imagenes = []

        # Despliega las opciones de dificultad
        self.mostrar_seleccion_dificultad()

    def mostrar_seleccion_dificultad(self):
        """
        Establece la dificultad y prepara el tablero para comenzar el juego.
        """

        ventana_dificultad = tk.Toplevel(self.root)
        ventana_dificultad.title("Seleccionar Dificultad")
        ventana_dificultad.configure(bg="#2C3E50")

        # Genera la interfaz de la ventana emergente
        ventana_dificultad.transient(self.root)
        ventana_dificultad.grab_set()

        # Configura coordenadas centrales de la ventana
        ancho = 400
        alto = 300
        x = self.root.winfo_x() + (self.root.winfo_width() - ancho) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - alto) // 2
        ventana_dificultad.geometry(f"{ancho}x{alto}+{x}+{y}")

        # Ventana principal de la aplicación
        marco_principal = tk.Frame(ventana_dificultad, bg="#2C3E50", padx=20, pady=20)
        marco_principal.pack(expand=True, fill='both')

        # Elemento título de la interfaz
        tk.Label(
            marco_principal,
            text="🎯 Selecciona la Dificultad",
            font=("Helvetica", 16, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=15
        ).pack()


        dificultad_seleccionada = tk.StringVar()

        def seleccionar_dificultad(dificultad):
            dificultad_seleccionada.set(dificultad)
            self.dificultad = dificultad
            ventana_dificultad.destroy()

        # Estilos predeterminados de botones
        estilo_boton = {
            'font': ('Helvetica', 12, 'bold'),
            'width': 15,
            'pady': 8,
            'bd': 0,
            'borderwidth': 0,
        }

        # Panel para grupo de botones
        marco_botones = tk.Frame(marco_principal, bg="#2C3E50")
        marco_botones.pack(pady=20)

        # Botón Fácil
        tk.Button(
            marco_botones,
            text="🟢 Nivel Fácil",
            command=lambda: seleccionar_dificultad("facil"),
            bg="#2ECC71",
            fg="white",
            activebackground="#27AE60",
            activeforeground="white",
            **estilo_boton
        ).pack(pady=10)

        # Botón Medio
        tk.Button(
            marco_botones,
            text="🟡 Nivel Medio",
            command=lambda: seleccionar_dificultad("medio"),
            bg="#F1C40F",
            fg="white",
            activebackground="#F39C12",
            activeforeground="white",
            **estilo_boton
        ).pack(pady=10)

        # Botón Difícil
        tk.Button(
            marco_botones,
            text="🔴 Nivel Difícil",
            command=lambda: seleccionar_dificultad("dificil"),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            activeforeground="white",
            **estilo_boton
        ).pack(pady=10)

        # Pausar ejecución hasta que se elija nivel de dificultad
        self.root.wait_window(ventana_dificultad)

        # Termina ejecución si el usuario no eligió dificultad
        if not hasattr(self, 'dificultad'):
            return

        # Solicita ingreso del nombre del usuario
        self.nombre_jugador = self.menu_principal.pedir_nombre_jugador()
        if self.nombre_jugador is None:
            return

        # Comienza la ejecución del juego
        self.modelo_juego = ModeloJuego(self.dificultad)
        self.mostrar_ventana_carga()
        self.iniciar_hilo_carga_imagenes()

    def mostrar_ventana_carga(self):
        """
        Presenta pantalla de espera mientras se obtienen las imágenes del sistema.
        """
        if hasattr(self, 'ventana_carga') and self.ventana_carga.winfo_exists():
            self.ventana_carga.destroy()

        self.ventana_carga = tk.Toplevel(self.root)
        self.ventana_carga.title("Cargando imágenes")
        self.ventana_carga.configure(bg="#2C3E50")

        ancho_ventana = 300
        alto_ventana = 150
        ancho_pantalla = self.ventana_carga.winfo_screenwidth()
        alto_pantalla = self.ventana_carga.winfo_screenheight()

        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2

        self.ventana_carga.geometry(f'{ancho_ventana}x{alto_ventana}+{x}+{y}')
        self.ventana_carga.resizable(False, False)

        marco = tk.Frame(self.ventana_carga, bg="#2C3E50")
        marco.pack(expand=True, fill='both', padx=20, pady=20)

        self.etiqueta_carga = tk.Label(
            marco,
            text="Cargando imágenes....",
            font=("Helvetica", 14, "bold"),
            fg="white",
            bg="#2C3E50"
        )
        self.etiqueta_carga.pack(pady=20)

        self.etiqueta_progreso = tk.Label(
            marco,
            text="⏳",
            font=("Helvetica", 24),
            fg="white",
            bg="#2C3E50"
        )
        self.etiqueta_progreso.pack(pady=10)

        self.animar_icono_carga()

        self.ventana_carga.protocol("WM_DELETE_WINDOW", lambda: None)
        self.ventana_carga.transient(self.root)
        self.ventana_carga.grab_set()

    def animar_icono_carga(self):
        try:
            if (hasattr(self, 'ventana_carga') and
                    self.ventana_carga.winfo_exists() and
                    hasattr(self, 'etiqueta_progreso') and
                    self.etiqueta_progreso.winfo_exists()):
                texto_actual = self.etiqueta_progreso.cget("text")
                self.etiqueta_progreso.configure(text="⌛" if texto_actual == "⏳" else "⏳")
                self.ventana_carga.after(500, self.animar_icono_carga)
        except Exception as e:
            pass

    def iniciar_hilo_carga_imagenes(self):
        """
        Crea un hilo secundario dedicado a la obtención de imágenes.
        """
        threading.Thread(target=self.cargar_imagenes).start()

    def cargar_imagenes(self):
        try:
            # Carga imagen posterior de las cartas
            respuesta = requests.get(self.url_imagen_oculta)
            img_oculta = Image.open(BytesIO(respuesta.content))
            img_oculta = img_oculta.resize((100, 100))
            self.imagen_oculta = ImageTk.PhotoImage(img_oculta)

            # Carga el conjunto de imágenes para las cartas
            urls_dificultad = self.urls_imagenes_por_dificultad.get(self.dificultad, [])
            for url in urls_dificultad:
                threading.Thread(target=self.iniciar_imagen, args=(url,)).start()
        except Exception as e:
            print(f"Error al cargar imágenes: {e}")

    def iniciar_imagen(self, url):
        """
        Procesa obtención de imagen en hilo independiente del principal.
        """
        descargar_imagen(url, self.callback_imagen_descargada)

    def callback_imagen_descargada(self, imagen):
        if imagen:
            self.imagenes.append(imagen)
        else:
            print("Error al descargar una imagen.")

        self.imagenes_cargadas = True
        self.verificar_imagenes_cargadas()

    def verificar_imagenes_cargadas(self):
        try:
            urls_dificultad = self.urls_imagenes_por_dificultad.get(self.dificultad, [])
            if len(self.imagenes) == len(urls_dificultad):
                print("Se completó la carga de imágenes exitosamente")

                if hasattr(self, 'ventana_carga') and self.ventana_carga.winfo_exists():
                    self.ventana_carga.destroy()

                if hasattr(self, 'vista_juego') and self.vista_juego:
                    if hasattr(self.vista_juego, 'frame') and self.vista_juego.frame.winfo_exists():
                        self.vista_juego.frame.destroy()

                self.iniciar_ventana_juego()
        except Exception as e:
            print(f"Fallo durante comprobación de imágenes: {e}")

    def iniciar_ventana_juego(self):
        """
            Configura e inicializa la interfaz principal del juego.
            """
        self.root.withdraw()
        ventana_juego = tk.Toplevel(self.root)
        ventana_juego.title("Juego de Memoria")

        self.vista_juego = VistaJuego(ventana_juego, self.modelo_juego, self)
        self.vista_juego.crear_tablero()

        self.actualizar_tiempo()

    def mostrar_estadisticas(self):
        """Mostrar estadísticas del juego en una ventana personalizada"""
        if self.modelo_juego is None:
            messagebox.showinfo("Estadísticas", "No se encuentran datos para graficar las estadísticas")
            return

        # Crear nueva ventana
        ventana_stats = tk.Toplevel(self.root)
        ventana_stats.title("Estadísticas del Juego")
        ventana_stats.geometry("600x500")
        ventana_stats.configure(bg="#2C3E50")

        # Hacer la ventana modal
        ventana_stats.transient(self.root)
        ventana_stats.grab_set()

        # Marco principal
        marco_principal = tk.Frame(ventana_stats, bg="#2C3E50", padx=20, pady=20)
        marco_principal.pack(fill='both', expand=True)

        # Título
        tk.Label(
            marco_principal,
            text="🏆 Tabla de Clasificación 🏆",
            font=("Helvetica", 20, "bold"),
            bg="#2C3E50",
            fg="white",
            pady=15
        ).pack()

        # Crear un marco para cada dificultad
        for dificultad in ["facil", "medio", "dificil"]:
            # Marco para cada dificultad
            marco_dificultad = tk.Frame(marco_principal, bg="#34495E", padx=10, pady=10)
            marco_dificultad.pack(fill='x', padx=10, pady=5)

            # Título de la dificultad
            titulo_texto = {
                "facil": "🟢 Nivel Fácil",
                "medio": "🟡 Nivel Medio",
                "dificil": "🔴 Nivel Difícil"
            }

            tk.Label(
                marco_dificultad,
                text=titulo_texto[dificultad],
                font=("Helvetica", 14, "bold"),
                bg="#34495E",
                fg="white",
                pady=5
            ).pack()

            # Crear tabla de jugadores
            marco_tabla = tk.Frame(marco_dificultad, bg="#34495E")
            marco_tabla.pack(fill='x', padx=5)

            # Encabezados
            encabezados = ["Posición", "Jugador", "Movimientos", "Tiempo", "Fecha"]
            for i, encabezado in enumerate(encabezados):
                tk.Label(
                    marco_tabla,
                    text=encabezado,
                    font=("Helvetica", 10, "bold"),
                    bg="#34495E",
                    fg="#BDC3C7",
                    padx=5
                ).grid(row=0, column=i, sticky="w")

            # Datos de jugadores
            puntajes_dificultad = self.modelo_juego.puntajes.get(dificultad, [])

            if not puntajes_dificultad:
                tk.Label(
                    marco_tabla,
                    text="No hay registros para este nivel",
                    font=("Helvetica", 10, "italic"),
                    bg="#34495E",
                    fg="#BDC3C7",
                    pady=5
                ).grid(row=1, column=0, columnspan=5)
            else:
                for idx, puntaje in enumerate(puntajes_dificultad, 1):
                    # Medallas para los primeros lugares
                    medallas = ["🥇", "🥈", "🥉"]
                    posicion = medallas[idx - 1] if idx <= 3 else str(idx)

                    # Convertir tiempo a formato mm:ss
                    minutos = puntaje['tiempo_tomado'] // 60
                    segundos = puntaje['tiempo_tomado'] % 60
                    tiempo_formato = f"{minutos:02d}:{segundos:02d}"

                    # Crear fila de datos
                    datos = [
                        posicion,
                        puntaje['nombre'],
                        str(puntaje['movimientos']),
                        tiempo_formato,
                        puntaje['fecha'].split()[0]
                    ]

                    for col, dato in enumerate(datos):
                        tk.Label(
                            marco_tabla,
                            text=dato,
                            font=("Helvetica", 10),
                            bg="#34495E",
                            fg="white",
                            padx=5,
                            pady=2
                        ).grid(row=idx, column=col, sticky="w")

        # Botón para cerrar
        tk.Button(
            marco_principal,
            text="Cerrar",
            command=ventana_stats.destroy,
            font=("Helvetica", 12),
            bg="#E74C3C",
            fg="white",
            padx=20,
            pady=5
        ).pack(pady=15)


    def al_hacer_clic_carta(self, indice):
        """
        Gestiona el evento de selección de carta por parte del jugador.
        """
        if len(self.seleccionadas) == 2 or any(indice == sel[0] for sel in self.seleccionadas):
            return

        valor_carta = self.modelo_juego.tablero[indice]
        self.seleccionadas.append((indice, valor_carta))

        self.vista_juego.actualizar_tablero([(indice, valor_carta)])

        if len(self.seleccionadas) == 2:
            self.manejar_seleccion_cartas()

    def manejar_seleccion_cartas(self):
        """
        Compara las cartas seleccionadas para validar coincidencia.
        """
        indice1, valor1 = self.seleccionadas[0]
        indice2, valor2 = self.seleccionadas[1]

        if valor1 == valor2:
            self.vista_juego.actualizar_tablero(self.seleccionadas, emparejadas=True)
            self.verificar_victoria()
        else:
            self.root.after(1000, self.vista_juego.reiniciar_cartas, indice1, indice2)

        self.incrementar_contador_movimientos()
        self.seleccionadas = []

    def incrementar_contador_movimientos(self):
        """
         Actualiza el registro de movimientos realizados por el jugador.
         """
        self.contador_movimientos += 1
        self.vista_juego.actualizar_movimientos(self.contador_movimientos)

    def actualizar_tiempo(self):
        try:
            if (hasattr(self, 'vista_juego') and
                    self.vista_juego is not None and
                    hasattr(self.vista_juego, 'etiqueta_tiempo') and
                    self.vista_juego.etiqueta_tiempo.winfo_exists()):
                self.tiempo_inicio += 1
                self.vista_juego.actualizar_tiempo(self.tiempo_inicio)
                self.root.after(1000, self.actualizar_tiempo)
        except Exception as e:
            print(f"Fallo en la actualización del temporizador: {e}")
            return

    def verificar_victoria(self):
        """Verificar si se completó el juego"""
        if len(self.vista_juego.cartas_emparejadas) == len(self.modelo_juego.tablero):
            messagebox.showinfo("¡Felicidades!", "¡Has ganado!")
            self.modelo_juego.guardar_puntaje(
                self.nombre_jugador,
                self.contador_movimientos,
                self.tiempo_inicio
            )
            self.root.after(100, self.volver_menu_principal)

    def volver_menu_principal(self):
        try:
            if hasattr(self, 'vista_juego') and self.vista_juego:
                if hasattr(self.vista_juego.root, 'destroy'):
                    self.vista_juego.root.destroy()

                if hasattr(self.vista_juego, 'frame') and self.vista_juego.frame.winfo_exists():
                    self.vista_juego.frame.destroy()

            self.vista_juego = None
            self.seleccionadas = []
            self.contador_movimientos = 0
            self.tiempo_inicio = 0
            self.imagenes_cargadas = False
            self.imagenes = []

            if self.root and self.root.winfo_exists():
                self.root.deiconify()
        except Exception as e:
            print(f"Error al regresar al menú de inicio: {e}")

    def callback_salir(self):
        """
        Finaliza la ejecución del programa y libera recursos.
        """
        if messagebox.askokcancel("Salir", "¿Deseas salir del juego?"):
            try:
                if hasattr(self, 'vista_juego') and self.vista_juego:
                    self.vista_juego.frame.destroy()

                self.root.quit()
                self.root.destroy()
                sys.exit(0)
            except:
                sys.exit(0)