import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
from Level import Level
from menu import MainMenu, LevelsMenu, PauseMenu, FinalMenu, High_Scores

pygame.init()

# Configuración screen
screen = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png').convert_alpha()
pygame.display.set_icon(icono)

global list_level
list_level = []

def play(level_play="level_1"):
  player = Player()

  level = Level(player, level_play)
  list_level.append(level.level)
  running_game = True
  game_over = False
  game_win = False
  is_paused = False
  return_to_play = False

  while running_game:
        if is_paused:
            pygame.display.update()
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.saltar()
                if event.key == pygame.K_ESCAPE:
                    is_paused = True
                    return_to_play = pause_menu(level_play)

        player.eventos(level.bubbles_group)
        if level_play == "level_2":
          player.transition_dark = True
        elif level_play == "level_3":
          player.dark = True

        if not game_over and not game_win:
            if player.muerto or level.time_restante == 0:
                game_over = True

            if level.game_win:
               game_win = True

            level.draw(screen)
            level.update(screen)

            if level.next_level == "level_2":
              level_play = "level_2"
              level = Level(player, level_play)
              if level not in list_level:
                list_level.append(level.level)
            elif level.next_level == "level_3":
              level_play = "level_3"
              level = Level(player, level_play)
              if level not in list_level:
                list_level.append(level.level)

        else:
            win_lose_menu(level_play, game_over, game_win, player.score, level_play)

        pygame.display.update()
        clock.tick(FPS)

        if return_to_play:
            is_paused = False
            return_to_play = False

def main_menu():
    alice_intro.play()

    while True:
      main_menu = MainMenu()
      ejecutar =  main_menu.update()
      main_menu.draw(screen)
      if ejecutar == "play":
        alice_intro.stop()
        play()
      elif ejecutar == "levels_menu":
        levels_menu()
      elif ejecutar == "records":
        high_scores_menu()
      pygame.display.update()

def levels_menu():
    alice_intro.stop()
    click_magic.play()
    while True:
      levels_menu = LevelsMenu()
      for i in range(len(list_level)):
        levels_menu.level_status[i] = True
      ejecutar = levels_menu.update()
      levels_menu.draw(screen)
      if ejecutar == "play_1" and levels_menu.level_status[0]:
          play("level_1")
      elif ejecutar == "play_2" and levels_menu.level_status[1]:
          play("level_2")
      elif ejecutar == "play_3" and levels_menu.level_status[2]:
          play("level_3")
      elif ejecutar == "main_menu":
        main_menu()
      pygame.display.update()

def pause_menu(level_play):
  alice_intro.stop()
  click_magic.play()

  while True:
    pause_menu = PauseMenu()
    ejecutar = pause_menu.update()
    pause_menu.draw(screen)
    if ejecutar == "continue":
      return True
    elif ejecutar == "restart":
      play(level_play)
    elif ejecutar == "main_menu":
      main_menu()
    pygame.display.update()


def win_lose_menu(level_play, game_over, game_win, score, level):
  if game_over:
    game_over_sound.play()
  if game_win:
    #TODO agrega musica de win
    pass

  final_menu = FinalMenu(game_over, game_win, score, level)

  while True:
    ejecutar = final_menu.update()
    final_menu.draw(screen)
    if game_over:
      if ejecutar == "retry":
        play(level_play)
      elif ejecutar == "main_menu":
        main_menu()
    elif game_win:
      escribir_screen(screen, 'NAME:', "white","", (845, 280))
      escribir_screen(screen, 'SCORE: ', "white",
                    str(score), (845, 350))
      if ejecutar == "guardar":
         high_scores_menu()
    pygame.display.update()

def high_scores_menu():
  high_scores = High_Scores()

  while True:
    ejecutar = high_scores.update()
    high_scores.draw(screen)
    if ejecutar == "main_menu":
      main_menu()
    pygame.display.update()

main_menu()
