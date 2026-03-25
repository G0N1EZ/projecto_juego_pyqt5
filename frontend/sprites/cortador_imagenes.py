import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image

class CortadorSprites(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cortador Automático de Spritesheets')
        self.resize(600, 400)

        main_layout = QVBoxLayout()
        images_layout = QHBoxLayout()

        self.btn_cargar = QPushButton('Cargar Spritesheet y Recortar Todo', self)
        self.btn_cargar.clicked.connect(self.procesar_imagen)
        main_layout.addWidget(self.btn_cargar)

        self.lbl_original = QLabel('Imagen Original', self)
        self.lbl_recortada = QLabel('Ejemplo del Primer Sprite', self)

        images_layout.addWidget(self.lbl_original)
        images_layout.addWidget(self.lbl_recortada)
        main_layout.addLayout(images_layout)

        self.setLayout(main_layout)

    def procesar_imagen(self):
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Hoja de Sprites", "",
                                                 "Images (*.png *.xpm *.jpg *.bmp);;All Files (*)",
                                                 options=opciones)
        if not archivo:
            return

        # Mostrar original
        pixmap_original = QPixmap(archivo)
        self.lbl_original.setPixmap(pixmap_original.scaled(300, 300))

        try:
            img = Image.open(archivo)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')

            ancho, alto = img.size
            pixeles = img.load()

            sprites_encontrados = []
            en_sprite = False
            inicio_x = 0

            # 1. Escanear columna por columna (de izquierda a derecha)
            for x in range(ancho):
                columna_tiene_pixeles = False
                for y in range(alto):
                    # Revisar si el pixel NO es totalmente transparente (Canal Alfa > 0)
                    if pixeles[x, y][3] > 0:
                        columna_tiene_pixeles = True
                        break

                # Lógica para detectar dónde empieza y termina cada personaje
                if columna_tiene_pixeles and not en_sprite:
                    en_sprite = True
                    inicio_x = x # Aquí empieza un personaje
                elif not columna_tiene_pixeles and en_sprite:
                    en_sprite = False
                    fin_x = x    # Aquí termina el personaje (hay un espacio vacío)
                    sprites_encontrados.append((inicio_x, fin_x))

            # Por si el último sprite toca el borde derecho de la imagen
            if en_sprite:
                sprites_encontrados.append((inicio_x, ancho))

            # 2. Recortar y guardar cada sprite encontrado
            base_nombre, extension = os.path.splitext(archivo)
            rutas_guardadas = []

            for indice, (start_x, end_x) in enumerate(sprites_encontrados):
                # Cortar la tira vertical del personaje
                tira_vertical = img.crop((start_x, 0, end_x, alto))

                # Ajustar los bordes de arriba y abajo usando getbbox()
                caja_perfecta = tira_vertical.getbbox()
                if caja_perfecta:
                    sprite_final = tira_vertical.crop(caja_perfecta)

                    # Guardar con número: nombre_0.png, nombre_1.png, etc.
                    ruta_guardado = f"{base_nombre}_{indice}{extension}"
                    sprite_final.save(ruta_guardado)
                    rutas_guardadas.append(ruta_guardado)

            # 3. Actualizar la interfaz y avisar
            if rutas_guardadas:
                # Mostrar solo el primero en la ventana como comprobación
                pixmap_recortado = QPixmap(rutas_guardadas[0])
                self.lbl_recortada.setPixmap(pixmap_recortado.scaled(150, 150))

                QMessageBox.information(self, "¡Éxito!", f"Se encontraron y guardaron {len(rutas_guardadas)} sprites individuales en la misma carpeta.")
            else:
                QMessageBox.warning(self, "Aviso", "No se detectaron sprites (la imagen parece estar vacía).")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CortadorSprites()
    ventana.show()
    sys.exit(app.exec_())