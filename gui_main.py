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

def play(level_play = "level_1"):
  player = Player()

  list_level = []

  level = Level(player, level_play)
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

    player.eventos(level.bubbles_group)
    if level_play == "level_2":
      player.transition_dark = True
    elif level_play == "level_3":
      player.dark = True

    if not game_over:
      if player.muerto or level.time_restante == 0:
        game_over = True

      level.draw(screen)
      level.update(screen)

      if level.next_level == "level_2":
        level_play = "level_2"
        level = Level(player, level_play)
        game_over = False
        list_level.append(level.level)
      elif level.next_level == "level_3":
        level_play = "level_3"
        level = Level(player, level_play)
        list_level.append(level.level)
    else:
      ambient_suspence.stop()
      game_over_sound.play()
      screen.blit(game_over_image, (0, 0))

    pygame.display.update()
    clock.tick(FPS)

def levels():
  while True:
    screen.fill("black")

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    LEVEL_1 = Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA/2, y=320,
                        text_input="LEVEL 1", base_color="white", hovering_color="yellow")
    LEVEL_2 = Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA/2, y=400,
                          text_input="LEVEL 2", base_color="white", hovering_color="yellow")
    LEVEL_3 = Button(image=pygame.image.load("./images/play-rect2.png"), x=WIDTH_PANTALLA/2, y=480,
                        text_input="LEVEL 3", base_color="white", hovering_color="yellow")

    for button in [LEVEL_1, LEVEL_2, LEVEL_3]:
      button.changeColor(MENU_MOUSE_POS)
      button.update(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            alice_intro.stop()
            click_magic.play()
            if LEVEL_1.checkForInput(MENU_MOUSE_POS):
              play("level_1")
            if LEVEL_2.checkForInput(MENU_MOUSE_POS):
              play("level_2")
            if LEVEL_3.checkForInput(MENU_MOUSE_POS):
              play("level_3")
            else:
              click_magic.stop()

    pygame.display.update()

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
            alice_intro.stop()
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
              play()
            if LEVELS_BUTTON.checkForInput(MENU_MOUSE_POS):
              levels()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
              pygame.quit()
              exit()
            else:
              click_magic.stop()

    pygame.display.update()

main_menu()