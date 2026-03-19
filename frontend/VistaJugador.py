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

    def wheelEvent(self, event: QWheelEvent | None) -> None:
        if event.angleDelta().y() > 0:
            self.scale(FACTOR_ZOOM, FACTOR_ZOOM)
        elif event.angleDelta().y() < 0:
            self.scale(1/FACTOR_ZOOM, 1/FACTOR_ZOOM)

    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        velocidad_camara = VELOCIDAD_CAMARA
        if event.key() == Qt.Key_W:
            barra_v = self.verticalScrollBar()
            barra_v.setValue(barra_v.value() - velocidad_camara)

        elif event.key() == Qt.Key_S:
            barra_vs = self.verticalScrollBar()
            barra_vs.setValue(barra_vs.value() + velocidad_camara)

        elif event.key() == Qt.Key_A:
            barra_ha = self.horizontalScrollBar()
            barra_ha.setValue(barra_ha.value() - velocidad_camara)

        elif event.key() == Qt.Key_D:
            barra_hd = self.horizontalScrollBar()
            barra_hd.setValue(barra_hd.value() + velocidad_camara)

        else:
            return super().keyPressEvent(event)

        centro_pantalla = self.viewport().rect().center()
        punto_escena = self.mapToScene(centro_pantalla)
        self.senal_mover_camara.emit(punto_escena.x(), punto_escena.y())



