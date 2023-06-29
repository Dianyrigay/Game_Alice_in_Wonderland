from Player import Player

class Level():
  """Clase padre genérica para definir un nivel"""

  def __init__(self, Player: Player, platforms_list: list, enemy_list: list) -> None:
    self.platforms_list = platforms_list
    self.enemy_list = enemy_list
    self.background = None
    self.Player = Player

    # Actualizar todo en este nivel
  def update(self, screen):
    for plataforma in self.platforms_list:
      plataforma.update(screen)
    for enemigo in self.enemy_list:
      enemigo.update(screen)

  # Dibujar todo en este nivel
  def draw(self, screen):
    screen.blit(self.background, (0,0))

    # Dibujar todas las listas de sprites
    for plataforma in self.platforms_list:
      plataforma.draw(screen)

    for enemigo in self.enemy_list:
      enemigo.draw(screen)
