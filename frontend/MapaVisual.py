from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from backend.mapa import MapaProcedimental
from frontend.GestorSprites import GestorActivos
from frontend.parametros import TILE_X, TILE_Y, TAMANO_CHUNK

class MapaVisual(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.tile_x = TILE_X
        self.tile_y = TILE_Y
        self.tamano_chunk = TAMANO_CHUNK
        self.objetos_graficos = GestorActivos()
        self.chunks_dibujados = {}

    def generar_chunk(self, coordenada_x, coordenada_y, chunk):
        items_de_este_chunk = [] # Guardaremos los 25 rombos aquí
        offset_x = coordenada_x * self.tamano_chunk
        offset_y = coordenada_y * self.tamano_chunk
        for y_local, fila_x in enumerate(chunk):
            for x_local, tipo_terreno in enumerate(fila_x):
                cor_x = offset_x + x_local
                cor_y = offset_y + y_local
                iso_x = ((cor_x-cor_y)*(self.tile_x/2))
                iso_y = ((cor_x+cor_y)*((self.tile_y - 9)/2))
                pixmap = None
                if tipo_terreno == 0:
                    pixmap = self.objetos_graficos.obtener_terreno(0)
                elif tipo_terreno == 1:
                    pixmap = self.objetos_graficos.obtener_terreno(1)
                if pixmap:
                    item = QGraphicsPixmapItem(pixmap)
                    item.setOffset(-self.tile_x / 2, 0)
                    item.setPos(iso_x, iso_y)
                    item.setZValue(iso_y)

                    self.addItem(item)
                    items_de_este_chunk.append(item)
                    print(item)
            self.chunks_dibujados[(coordenada_x, coordenada_y)] = items_de_este_chunk

    def actualizar_chunks_visibles(self, diccionario_chunks: dict):
        borrar_chunks = []
        for coordenadas_chunk in self.chunks_dibujados.keys():
            if coordenadas_chunk not in diccionario_chunks:
                borrar_chunks.append(coordenadas_chunk)

        for coordenadas_chunk in borrar_chunks:
            for item in self.chunks_dibujados[coordenadas_chunk]:
                self.removeItem(item)
            del self.chunks_dibujados[coordenadas_chunk]

        # 2. DIBUJAR: Revisamos qué chunks nuevos NO están en la pantalla aún
        for coordenadas_chunk, chunk_bruto in diccionario_chunks.items():
            if coordenadas_chunk not in self.chunks_dibujados:
                self.generar_chunk(coordenadas_chunk[0], coordenadas_chunk[1], chunk_bruto)









