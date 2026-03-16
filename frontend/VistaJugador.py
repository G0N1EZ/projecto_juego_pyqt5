from PyQt5.QtGui import QWheelEvent, QPainter
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtCore import Qt
from frontend.parametros import NIVEL_ZOOM, FACTOR_ZOOM

class VistaJugador(QGraphicsView):
    def __init__(self, escena):
        super().__init__()
        self.escena = escena
        self.zoom_camara = NIVEL_ZOOM
        self.setRenderHint(QPainter.Antialiasing)

        # configuraciones de camara
        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def wheelEvent(self, event: QWheelEvent | None) -> None:
        if event.angleDelta().y() > 0:
            self.scale(FACTOR_ZOOM, FACTOR_ZOOM)
        elif event.angleDelta().y() < 0:
            self.scale(1/FACTOR_ZOOM, 1/FACTOR_ZOOM)


