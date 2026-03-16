from PyQt5.QtWidgets import QMainWindow
from frontend.parametros import DIMENSION_X, DIMENSION_Y
from frontend.MapaVisual import MapaVisual
from frontend.VistaJugador import VistaJugador
from backend.mapa import MapaProcedimental


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Juego")
        self.resize(DIMENSION_X, DIMENSION_Y)
        self.mapa = MapaProcedimental().chunk

        self.escena = MapaVisual(self.mapa)
        self.vista = VistaJugador(self.escena)

        self.setCentralWidget(self.vista)





