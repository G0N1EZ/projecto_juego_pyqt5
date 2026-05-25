import math
from PyQt5.QtWidgets import QGraphicsPixmapItem
from frontend.parametros import RUTA_SPRITE_JUGADOR, TILE_X, TILE_Y
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QTransform



class Jugador(QGraphicsPixmapItem):
    '''
    Clase de jugador en el frontend con el sprite puesto encima
    que actualiza su posicion en la cuadrilla isometrica
    '''
    def __init__(self):
        super().__init__()
        self.cor_x = 0.0
        self.cor_y = 0.0

        # cargamos imagen del sprite y la dvidimos
        sprite_sheet = QPixmap(RUTA_SPRITE_JUGADOR)
        self.frames = []
        self.cantidad_frames = 6
        ancho_frame = sprite_sheet.width() // self.cantidad_frames
        alto_frame = sprite_sheet.height()

        for i in range(self.cantidad_frames):
            frame = sprite_sheet.copy(i*ancho_frame, 0, ancho_frame, alto_frame)
            self.frames.append(frame)
        self.frame_actual = 0
        self.setPixmap(self.frames[self.frame_actual])

        #centrar la imagen en el suelo simulado de la grilla
        self.setOffset(-ancho_frame / 2, -alto_frame)

        # animacion
        self.timer_animacion = QTimer()
        self.timer_animacion.timeout.connect(self.actualizar_frame)
        self.timer_animacion.start(100)

        self.en_movimiento = False
        self.mirando_izquierda = False
        self.actualizar_posicion_pantalla()

    def actualizar_frame(self):
        if self.en_movimiento:
            self.frame_actual = (self.frame_actual + 1) % self.cantidad_frames
        else:
            self.frame_actual = 0
        pixmap = self.frames[self.frame_actual]
        if self.mirando_izquierda:
            pixmap = pixmap.transformed(QTransform().scale(-1,1))
        self.setPixmap(pixmap)

    def actualizar_posicion_pantalla(self):
        #convertimos coordenadas logicas a isometricas
        #ocupamos el mismo offsetque usamos en la creacion de mapa con el 9
        iso_x = ((self.cor_x - self.cor_y) * (TILE_X / 2))
        iso_y = ((self.cor_x + self.cor_y) * ((TILE_Y - 9) / 2))
        self.setPos(iso_x, iso_y)
        #orden de dibujado: que se dibuje arriba del suelo
        self.setZValue(iso_y + 1)


