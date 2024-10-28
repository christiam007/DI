class NotasModel:
    def __init__(self):
        self.notas = []
        self.cargar_notas()

    def agregar_nota(self, nueva_nota):
        if nueva_nota.strip():  # Verifica que la nota no esté vacía
            self.notas.append(nueva_nota)
            return True
        return False

    def eliminar_nota(self, indice):
        if 0 <= indice < len(self.notas):
            del self.notas[indice]
            return True
        return False

    def obtener_notas(self):
        return self.notas

    def guardar_notas(self):
        try:
            with open('notas.txt', 'w', encoding='utf-8') as archivo:
                for nota in self.notas:
                    archivo.write(nota + '\n')
            return True
        except Exception as e:
            print(f"Error al guardar notas: {e}")
            return False

    def cargar_notas(self):
        try:
            with open('notas.txt', 'r', encoding='utf-8') as archivo:
                self.notas = [linea.strip() for linea in archivo if linea.strip()]
        except FileNotFoundError:
            self.notas = []
        except Exception as e:
            print(f"Error al cargar notas: {e}")
            self.notas = []