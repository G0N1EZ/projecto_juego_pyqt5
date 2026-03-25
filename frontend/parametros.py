import os

# parametros ventana grafica
DIMENSION_X = 800
DIMENSION_Y = 600


# parametros mapa visual
TILE_X = 105  # El ancho exacto al que escalas en GestorSprites
TILE_Y = 71  # La mitad perfecta para isometría
TAMANO_CHUNK = 8



# parametros camara
NIVEL_ZOOM = 1.0
FACTOR_ZOOM = 1.15
VELOCIDAD_CAMARA = 8 # fRAMES

# parametros de cortado de imagen
RUTA_IMAGEN = os.path.join("frontend", "sprites", "sprites_basicos.png")

COORDENADA_IMAGEN_PASTO_X = 6
COORDENADA_IMAGEN_PASTO_Y = 11
ANCHO_TYLE_PASTO = 105
ALTO_TYLE_PASTO = 71

COORDENADA_IMAGEN_AGUA_X = 1061
COORDENADA_IMAGEN_AGUA_Y = 11
ANCHO_TYLE_AGUA = 105
ALTO_TYLE_AGUA = 71

# JUGADOR
PATH_SPRITE_JUGADOR = os.path.join("frontend", "sprites", "jugador.png")

