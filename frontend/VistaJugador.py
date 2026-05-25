from PyQt5.QtGui import QKeyEvent, QWheelEvent, QPainter
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import pyqtSignal, Qt
from frontend.parametros import NIVEL_ZOOM, FACTOR_ZOOM, VELOCIDAD_CAMARA


class VistaJugador(QGraphicsView):
    senal_mover_camara = pyqtSignal(float, float)

    def __init__(self, escena):
        super().__init__(escena)
        self.escena = escena
        self.zoom_camara = NIVEL_ZOOM
        self.setRenderHint(QPainter.Antialiasing)
        self.setBackgroundBrush(Qt.darkGray)

        # configuraciones de camara
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.teclas_presionadas = set()

    def wheelEvent(self, event: QWheelEvent | None) -> None:
        if event.angleDelta().y() > 0:
            self.scale(FACTOR_ZOOM, FACTOR_ZOOM)
        elif event.angleDelta().y() < 0:
            self.scale(1/FACTOR_ZOOM, 1/FACTOR_ZOOM)

    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        self.teclas_presionadas.add(event.key())

    def keyReleaseEvent(self, event: QKeyEvent | None) -> None:
        if event.key() in self.teclas_presionadas:
            self.teclas_presionadas.remove(event.key())



