import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
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

  # Grupos de sprites
  bullets_group = pygame.sprite.Group()
  bubbles_group = pygame.sprite.Group()
  items_group = pygame.sprite.Group()
  traps_group = pygame.sprite.Group()

  # Instanciacion del personaje principal
  player = Player()

  list_level = []

  level = Level(bullets_group, bubbles_group, items_group, traps_group, player, "level_1", "./Levels/Level1.json")
  list_level.append(level.level)
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

    if not game_over:
      if player.muerto or level.time_restante == 0:
        game_over = True

      level.draw(screen)
      level.update(screen)

      if level.next_level == "Level2":
        level = Level(bullets_group, bubbles_group, items_group,
                        traps_group, player, "level_2", f"./Levels/{level.next_level}.json")
        game_over = False
        list_level.append(level.level)
      elif level.next_level == "Level3":
        level = Level(bullets_group, bubbles_group, items_group,
                      traps_group, player, "level_3", f"./Levels/{level.next_level}.json")
        list_level.append(level.level)
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

    PLAY_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x= 1060, y=320,
                      text_input="PLAY", base_color="white", hovering_color="yellow")
    LEVELS_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x=1060, y=400,
                         text_input="LEVELS", base_color="white", hovering_color="yellow")
    QUIT_BUTTON = Button(image=pygame.image.load("./images/play-rect2.png"), x=1060, y=480,
                         text_input="QUIT", base_color="white", hovering_color="yellow")

    for button in [PLAY_BUTTON, QUIT_BUTTON, LEVELS_BUTTON]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_magic.play()
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
              alice_intro.stop()
              play()
            if LEVELS_BUTTON.checkForInput(MENU_MOUSE_POS):
              pass
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
              pygame.quit()
              exit()
            else:
              click_magic.stop()
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.display.update()

main_menu()