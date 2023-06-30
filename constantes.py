import pygame

pygame.font.init()

WIDTH_PANTALLA = 1400
HEIGHT_PANTALLA = 800
ALTURA_PISO = 120
FPS = 60

TIEMPO_ENTRE_DISPAROS = 200

# Movimiento en x del enemigo
MARGEN_IZQUIERDO = 100
MARGEN_DERECHO = 600

# ------------------------Platforms------------------------
AREA_1 = "./images/platforms/area.png"

# ------------------------Sonidos------------------------
pygame.mixer.init()
# ambient sound
ambient_suspence = pygame.mixer.Sound('./sonidos/ambient-suspence.wav')
ambient_fantasy = pygame.mixer.Sound('./sonidos/ambient-fantasy.wav')
alice_intro = pygame.mixer.Sound('./sonidos/alice-intro.mp3')
game_over_sound = pygame.mixer.Sound('./sonidos/game_over.wav')

# items and object sound
items_win = pygame.mixer.Sound('./sonidos/items-win.wav')
pig_dead_sound = pygame.mixer.Sound('./sonidos/pig-dead.ogg')
impact = pygame.mixer.Sound('./sonidos/impact.wav')
plant_dead_sound = pygame.mixer.Sound('./sonidos/plant-dead.wav')
click_magic = pygame.mixer.Sound('./sonidos/magic.wav')
bubble = pygame.mixer.Sound('./sonidos/bubble.wav')

sonidos_caracters = [items_win, game_over_sound,
                     pig_dead_sound, impact, plant_dead_sound, ambient_fantasy, alice_intro, click_magic, bubble]
sonidos_005 = [ambient_suspence]

for sonido in sonidos_005:
  sonido.set_volume(0.05)

for sonido in sonidos_caracters:
  sonido.set_volume(0.15)

# ------------------------Fonts------------------------
font = pygame.font.Font("./assets/fonts/Redaction35-Bold.otf", 35)


