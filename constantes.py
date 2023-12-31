import pygame

pygame.font.init()

WIDTH_PANTALLA = 1500
HEIGHT_PANTALLA = 800
ALTURA_PISO = 120
FPS = 60

TIEMPO_ENTRE_DISPAROS = 200

PISO_TOP = 680

# ------------------------Sonidos------------------------
pygame.mixer.init()
# ambient sound
ambient_suspence = pygame.mixer.Sound('./sonidos/ambient-suspence.wav')
ambient_fantasy = pygame.mixer.Sound('./sonidos/ambient-fantasy.wav')
ambient_horror = pygame.mixer.Sound('./sonidos/ambient-horror.wav')

alice_intro = pygame.mixer.Sound('./sonidos/intro.wav')
game_over_sound = pygame.mixer.Sound('./sonidos/game_over.wav')
game_win_sound = pygame.mixer.Sound('./sonidos/win.mp3')

# items and object sound
items_win = pygame.mixer.Sound('./sonidos/items-win.wav')
pig_dead_sound = pygame.mixer.Sound('./sonidos/pig-dead.ogg')
impact = pygame.mixer.Sound('./sonidos/impact.wav')
impact2 = pygame.mixer.Sound('./sonidos/impact2.wav')
plant_dead_sound = pygame.mixer.Sound('./sonidos/plant-dead.wav')
click_magic = pygame.mixer.Sound('./sonidos/magic.wav')
bubble_sound = pygame.mixer.Sound('./sonidos/bubble.wav')
portal_magic = pygame.mixer.Sound('./sonidos/portal-magic.wav')
suspence_invertion = pygame.mixer.Sound('./sonidos/suspence_invertion.wav')
knife_sound = pygame.mixer.Sound('./sonidos/knife.wav')
scream = pygame.mixer.Sound('./sonidos/scream.wav')

sonidos_caracters = [items_win, game_over_sound,
                     pig_dead_sound, impact, plant_dead_sound, ambient_fantasy, click_magic, bubble_sound, suspence_invertion, knife_sound, game_win_sound]
sonidos_005 = [ambient_suspence, portal_magic, ambient_horror, alice_intro]

for sonido in sonidos_005:
  sonido.set_volume(0.05)

for sonido in sonidos_caracters:
  sonido.set_volume(0.15)

# ------------------------Fonts------------------------
font = pygame.font.Font("./assets/fonts/Redaction35-Bold.otf", 35)


