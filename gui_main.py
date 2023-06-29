import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving
from Platform import Platform
from collitions import Collition
from Item import Portal
from gui_button import Button

pygame.init()

# Configuración screen
screen = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()
pygame.display.set_icon(icono)

background_menu = pygame.transform.scale(pygame.image.load(
    "./images/background-alice.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))

# TODO CAMBIAR FONT
font = pygame.font.Font("./assets/fonts/Redaction35-Bold.otf", 40)

def play(): #Play screen
  # Cronómetro del juego
  tiempo_total = 60000  # Duración total del cronómetro en milisegundos
  tiempo_actual = pygame.time.get_ticks()  # Tiempo transcurrido inicialmente

  # Sistema de score
  score = 100

  # Sonidos
  sonidos_caracters = [items_win, game_over_sound,
                       pig_dead_sound, impact, plant_dead_sound]
  sonidos_005 = [ambiente_fantasy]

  for sonido in sonidos_005:
    sonido.set_volume(0.05)

  for sonido in sonidos_caracters:
    sonido.set_volume(0.15)

  ambiente_fantasy.play()

  background_1 = pygame.transform.scale(pygame.image.load(
      "./images/fondo/area.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))

  # Superficie piso
  piso_surf = pygame.Surface((WIDTH_PANTALLA, ALTURA_PISO))
  piso_rect = piso_surf.get_rect(
      topleft=(0, HEIGHT_PANTALLA - piso_surf.get_height()))

  # Grupos de sprites
  bullets_group = pygame.sprite.Group()
  bubbles_group = pygame.sprite.Group()
  items_group = pygame.sprite.Group()
  traps_group = pygame.sprite.Group()

  # Instanciacion del personaje principal
  player = Player()
  # Instanciacion de enemigos
  enemigo_plant = Enemy_Shooter(
      (WIDTH_PANTALLA - 200, HEIGHT_PANTALLA - ALTURA_PISO), attack)
  enemigo_pig = Enemy_Moving((WIDTH_PANTALLA/2, 250), pig_fly)
  # Instanciacion de plataformas
  plataforma1 = Platform(AREA_1, 3, 0, 300, 500, items_group, hongo_yellow)
  plataforma2 = Platform(AREA_1, 2, 0, 550, 450, items_group, hongo_violet)
  plataforma3 = Platform(AREA_1, 5, 0, 700, 280, items_group, hongo_yellow)
  plataforma4 = Platform(AREA_1, 3, 0, 270, 250, items_group, key_yellow)
  plataforma5 = Platform(AREA_1, 1, 0, 1200, 500, items_group, pocion_reduce)
  plataforma6 = Platform(AREA_1, 1, 0, 100, 200, traps_group, mirror)

  lista_rectangulos = [piso_rect, plataforma1.rect, plataforma2.rect,
                       plataforma3.rect, plataforma4.rect, plataforma5.rect, plataforma6.rect]
  platforms_list = [plataforma1, plataforma2,
                    plataforma3, plataforma4, plataforma5, plataforma6]
  enemy_list = [enemigo_plant, enemigo_pig]

  # Instanciacion de colisiones
  colisiones = Collition(player, enemy_list, platforms_list,
                         bullets_group, bubbles_group, items_group, sonidos_caracters)

  running_game = True
  game_over = False
  game_over_image = pygame.image.load("./images/game_over.png").convert_alpha()
  game_over_image = pygame.transform.scale(
      game_over_image, (WIDTH_PANTALLA, HEIGHT_PANTALLA))

  while running_game:
    screen.fill("black")

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running_game = False
        exit()


    tiempo_transcurrido = pygame.time.get_ticks() - tiempo_actual
    tiempo_restante = max(0, tiempo_total - tiempo_transcurrido) // 1000

    keys = pygame.key.get_pressed()
    player.eventos(keys, bubbles_group)

    # Background
    screen.blit(background_1, (0, 0))

     # Level 1
    if not game_over:
      if player.muerto or tiempo_restante == 0:
        game_over = True

        # -- Colisiones
      colisiones.update(screen)

          # -- Player
      player.update(screen, lista_rectangulos)
      if player.key_recogida:
        # TODO agregar sonido cuando abre portal
        portal = Portal(WIDTH_PANTALLA - 100, HEIGHT_PANTALLA - ALTURA_PISO, open_portal)
        portal.update(screen)

          # --Platforms
      for plataforma in platforms_list:
        plataforma.dibujar(screen)

      # --Actualización y dibujos de Groups
      # balas
      bullets_group.update()
      bullets_group.draw(screen)
      # burbuja
      bubbles_group.update()
      bubbles_group.draw(screen)
      # items
      items_group.update()
      items_group.draw(screen)

      # -- Enemigos
      enemigo_plant.update(screen, piso_rect, bullets_group)
      enemigo_pig.update(screen)

      escribir_screen(screen, 'SCORE: ', "white", str(score), (20, 20))
      escribir_screen(screen, 'VIDAS: ', "white",str(player.vidas), (1250, 20))
      escribir_screen(screen, '00:', "white", str(tiempo_restante).zfill(2), (WIDTH_PANTALLA/2, 20))
    else:
      ambiente_fantasy.stop()
      game_over_sound.play()
      screen.blit(game_over_image, (0, 0))

    pygame.display.update()
    clock.tick(FPS)

def main_menu():
  while True:
    screen.blit(background_menu, (0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    PLAY_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x= 1030, y=320,
                      text_input="PLAY", base_color="white", hovering_color="Yellow")

    for button in [PLAY_BUTTON]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
              play()

    pygame.display.update()

main_menu()