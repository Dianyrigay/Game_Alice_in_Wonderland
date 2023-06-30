import pygame
from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving

class Level():
  """Clase padre genérica para definir un nivel"""

  def __init__(self, platforms_list: list, enemy_list: list, rectangles_list: list, bullets_group, bubbles_group, items_group, traps_group, piso_rect, player: Player, background, colisiones) -> None:
    # --List
    self.platforms_list = platforms_list
    self.enemy_list = enemy_list
    self.rectangles_list = rectangles_list
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
    self.colisiones = colisiones

  # Actualizar todo en este nivel
  def update(self, screen):
    self.player.update(screen, self.rectangles_list)

    self.bullets_group.update()
    self.bubbles_group.update()
    self.items_group.update()

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.update(self.piso_rect, self.bullets_group)
      else:
        enemigo.update()

    self.colisiones.update(screen)

  # Dibujar todo en este nivel
  def draw(self, screen):
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
