from backend.parametros import TAMANO_CHUNK
import random

class MapaProcedimental:
    def __init__(self):
        self.tamano_chunk = TAMANO_CHUNK
        self.chunk_generados = {}

    def generar_chunk(self, chunk_x, chunk_y):
        chunk = []
        if (chunk_x, chunk_y) in self.chunk_generados:
            return
        for _ in range(self.tamano_chunk):
            # Agregamos [0] al final de random.choices
            fila = [random.choices([0, 1], weights=[0.2, 0.8])[0] for tile in range(self.tamano_chunk)]
            chunk.append(fila)
        self.chunk_generados[(chunk_x, chunk_y)] = chunk

    def obtener_entorno(self, centro_x, centro_y):
        entorno_visible = {}
        for coordenada_x_chunks in range(centro_x - 1, centro_x + 2):
            for coordenada_y_chunks in range(centro_y - 1, centro_y + 2):
                self.generar_chunk(coordenada_x_chunks, coordenada_y_chunks)
                entorno_visible[(coordenada_x_chunks, coordenada_y_chunks)] = self.chunk_generados[(coordenada_x_chunks, coordenada_y_chunks)]
        return entorno_visible












