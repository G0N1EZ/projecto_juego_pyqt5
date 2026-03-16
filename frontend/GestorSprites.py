from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect
from frontend.parametros import CORTADO_X, CORTADO_Y, MARGEN_ENTRE_IMAGEN, MARGEN_INICIO_X, MARGEN_INICIO_Y, RUTA_IMAGEN, SPRITES_POR_FILA

class GestorActivos:
    def __init__(self):
        self.spritesheet = QPixmap(RUTA_IMAGEN)

        # 1. Tus medidas exactas
        self.TILE_ANCHO = CORTADO_X
        self.TILE_ALTO = CORTADO_Y

        # 2. Los márgenes y espacios que descubriste
        margen_x_inicial = MARGEN_INICIO_X
        margen_y_inicial = MARGEN_INICIO_Y
        espacio_entre_tiles = MARGEN_ENTRE_IMAGEN

        # El "salto" total que da el cortador en cada ciclo
        salto_x = self.TILE_ANCHO + espacio_entre_tiles # 105 + 13 = 118

        self.terrenos = {}

        # 3. El bucle mágico para cortar la primera fila (tiene unas 12 baldosas)
        for i in range(12):
            # Calculamos la posición X para la baldosa actual (i)
            # Empezamos en 6, y le sumamos 118 por cada baldosa que avanzamos
            pos_x = margen_x_inicial + (i * salto_x)

            # La posición Y es siempre 11 para la primera fila
            pos_y = margen_y_inicial

            # Configuramos el cortador
            rect_cortador = QRect(pos_x, pos_y, self.TILE_ANCHO, self.TILE_ALTO)

            # ¡Zas! Cortamos y guardamos en el diccionario
            self.terrenos[i] = self.spritesheet.copy(rect_cortador)

    def obtener_terreno(self, ID):
        return self.terrenos.get(ID)