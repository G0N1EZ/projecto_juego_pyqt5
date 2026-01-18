def colision(posicion_x, posicion_y, recorrido_x, recorrido_y, posicion_x_objeto, posicion_y_objeto, ancho_objeto1, alto_objeto1, ancho_objeto2, alto_objeto2):
    if (posicion_x + recorrido_x) < posicion_x_objeto and (posicion_x + recorrido_x < posicion_x_objeto + ancho_objeto2):
        pos_x = posicion_x + recorrido_x
    else:
        pos_x = posicion_x_objeto - ancho_objeto1
    if (posicion_y + recorrido_y) < posicion_y_objeto and (posicion_y + recorrido_y < posicion_y_objeto + alto_objeto2):
        pos_y = posicion_y + recorrido_y
    else:
        pos_y = posicion_y_objeto + alto_objeto2


