import math
from PyQt5.QtWidgets import QMainWindow
from frontend.parametros import DIMENSION_X, DIMENSION_Y, TILE_X, TILE_Y, TAMANO_CHUNK
from frontend.MapaVisual import MapaVisual
from frontend.VistaJugador import VistaJugador
from backend.mapa import MapaProcedimental


class VentanaJuego(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Juego")
        self.resize(DIMENSION_X, DIMENSION_Y)
        self.mapa = MapaProcedimental()
        self.escena = MapaVisual()
        self.vista = VistaJugador(self.escena)

        self.setCentralWidget(self.vista)

        self.vista.senal_mover_camara.connect(self.actualizar_mundo)
        self.chunk_actual = (0,0)
        entorno_inicial = self.mapa.obtener_entorno(0, 0)
        self.escena.actualizar_chunks_visibles(entorno_inicial)


    def actualizar_mundo(self, escena_x, escena_y):
        '''convertimos la posicion de la pantalla en coordenadas chunk'''
        mitad_w = TILE_X / 2
        mitad_h = (TILE_Y - 9) / 2

        cor_x = (escena_x / mitad_w + escena_y / mitad_h) / 2
        cor_y = (escena_y / mitad_h - escena_x / mitad_w) / 2

        chunk_x = math.floor(cor_x / TAMANO_CHUNK)
        chunk_y = math.floor(cor_y / TAMANO_CHUNK)

        # Si cambiamos de chunk, actualizamos el mapa
        if (chunk_x, chunk_y) != self.chunk_actual:
            print(f"¡Nuevo Chunk! Generando entorno para: {chunk_x}, {chunk_y}")
            self.chunk_actual = (chunk_x, chunk_y)

            nuevo_entorno = self.mapa.obtener_entorno(chunk_x, chunk_y)
            self.escena.actualizar_chunks_visibles(nuevo_entorno)










