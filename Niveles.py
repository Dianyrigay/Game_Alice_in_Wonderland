import pygame
from constantes import *
from Plataforma import Plataforma
from Nivel import Nivel

class Nivel_01(Nivel):
  """ Definición para el nivel 1"""

  def __init__(self, Player):
    super().__init__(self, Player)

    self.fondo_imagen = pygame.transform.scale(pygame.image.load(
            "./images/fondo_niveles/nivel-01.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
    self.level_limit = -2500

    # Array con tipo de plataforma, y ​​ubicación x, y de la plataforma.
    nivel = [[AREA_1, 300, 500],
            [AREA_1, 650, 450]]

    # Agregar las plataformas
    for plataforma in nivel:
      bloque = Plataforma(plataforma[0], 3, 0, (plataforma[1], plataforma[2])) #Falta el items_group que lo pido
      bloque.rect.x = plataforma[1]
      bloque.rect.y = plataforma[2]
      bloque.Player = self.Player
      self.lista_plataformas.add(bloque)


