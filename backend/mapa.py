from backend.parametros import TILE_ANCHO, TILE_ALTO

class MapaProcedimental:
    def __init__(self):
        self.chunk = [
            [0, 0, 1, 1, 1],
            [0, 1, 1, 2, 1],
            [1, 1, 2, 2, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0]
        ]
        self.tile_x = TILE_ANCHO
        self.tile_y = TILE_ALTO

