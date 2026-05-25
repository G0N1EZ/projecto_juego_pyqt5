# Proceso Creativo de RPG en PyQt5

## Logs
- 23/12/2025: Inicialmente tengo la idea de hacer el RPG en python ocupando PyQt5, se que probablemente no es lo mejor ni es lo mas rapido, pero creo que puedo aprender más cosas valiosas haciendolo de esta manera. Ejemplo de esto es movimiento y colocacion manual de pixeles en pantalla. Estoy intentando aprender lo más posible haciendo este projecto por lo que tampoco estoy ocupando mucho herramientas IA. La idea es afirmar y profundizar mis conocimientos de progra avanzada. Respecto a el juego mismo todavia no decido nada, simplemente estoy probando conceptos fundamentales para ver que funciona, de esta manera comienzo intentado entender como puedo mover a un personaje en pantalla y generar coalisiones de objetos. tengo pensado hacer una ventana simple de prueba y un personaje con un sprite donde pueda colocar ciertos obstaculos y generar coalisiones.

-24/12/2025 1:27 am: me di cuenta que tenia mal la aproximacion, empece a ocupar entonces los metodos especializados de pyqt5 que se usan para configurar un espacio 2d. logre hacer un espacio negro y un sprite que se mueve con wasd. Lo proximo seria revisar coalisiones y mejorar la interaccion del sprite.

-18/1/2026 16:43 pm: empezamos a agregar a un enemigo en el juego y a hacer la logica de coalisiones, el enemigo por ahora es solo un obstaculo, una vez desarrollada la implementacion de la coalicion  entre dos cosas podemos lograr hacer un arma y pasarle un hitbox.

-15/03/2026 19:40 pm: He decidido reiniciar este projecto y empezar de nuevo a programar desde 0 un juego de mapa infinito procedimental y punto de vista 3d isometrico.
para esto vamos a ocupar principalmente a la hora de procesar objetos 2d a 3d las siguientes formulas del mapa:


## Tareas por hacer (lo mas cercano)
1. movimiento del jugador y sprite (actualmente)
2. objetos en mapa y orden.
3. coalisiones
4. 1 enemigo
5. Sistema de combate
6. ...

## Resumen de estructura frontend actual
1. **parametros.py (El Archivo de Configuración)**
Qué hace: Es la única fuente de la verdad para los "números mágicos" de tu juego (velocidades, rutas de archivos, tamaños).

Regla de oro para el futuro: Si vas a escribir un número o una ruta de archivo más de una vez en tu código, ponlo aquí. Si en el futuro quieres que el jugador camine más rápido, solo cambias VELOCIDAD_JUGADOR aquí y todo el juego se adapta sin tener que buscar en cientos de líneas de código.

2. **jugador.py (La Entidad / El Actor)**
Qué hace: Representa un objeto dinámico en el mundo. Hereda de QGraphicsPixmapItem para poder dibujarse.

Cómo funciona: * Guarda su propio estado: su posición matemática en el mundo (cor_x, cor_y), hacia dónde mira y qué fotograma de animación está reproduciendo.

Calcula su propia proyección: Tiene una función que traduce sus coordenadas de cuadrícula a la vista isométrica (diamante) para saber dónde dibujarse en la pantalla.

Regla de oro para el futuro: Cualquier cosa que el jugador haga o tenga (salud, inventario, atacar) debe programarse dentro de esta clase.

3. **VistaJugador.py (El Teclado y el Lente)**
Qué hace: Es la ventana física (QGraphicsView) por donde el jugador humano mira el mundo. También es el "teclado".

Cómo funciona: En lugar de procesar el movimiento, ahora solo registra la intención. Usamos un Set (conjunto) en Python para guardar qué teclas están presionadas actualmente y cuáles se soltaron.

Regla de oro para el futuro: Este archivo solo debe preocuparse por leer los controles del usuario (teclado, ratón) y aplicar zoom. No debe contener reglas del juego ni saber dónde está el jugador.

4. **MapaVisual.py (El Escenario)**
Qué hace: Es el lienzo (QGraphicsScene) donde se pintan los bloques de tierra, agua y ahora, el jugador.

Cómo funciona: Mantiene un registro de qué "chunks" (trozos de mapa) están generados y dibujados para no sobrecargar la memoria.

Regla de oro para el futuro: Si vas a añadir árboles, enemigos, edificios o cualquier cosa visual, se añaden a esta escena. Asegúrate de usar setZValue() correctamente (como hicimos con el jugador) para que los objetos que están "delante" tapen a los que están "detrás".

5. **VentanaJuego.py (El Controlador Principal / El Motor)**
Qué hace: Es el director de la orquesta. Conecta todo.

Cómo funciona (El Game Loop): Implementamos un QTimer que se ejecuta unas 60 veces por segundo (16ms). En cada "tic" del reloj, hace tres cosas en este orden exacto:

Lee el Input: Pregunta a VistaJugador qué teclas están presionadas.

Actualiza el Estado: Cambia la posición lógica del Jugador y actualiza la animación.

Renderiza: Le ordena a la VistaJugador que centre su lente (centerOn) en las nuevas coordenadas del jugador y revisa si es necesario generar más mapa procedimental en esa nueva ubicación.

Regla de oro para el futuro: Toda la lógica central (qué pasa si el jugador toca un objeto, si el jugador pasa de nivel) se orquesta aquí, leyendo información de las entidades y actualizando el mapa.