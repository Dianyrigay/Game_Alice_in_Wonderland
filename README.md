# Game_Alice_in_Wonderland


<!--
Archivo "main.py":

Importa los módulos necesarios de pygame y sys.
Importa las constantes y animationes desde archivos separados.
Importa las clases "Player", "Enemy_Shooter", "Enemy_Moving", "Platform" y "Portal" desde archivos separados.
Inicializa pygame y configura la screen del juego.
Establece variables para el tiempo, puntuación y sonidos del juego.
Carga las imágenes y sonidos necesarios para el juego.
Define una función para draw el fondo del juego.
Crea instancias de los objetos principales del juego, como el personaje principal, enemigos y plataformas.
Inicia un bucle principal del juego que maneja eventos, actualiza la lógica del juego y dibuja los elementos en la screen.

Archivo "Personaje.py":

Define la clase base "Personaje" que contiene métodos y atributos comunes para los personajes del juego.
El método "animar_personaje" muestra la animación actual del personaje en la screen.
El método "disparar" permite que el personaje dispare proyectiles.

Archivo "Player.py":

Importa las constantes y animationes desde archivos separados.
Importa la clase base "Personaje" desde el archivo "Personaje.py".
Define la clase "Player", que hereda de la clase base "Personaje".
Agrega atributos específicos del personaje principal, como speed, gravedad, vidas, etc.
Implementa métodos para controlar los movimientos y acciones del personaje principal, como saltar, moverse, disparar, etc.
Implementa el método "update" para actualizar la lógica del personaje principal en cada fotograma.

Otros archivos:

Archivo "constantes.py": Contiene constantes utilizadas en el juego, como dimensiones de screen, rutas de archivos, etc.
Archivo "animationes.py": Contiene listas de imágenes para animationes utilizadas en el juego.
Archivo "Enemigo.py": Define las clases de los enemigos del juego.
Archivo "Platform.py": Define la clase de las plataformas del juego.
Archivo "Item.py": Define la clase de los objetos de los juegos, como portales y pociones. -->