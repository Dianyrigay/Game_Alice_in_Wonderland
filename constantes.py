import pygame

WIDTH_PANTALLA = 1400
HEIGHT_PANTALLA = 800
ALTURA_PISO = 120
FPS = 60

TIEMPO_ENTRE_DISPAROS = 200

# Movimiento en x del enemigo
MARGEN_IZQUIERDO = 100
MARGEN_DERECHO = 600

# ------------------------Plataformas------------------------
AREA_1 = "./images/platforms/area.png"

# ------------------------Sonidos------------------------
pygame.mixer.init()
ambiente_fantasy = pygame.mixer.Sound('./sonidos/fantasy-ambient.wav')
items_win = pygame.mixer.Sound('./sonidos/items-win.wav')
pig_dead_sound = pygame.mixer.Sound('./sonidos/pig-dead.ogg')
game_over_sound = pygame.mixer.Sound('./sonidos/game_over.wav')
impact = pygame.mixer.Sound('./sonidos/impact.wav')
plant_dead_sound = pygame.mixer.Sound('./sonidos/plant-dead.wav')
