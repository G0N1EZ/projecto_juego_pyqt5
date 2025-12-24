import sys
from Renderizado.ventana_juego import VentanaJuego
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    def hook(type_, value, traceback):
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana_juego = VentanaJuego()
    ventana_juego.show()
    sys.exit(app.exec())