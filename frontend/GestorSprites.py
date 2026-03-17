from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt
from frontend.parametros import RUTA_IMAGEN, COORDENADA_IMAGEN_PASTO_X, COORDENADA_IMAGEN_PASTO_Y, ANCHO_TYLE_PASTO, ALTO_TYLE_PASTO, COORDENADA_IMAGEN_AGUA_X, COORDENADA_IMAGEN_AGUA_Y, ANCHO_TYLE_AGUA, ALTO_TYLE_AGUA

class GestorActivos:
    def __init__(self):
        '''
        cortamos manualmente los recursos que vamos a ocupar y los guardamos en un diccionario
        '''
        self.spritesheet = QPixmap(RUTA_IMAGEN)
        self.terrenos = {}

        # BUSCAMOS LAS TYLES QUE NECESITAMOS
        # PASTO
        self.cortar_imagen(COORDENADA_IMAGEN_PASTO_X, COORDENADA_IMAGEN_PASTO_Y, ANCHO_TYLE_PASTO, ALTO_TYLE_PASTO, 1)

        # AGUA
        self.cortar_imagen(COORDENADA_IMAGEN_AGUA_X, COORDENADA_IMAGEN_AGUA_Y, ANCHO_TYLE_AGUA, ALTO_TYLE_AGUA, 0)



    def obtener_terreno(self, ID):
        return self.terrenos.get(ID)

    def cortar_imagen(self, pos_x, pos_y, ancho_cortado, alto_cortado, tipo_terreno):
        '''
        esta funcion se encarga de cortar las imagenes o sprites que estan dentro de nuestra hoja de recursos
        '''
        rect_cortador = QRect(pos_x, pos_y, ancho_cortado, alto_cortado)
        pixmap_original = self.spritesheet.copy(rect_cortador)

            # 2. ESCALADO (La Magia)
        nuevo_ancho = 64
            # Calculamos el nuevo alto proporcionalmente (~43 pixeles)
        nuevo_alto = int(alto_cortado * (64 / ancho_cortado))

            # Aplicamos el suavizado (SmoothTransformation) para que no se vea pixelado
        pixmap_escalado = pixmap_original.scaled(
            nuevo_ancho,
            nuevo_alto,
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )

            # 3. Guardamos la versión encogida
        self.terrenos[tipo_terreno] = pixmap_escalado

