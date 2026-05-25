import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer, Qt
from frontend.parametros import DIMENSION_X, DIMENSION_Y, TILE_X, TILE_Y, TAMANO_CHUNK, VELOCIDAD_JUGADOR
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

        self.chunk_actual = (0,0)
        entorno_inicial = self.mapa.obtener_entorno(0, 0)
        self.escena.actualizar_chunks_visibles(entorno_inicial)

        # centrAR vista en el jugador al iniciar
        self.vista.centerOn(self.escena.jugador)

        #gameloop
        self.timer_juego = QTimer()
        self.timer_juego.timeout.connect(self.loop_movimiento)
        self.timer_juego.start(16)

    def loop_movimiento(self):
        dx = 0
        dy = 0

        #mapeo de teclas cartesianas a isometricas
        if Qt.Key_W in self.vista.teclas_presionadas:
            dx -= VELOCIDAD_JUGADOR; dy -= VELOCIDAD_JUGADOR
        if Qt.Key_S in self.vista.teclas_presionadas:
            dx += VELOCIDAD_JUGADOR; dy += VELOCIDAD_JUGADOR
        if Qt.Key_A in self.vista.teclas_presionadas:
            dx -= VELOCIDAD_JUGADOR; dy += VELOCIDAD_JUGADOR
            self.escena.jugador.mirando_izquierda = True
        if Qt.Key_D in self.vista.teclas_presionadas:
            dx += VELOCIDAD_JUGADOR; dy -= VELOCIDAD_JUGADOR
            self.escena.jugador.mirando_izquierda = False

        if dx != 0 or dy != 0:
            #mover personaje
            self.escena.jugador.cor_x += dx
            self.escena.jugador.cor_y += dy
            self.escena.jugador.en_movimiento = True
            self.escena.jugador.actualizar_posicion_pantalla()

            self.vista.centerOn(self.escena.jugador)

            self.actualizar_mundo_por_posicion()

        else:
            self.escena.jugador.en_movimiento = False

    def actualizar_mundo_por_posicion(self):
        #convertimos la posicion logica del jugador a coordenadas de chunk
        chunk_x = math.floor(self.escena.jugador.cor_x / TAMANO_CHUNK)
        chunk_y = math.floor(self.escena.jugador.cor_y / TAMANO_CHUNK)

        if (chunk_x, chunk_y) != self.chunk_actual:
            print(f"¡Nuevo Chunk! Generando entorno para: {chunk_x}, {chunk_y}")
            self.chunk_actual = (chunk_x, chunk_y)
            nuevo_entorno = self.mapa.obtener_entorno(chunk_x, chunk_y)
            self.escena.actualizar_chunks_visibles(nuevo_entorno)










