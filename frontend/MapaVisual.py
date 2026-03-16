from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from frontend.GestorSprites import GestorActivos
from frontend.parametros import TILE_X, TILE_Y

class MapaVisual(QGraphicsScene):
    def __init__(self, datos_backend):
        super().__init__()
        self.tile_x = TILE_X
        self.tile_y = TILE_Y
        self.chunk = datos_backend
        self.objetos_graficos = GestorActivos()

        self.generar_chunk()

    def generar_chunk(self):
        print("llegamos")
        for cor_y, fila_x in enumerate(self.chunk):
            for cor_x, tipo_terreno in enumerate(fila_x):
                iso_x = (cor_x-cor_y)*(self.tile_x/2)
                iso_y = (cor_x+cor_y)*(self.tile_y/2)

                if tipo_terreno == 0:
                    pixmap = self.objetos_graficos.obtener_terreno(10)
                elif tipo_terreno == 1:
                    pixmap = self.objetos_graficos.obtener_terreno(0)

                print(pixmap)
                if pixmap:
                    item = QGraphicsPixmapItem(pixmap)
                    item.setOffset(-self.tile_x / 2, 0)
                    item.setPos(iso_x, iso_y)
                    item.setZValue(iso_y)

                    self.addItem(item)
                    print(item)



    def borrar_chunk(self):
        pass

    def conversion_isometrica(self):
        pass


