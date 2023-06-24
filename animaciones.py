import pygame
from utilidades import *

# Alice
quieto_der = [pygame.image.load('./images/alice/idle/rigth.png')]

camina_der = [pygame.image.load('./images/alice/walk/rigth-00.png'),
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

lista_animaciones_alice = [quieto_der, camina_der, floating]
reescalar_imagen(lista_animaciones_alice, 2.25)
lista_dead = [dead]
reescalar_imagen(lista_dead, 2)

# ENEMIGOS

# plant
quieto_front = [pygame.image.load('./images/enemigos/plant/front-00.gif'),
                pygame.image.load('./images/enemigos/plant/front-01.gif'),
                pygame.image.load('./images/enemigos/plant/front-02.gif')]

attack_izq = [pygame.image.load('./images/enemigos/plant/attack-00.gif'),
              pygame.image.load('./images/enemigos/plant/attack-01.gif'),
              pygame.image.load('./images/enemigos/plant/attack-02.gif'),
              pygame.image.load('./images/enemigos/plant/attack-03.gif'),
              pygame.image.load('./images/enemigos/plant/attack-04.gif')]

enemy_dead = [pygame.image.load('./images/enemigos/plant/dead-00.gif'),
        pygame.image.load('./images/enemigos/plant/dead-01.gif'),
        pygame.image.load('./images/enemigos/plant/dead-02.gif')]

lista_animaciones_plant = [quieto_front, attack_izq, enemy_dead]
reescalar_imagen(lista_animaciones_plant, 1.5)

# pig
pig_fly = getSurfaceFromSpriteSheet('./images/enemigos/pig/pig_fly.png', 7, 1, 1)
pig_dead = getSurfaceFromSpriteSheet('./images/enemigos/pig/pig_dead.png', 7, 1, 1)