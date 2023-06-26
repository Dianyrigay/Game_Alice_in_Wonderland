import pygame

from utilidades import *

# Alice
quieto = [pygame.image.load('./images/alice/idle/rigth.png')]

camina = [pygame.image.load('./images/alice/walk/rigth-00.png'),
              pygame.image.load('./images/alice/walk/rigth-01.png'),
              pygame.image.load('./images/alice/walk/rigth-02.png'),
              pygame.image.load('./images/alice/walk/rigth-03.png'),
              pygame.image.load('./images/alice/walk/rigth-04.png'),
              pygame.image.load('./images/alice/walk/rigth-05.png')]

floating = [pygame.image.load('./images/alice/floating/floating-01.png'),
            pygame.image.load('./images/alice/floating/floating-02.png'),
            pygame.image.load('./images/alice/floating/floating-03.png'),
            pygame.image.load('./images/alice/floating/floating-04.png'),
            pygame.image.load('./images/alice/floating/floating-05.png'),
            pygame.image.load('./images/alice/floating/floating-06.png')]

dead = [pygame.image.load('./images/alice/dead/dead-01.gif'),
        pygame.image.load('./images/alice/dead/dead-02.gif'),
        pygame.image.load('./images/alice/dead/dead-03.gif'),
        pygame.image.load('./images/alice/dead/dead-04.gif'),
        pygame.image.load('./images/alice/dead/dead-05.gif'),
        pygame.image.load('./images/alice/dead/dead-06.gif')]

angry = getSurfaceFromSpriteSheet('./images/alice/angry/angry.png', 8, 1, 1)

lista_animaciones_alice = [quieto, camina, floating, angry]

reescalar_imagen(lista_animaciones_alice, 2.25)
lista_dead = [dead]
reescalar_imagen(lista_dead, 2)

burbuja_bala = pygame.image.load('./images/alice/disparo_magic/burbuja.png')
explosion_burbuja = getSurfaceFromSpriteSheet('./images/alice/disparo_magic/explosion-burbuja.png', 8, 1, 1)

# ENEMIGOS

# plant
quieto_front = [pygame.image.load('./images/enemigos/plant/front-00.gif'),
                pygame.image.load('./images/enemigos/plant/front-01.gif'),
                pygame.image.load('./images/enemigos/plant/front-02.gif')]

plant_dead = [pygame.image.load('./images/enemigos/plant/dead-00.gif'),
        pygame.image.load('./images/enemigos/plant/dead-01.gif'),
        pygame.image.load('./images/enemigos/plant/dead-02.gif')]

attack = getSurfaceFromSpriteSheet('./images/enemigos/plant/attack.png', 5, 1, 1)

lista_animaciones_plant = [quieto_front, attack, plant_dead]
reescalar_imagen(lista_animaciones_plant, 1.5)

bala_plant = pygame.image.load('./images/enemigos/plant/bala_plant.gif')

# pig
pig_fly = getSurfaceFromSpriteSheet('./images/enemigos/pig/pig_fly.png', 7, 1, 1)
pig_dead = getSurfaceFromSpriteSheet('./images/enemigos/pig/pig_dead.png', 7, 1, 1)

# ITEMS
hongo_yellow = './images/items/hongo-yellow.png'
hongo_violet = './images/items/hongo-violet.png'
pocion_reduce = './images/items/pocion.png'
key_yellow = './images/items/key-00.png'
taza1 = './images/items/taza1.png'

# PORTAL
open_portal = getSurfaceFromSpriteSheet('./images/portal/open.png', 10, 1, 1)
loop_portal = getSurfaceFromSpriteSheet('./images/portal/loop.png', 5, 1, 1)
