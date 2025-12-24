from PyQt5.QtWidgets import QGraphicsView, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
from Logica.jugador import Jugador
from parametros import DIRECCION_SPRITE, ANCHO_VENTANA, ALTO_VENTANA, ANCHO_JUGADOR, ALTO_JUGADOR

class ImagenJugador(QGraphicsPixmapItem):
    def __init__(self, pixmap: QPixmap):
        super().__init__(pixmap)

    def sinc_movimiento(self, jugador: Jugador):
        self.setPos(jugador.pos_x, jugador.pos_y)



class VentanaJuego(QGraphicsView):
    def __init__(self):
        super().__init__()

        # escena
        self.escena = QGraphicsScene()
        self.escena.setBackgroundBrush(Qt.black)
        self.setScene(self.escena)

        # jugador
        self.jugador = Jugador()
        pixmap = QPixmap(DIRECCION_SPRITE)
        pixmap = pixmap.scaled(
            ANCHO_JUGADOR, ALTO_JUGADOR,
            Qt.KeepAspectRatio,
            Qt.FastTransformation
        )
        self.imagen_jugador = ImagenJugador(pixmap)
        pixmap = QPixmap(DIRECCION_SPRITE)
        print(pixmap.isNull())
        self.escena.addItem(self.imagen_jugador)
        self.imagen_jugador.sinc_movimiento(self.jugador)

        # loop juego
        self.acciones = set()
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_juego)
        self.timer.start(16)

        #modo ventana
        self.setFixedSize(ANCHO_VENTANA, ALTO_VENTANA)
        self.setSceneRect(0, 0, ANCHO_VENTANA, ALTO_VENTANA)
        self.setFocusPolicy(Qt.StrongFocus)

    def keyPressEvent(self, event):
        self.acciones.add(event.key())

    def keyReleaseEvent(self, event):
        self.acciones.discard(event.key())

    def actualizar_juego(self):
        recorrido_x = 0
        recorrido_y = 0

        if Qt.Key_W in self.acciones:
            recorrido_y -= 1
        if Qt.Key_S in self.acciones:
            recorrido_y += 1
        if Qt.Key_A in self.acciones:
            recorrido_x -= 1
        if Qt.Key_D in self.acciones:
            recorrido_x += 1

        self.jugador.moverse(recorrido_x, recorrido_y)
        self.imagen_jugador.sinc_movimiento(self.jugador)






