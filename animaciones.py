import pygame
from utilidades import *

pygame.init()
pygame.display.set_mode((WIDTH_PANTALLA,HEIGHT_PANTALLA))
# Alice
idle = [pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()]
idle_dark = [pygame.image.load('./images/alice/evil/idle.png').convert_alpha()]

walk = [pygame.image.load('./images/alice/walk/rigth-00.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-01.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-02.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-03.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-04.png').convert_alpha(),
              pygame.image.load('./images/alice/walk/rigth-05.png').convert_alpha()]

walk_dark = obtener_surface_de_spriteSheet('./images/alice/evil/walk.png', 7, 1, 1)

floating = [pygame.image.load('./images/alice/floating/floating-01.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-02.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-03.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-04.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-05.png').convert_alpha(),
            pygame.image.load('./images/alice/floating/floating-06.png').convert_alpha()]

floating_dark = obtener_surface_de_spriteSheet(
    './images/alice/evil/floating.png', 5, 1, 1)

# dead = [pygame.image.load('./images/alice/dead/dead-01.gif').convert_alpha(),
#         pygame.image.load('./images/alice/dead/dead-02.gif').convert_alpha(),
#         pygame.image.load('./images/alice/dead/dead-03.gif').convert_alpha(),
#         pygame.image.load('./images/alice/dead/dead-04.gif').convert_alpha(),
#         pygame.image.load('./images/alice/dead/dead-05.gif').convert_alpha(),
#         pygame.image.load('./images/alice/dead/dead-06.gif').convert_alpha()]

death = obtener_surface_de_spriteSheet(
    './images/alice/dead/death.png', 7, 1, 1)

angry = obtener_surface_de_spriteSheet('./images/alice/angry/angry.png', 8, 1, 1)
angry_dark = obtener_surface_de_spriteSheet(
    './images/alice/evil/angry.png', 8, 1, 1)


reducir = [pygame.image.load('./images/alice/reduce/shrinking-01.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-02.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-03.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-04.png').convert_alpha(),
           pygame.image.load('./images/alice/reduce/shrinking-05.png').convert_alpha()]

list_alice = [idle, walk, floating, angry, death]
list_alice_dark = [idle_dark, walk_dark, floating_dark, angry_dark, death]
lista_dead = [death]

reescalar_imagen(lista_dead, 2)
reescalar_imagen(list_alice, 2.25)
reescalar_imagen(list_alice_dark, 2.25)

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

# sombrero
sombrero_walk = [pygame.image.load('./images/enemigos/sombrero/walk/0.png.').convert_alpha(),
                 pygame.image.load('./images/enemigos/sombrero/walk/1.png.').convert_alpha(),
                 pygame.image.load('./images/enemigos/sombrero/walk/2.png.').convert_alpha(),
                 pygame.image.load('./images/enemigos/sombrero/walk/3.png.').convert_alpha()]

sombrero_attack = [pygame.image.load('./images/enemigos/sombrero/attack/0.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/attack/1.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/attack/2.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/attack/3.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/attack/4.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/attack/5.png.').convert_alpha()]

sombrero_hit = [pygame.image.load('./images/enemigos/sombrero/hit/0.png.').convert_alpha(),
                pygame.image.load(
                    './images/enemigos/sombrero/hit/1.png.').convert_alpha(),
                pygame.image.load(
                    './images/enemigos/sombrero/hit/2.png.').convert_alpha()]

sombrero_dead = [pygame.image.load(
    './images/enemigos/sombrero/death/0.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/death/1.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/death/2.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/death/3.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/death/4.png.').convert_alpha(),
pygame.image.load('./images/enemigos/sombrero/death/5.png.').convert_alpha()]

sombrero = [sombrero_walk, sombrero_hit, sombrero_attack]

#cuervo
cuervo_walk = obtener_surface_de_spriteSheet(
    './images/enemigos/cuervo/walk.png', 6, 1, 1)
cuervo_hit = obtener_surface_de_spriteSheet(
    './images/enemigos/cuervo/hit.png', 3, 1, 1)
cuervo_attack = obtener_surface_de_spriteSheet(
    './images/enemigos/cuervo/attack.png', 7, 1, 1)

cuervo = [cuervo_walk, cuervo_hit, cuervo_attack]

# dead
dead_idle = obtener_surface_de_spriteSheet(
    './images/enemigos/dead/idle.png', 3, 3, 1)
dead_hit = obtener_surface_de_spriteSheet(
    './images/enemigos/dead/death.png', 3, 3, 1)
dead_attack = obtener_surface_de_spriteSheet(
    './images/enemigos/dead/attack.png', 2, 3, 1)

dead = [dead_idle, dead_attack, dead_hit]

bala_dead = pygame.image.load('./images/enemigos/dead/bullet.png').convert_alpha()
reescalar_imagen(dead, 3.8)
reescalar_imagen(cuervo, 2)
reescalar_imagen(sombrero, 2.5)

# ITEMS
pocion_reduce = './images/items/pocion.png'
key_yellow = './images/items/key-yellow.png'
key_red = './images/items/key-red.png'
taza1 = './images/items/taza1.png'
live_item = './images/items/live.png'

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
game_over_image = pygame.image.load("./images/you_lose.png").convert_alpha()
game_over_image = pygame.transform.scale(
    game_over_image, (WIDTH_PANTALLA, HEIGHT_PANTALLA))
you_win = pygame.transform.scale(pygame.image.load(
"./images/you_win.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
background_pause = pygame.transform.scale(pygame.image.load("./images/menu_pause.png").convert_alpha(), (500,600))
high_scores_image = pygame.transform.scale(pygame.image.load(
    "./images/high_scores.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))

#PORTALES
portal_piedra = obtener_surface_de_spriteSheet(
    './images/portal/open.png', 2, 1, 1)
portal_blue = obtener_surface_de_spriteSheet(
    './images/portal/blue.png', 8, 1, 1)

dict_portales = {
    "portal_piedra": portal_piedra,
    "portal_blue": portal_blue
}
dict_animations = {
    "pig_fly": pig_fly,
    "pig_dead": pig_dead,
    "plant_attack": plant_attack,
    "plant_idle": plant_idle,
    "cuervo": cuervo,
    "sombrero": sombrero,
    "dead": dead
}
