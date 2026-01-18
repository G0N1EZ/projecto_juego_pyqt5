from parametros import AREA_MAX_ENEMIGOS_X, AREA_MAX_ENEMIGOS_Y
import random

class Enemigo:
    def __init__(self):
        self.pos_x = random.randint(0, AREA_MAX_ENEMIGOS_X)
        self.pos_y = random.randint(0, AREA_MAX_ENEMIGOS_Y)
