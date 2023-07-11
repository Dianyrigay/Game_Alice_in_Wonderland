<h1 align="center">Alice in Wonderland</h1>

<h4> Hola! Soy Dianyeli yrigay 👋</h4>
<h4> Estudiante de Programación en la UTN </h4>

<p>Alice in Wonderland es un juego de plataformas inspirado en el cuento de Alicia en el País de las Maravillas, donde nada es lo que parece. Los jugadores asumen el papel de Alice y viven con ella la transformación de su personaje, pasando de ser una niña tierna a una niña trastornada en busca de matar a los demonios que la perturban.

El objetivo principal del juego es ayudar a Alice a encontrar la llave que abrirá el portal para sumergirse a un nuevo mundo, tratando de escapar de sus pesadillas que cada vez son mas perturbadoras.</p>

# Niveles
### Nivel 1: El país de las maravillas
<p>Alice se adentra en el país de las maravillas donde deberás guiarla a buscar la llave que abrirá el portal de salida. Durante esta búsqueda deberás enfrentar a los enemigos y ten cuidado con las trampas! Podrían distorsionar la realidad...</p>
<p align="center">
 <img height=300px src="./images/readme/level_1.gif" alt="banner" />
</p>

### Nivel 2: La hora del Té
<p>Un nuevo desafío espera a Alice y parece que su tamaño no le favorece, deberás ayudarla a escapar de un nuevo enemigo... el sombrerero (¡parece que ha perdido la cabeza!). Y no llegues a mitad del camino, en Alice se despierta una nueva personalidad...</p>
<p align="center">
 <img height=300px src="./images/readme/level_2.gif" alt="banner" />
</p>

### Nivel 3: El bosque maldito
<p>En este nivel deberás acompañar a Alice a enfrentar a sus peores pesadillas, los demonios que perturbaron su país de las maravillas...</p>
<p align="center">
 <img height=300px src="./images/readme/level_3.gif" alt="banner" />
</p>

# Controles
Para controlar a Alice, podremos utilizar las siguientes teclas:

`TECLA →:` Movimiento hacia la derecha.

`TECLA ←:` Movimiento hacia la izquierda.

`TECLA BARRA ESPACIADORA:` Salto (doble barra / doble salto).

`TECLA X:` Disparar.

# Enemigos

### - Flypig:
![flypig](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/7607979c-ae59-406b-96fc-3d319bb5f890)

Estos cerditos voladores no son lo que parece, cuidado con tocarlos que pueden restarte una vida.

### - Flor Mortal:
![plantaMortal](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/e9c1fb3f-8b84-43b4-b94e-8b4f0e62f68c)

Que no te engañen! disparan constantemente, deberás esquivar sus proyectiles.

### - EL Sombrerero:
![sombrerero](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/ec9ebc10-d84c-4af1-930d-4698aaad74e1)

Ha perdido la cabeza y si detecta tus movimientos cerca buscará clavarte los dientes.

### - Cuervo de la Muerte:
![cuervoDead](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/97cf7a9b-38af-43ee-9f64-037b0f19bd4a)

Este cuervo es el guardían de nuestro enemigo final, vigila la zona y si detecta movimientos cerca buscará matarte.

### - El demonio de la Muerte:
![dead](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/23f30e53-ae41-4704-92f6-96df2def61cd)

El Jefe Final. La peor pesadilla de Alice, te perseguirá y buscará matarte, apuntale bien, intentará esquivar tus cuchillazos.

# Consumibles
### - Objetos:
![hongo-yellow](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/ecdae036-8949-499c-b29b-b047b88f01a2) ![queen](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/e2bf5ad9-3281-4fa6-a6c9-fd07df41c47a) ![sombrero](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/9110cb53-b4c8-4d12-8bea-1f260d6a5c5c) ![taza1](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/f917a687-4a64-468a-8d48-2704702cd25e)

Podrás escontrar objetos a lo largo de los niveles que te ayudarán a subir puntos.

### - Vidas:
![live](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/dd208bb3-bb04-49f2-b30f-2e2f4ed14cb3)

Aumentarán tus vidas! menor probabilidad a que te maten.

### - Poción de Encogimiento / Tarta Mágica:
![pocion](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/3468e4e2-7e76-4914-9271-8421247b2155) ![tarta](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/f06e7347-56de-41e7-839a-17d8fb26586e)

Ayudarán a que Alice se adapte al tamaño que necesite para continuar los niveles.

### - Keys:
![key-red](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/17e59fbd-cbec-4104-bda6-c41a8e14709d) ![key-yellow](https://github.com/Dianyrigay/yrigayDianyeli-pygame-tp-final/assets/80293439/960fe2f4-940a-47ae-a1e5-1626391a7089)



Ayudarán a descubrir el portal y poder avanzar al siguiente nivel.

# Cómo perder

- Perdiendo todas las vidas (se van restando al colisionar con un enemigo o al recibir algún disparo)
- Si te quedas sin tiempo en el nivel, cada uno tiene un tiempo de 60 segundos.

Si Alice pierde todas sus vidas o se queda sin tiempo, el juego terminará y se mostrará el menú de juego perdido.

#
<h3 align="center">Alice in Wonderland ha sido desarrollado con Pygame como entrega final para la asignatura Programación 1 de la Universidad Tecnológica Nacional (UTN)</h3>





