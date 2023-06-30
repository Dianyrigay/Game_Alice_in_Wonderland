import pygame
import json

from utilidades import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter
from Item import Portal

class Level():
  """Clase padre genérica para definir un nivel"""

  def __init__(self, platforms_list: list, enemy_list: list, bullets_group, bubbles_group, items_group, traps_group, piso_rect, player: Player, background, collition) -> None:
    # --List
    self.platforms_list = platforms_list
    self.enemy_list = enemy_list
    # --Group
    self.items_group = items_group
    self.traps_group = traps_group
    self.bullets_group = bullets_group
    self.bubbles_group = bubbles_group
    #-------
    self.piso_rect = piso_rect
    self.background = background
    self.player = player
    # --Colisiones
    self.collition = collition
    # --Cronometro
    self.time_game = 60000
    self.time_actual = pygame.time.get_ticks()
    self.time_transcurrido = 0
    self.time_restante = 60000

  # Actualizar todo en este nivel
  def update(self, screen):
    self.player.update(screen, self.platforms_list, self.piso_rect)

    if self.player.key_recogida:
      # TODO agregar sonido cuando abre portal
      portal = Portal(WIDTH_PANTALLA - 100, HEIGHT_PANTALLA -
                      ALTURA_PISO, open_portal)
      portal.update(screen)

    self.bullets_group.update()
    self.bubbles_group.update()
    self.items_group.update()

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.update(self.piso_rect, self.bullets_group)
      else:
        enemigo.update()

    self.collition.update(screen)

    self.update_time()

  # Dibujar todo en este nivel
  def draw(self, screen):
    screen.fill("black")
    screen.blit(self.background, (0,0))

    for plataforma in self.platforms_list:
      plataforma.draw(screen)

    self.bullets_group.draw(screen)
    self.bubbles_group.draw(screen)
    self.items_group.draw(screen)

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.draw(screen)
      else:
        enemigo.draw(screen)

    self.player.draw(screen)

    escribir_screen(screen, 'SCORE: ', "white", str(self.player.score), (20, 20))
    escribir_screen(screen, '00:', "white", str(self.time_restante).zfill(2), (WIDTH_PANTALLA/2, 20))

  def update_time(self):
    self.time_transcurrido = pygame.time.get_ticks() - self.time_actual
    self.time_restante = max(0, self.time_game - self.time_transcurrido) // 1000