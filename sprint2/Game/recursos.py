import requests
from io import BytesIO
from PIL import Image


def descargar_imagen(url, retorno_llamada):
    """
        Descarga una imagen de internet y la pasa a otra función para procesarla

        Args:
            url (str): La dirección web donde se encuentra la imagen
            retorno_llamada (function): Función que recibe la imagen descargada para procesarla
        """
    try:
        # Obtenemos la imagen de internet y la preparamos
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        imagen = Image.open(BytesIO(respuesta.content))
        retorno_llamada(imagen)
    except requests.exceptions.RequestException as error:
        print(f"Error de descarga de la imagen: {error}")
        retorno_llamada(None)