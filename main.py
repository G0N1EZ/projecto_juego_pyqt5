import sys
from PyQt5.QtWidgets import QApplication
from frontend.VentanaJuego import VentanaJuego



if __name__ == "__main__":
    def hook(type_, value, traceback):
        """Hook para capturar excepciones no manejadas"""
        print(f"Error tipo: {type_}")
        print(f"Valor: {value}")
        print(f"Traceback: {traceback}")

    sys.__excepthook__ = hook

    # Crear instancia del backend (lógica del juego)


    # Crear aplicación Qt
    app = QApplication(sys.argv)

    # Crear ventana y pasar la referencia al juego
    ventana = VentanaJuego()
    ventana.show()

    # Iniciar loop de la aplicación
    sys.exit(app.exec_())