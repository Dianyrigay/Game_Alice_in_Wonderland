import pygame
from utilidades import *

pygame.init()
pygame.display.set_mode((WIDTH_PANTALLA,HEIGHT_PANTALLA))
# Alice
idle = [pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()]
idle_dark = [pygame.image.load('./images/alice/idle-dark2.png').convert_alpha()]

walk = [pygame.image.load('./images/alice/walk/rigth-00.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-01.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-02.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-03.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-04.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-05.png').convert_alpha()]

walk_dark = obtener_surface_de_spriteSheet('./images/alice/walk-dark.png', 7, 1, 1)

floating = [pygame.image.load('./images/alice/floating/floating-01.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-02.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-03.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-04.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-05.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-06.png').convert_alpha()]

floating_dark = obtener_surface_de_spriteSheet(
    './images/alice/floating-dark.png', 5, 1, 1)

dead = [pygame.image.load('./images/alice/dead/dead-01.gif').convert_alpha(),
        pygame.image.load('./images/alice/dead/dead-02.gif').convert_alpha(),
        pygame.image.load('./images/alice/dead/dead-03.gif').convert_alpha(),
        pygame.image.load('./images/alice/dead/dead-04.gif').convert_alpha(),
        pygame.image.load('./images/alice/dead/dead-05.gif').convert_alpha(),
        pygame.image.load('./images/alice/dead/dead-06.gif').convert_alpha()]

angry = obtener_surface_de_spriteSheet('./images/alice/angry/angry.png', 8, 1, 1)

reducir = [pygame.image.load('./images/alice/reduce/shrinking-01.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-02.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-03.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-04.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-05.png').convert_alpha()]

list_alice = [idle, walk, floating, angry]
reescalar_imagen(list_alice, 2.25)
list_alice_dark = [idle_dark, walk_dark, floating_dark]
reescalar_imagen(list_alice_dark, 2.25)

lista_dead = [dead]
reescalar_imagen(lista_dead, 2)

bubble = pygame.image.load('./images/alice/armas/burbuja.png').convert_alpha()
knife = pygame.image.load('./images/alice/armas/knife.png').convert_alpha()
explosion_burbuja = obtener_surface_de_spriteSheet('./images/explosiones/explosion1.png', 8, 1, 1)

live = obtener_surface_de_spriteSheet('./images/live.png', 1, 4, 1)
reescalar_imagen([live], 2)

transition_alice = obtener_surface_de_spriteSheet('./images/falling-alice.png', 16, 1, 1)

# ENEMIGOS

# plant
plant_idle = [pygame.image.load('./images/enemigos/plant/front-00.gif').convert_alpha(),
                pygame.image.load('./images/enemigos/plant/front-01.gif').convert_alpha(),
                pygame.image.load('./images/enemigos/plant/front-02.gif').convert_alpha()]

plant_dead = [pygame.image.load('./images/enemigos/plant/dead-00.gif').convert_alpha(),
        pygame.image.load('./images/enemigos/plant/dead-01.gif').convert_alpha(),
        pygame.image.load('./images/enemigos/plant/dead-02.gif').convert_alpha()]

plant_attack = obtener_surface_de_spriteSheet('./images/enemigos/plant/attack.png', 5, 1, 1)

lista_animaciones_plant = [plant_idle, plant_attack, plant_dead]
reescalar_imagen(lista_animaciones_plant, 1.5)

bala_plant = pygame.image.load('./images/enemigos/plant/bala_plant.gif').convert_alpha()

# pig
pig_fly = obtener_surface_de_spriteSheet('./images/enemigos/pig/pig_fly.png', 7, 1, 1)
pig_dead = obtener_surface_de_spriteSheet('./images/enemigos/pig/pig_dead.png', 7, 1, 1)

#bunny
bunny_idle = [pygame.image.load('./images/enemigos/bunny/idle/0.png').convert_alpha(),
              pygame.image.load('./images/enemigos/bunny/idle/1.png').convert_alpha(),
              pygame.image.load('./images/enemigos/bunny/idle/2.png').convert_alpha(),
              pygame.image.load('./images/enemigos/bunny/idle/3.png').convert_alpha(),]

lista_animaciones_bunny = [bunny_idle]
reescalar_imagen(lista_animaciones_bunny, 2)



# ITEMS
pocion_reduce = './images/items/pocion.png'
key_yellow = './images/items/key-yellow.png'
taza1 = './images/items/taza1.png'

# TRAMPAS

# mirror
mirror = [pygame.image.load('./images/trampas/mirror/0.png').convert_alpha(),
           pygame.image.load('./images/trampas/mirror/1.png').convert_alpha(),
           pygame.image.load('./images/trampas/mirror/2.png').convert_alpha(),
           pygame.image.load('./images/trampas/mirror/3.png').convert_alpha(),
           pygame.image.load('./images/trampas/mirror/4.png').convert_alpha()]

# Backgrounds
background_menu = pygame.transform.scale(pygame.image.load(
    "./images/background-menu.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
game_over_image = pygame.image.load("./images/game_over.png").convert_alpha()
game_over_image = pygame.transform.scale(
    game_over_image, (WIDTH_PANTALLA, HEIGHT_PANTALLA))


dict_animations = {
    "pig_fly": pig_fly,
    "pig_dead": pig_dead,
    "bunny_idle": bunny_idle,
    "plant_attack": plant_attack,
    "plant_idle": plant_idle,
}
