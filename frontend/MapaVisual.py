from PyQt5.QtWidgets import QGraphicsScene


class MapaVisual(QGraphicsScene):
    def __init__(self, datos_backend):
        super().__init__()
        self.backend = datos_backend
        self.objetos_en_pantalla = {}

    def generar_chunk(self):
        pass

    def borrar_chunk(self):
        pass

    def conversion_isometrica(self):
        pass


