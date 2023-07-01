import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving
from gui_button import Button

from Level import Level

pygame.init()

# Configuración screen
screen = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()
pygame.display.set_icon(icono)

def play():
  ambient_suspence.play()

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
  enemy_list = [enemigo_plant, enemigo_pig]

  level_1 = Level(enemy_list, bullets_group, bubbles_group, items_group, traps_group, piso_rect, player, background_1, "./Levels/Level1.json")
  running_game = True
  game_over = False

  while running_game:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running_game = False
        exit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          player.saltar()

    player.eventos(bubbles_group)

    # Level 1
    if not game_over:
      if player.muerto or level_1.time_restante == 0:
        game_over = True

      level_1.draw(screen)
      level_1.update(screen)
    else:
      ambient_suspence.stop()
      game_over_sound.play()
      screen.blit(game_over_image, (0, 0))

    pygame.display.update()
    clock.tick(FPS)

def main_menu():
  alice_intro.play()
  while True:
    screen.blit(background_menu, (0,0))

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    PLAY_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x= 1030, y=320,
                      text_input="PLAY", base_color="white", hovering_color="yellow")
    QUIT_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x=1030, y=400,
                         text_input="QUIT", base_color="white", hovering_color="yellow")

    for button in [PLAY_BUTTON, QUIT_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
              click_magic.play()
              alice_intro.stop()
              play()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
              click_magic.play()
              pygame.quit()
              exit()
            else:
              click_magic.stop()
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.update()

main_menu()