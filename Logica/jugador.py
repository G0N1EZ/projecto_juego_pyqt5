from parametros import POSICION_INICIAL_X, POSICION_INICIAL_y, VELOCIDAD_JUGADOR

class Jugador:
    def __init__(self):
        self.pos_x = POSICION_INICIAL_X
        self.pos_y = POSICION_INICIAL_y
        self.velocidad = VELOCIDAD_JUGADOR


    def moverse(self, movimiento_x, movimiento_y):
        self.pos_x += movimiento_x
        self.pos_y += movimiento_y


