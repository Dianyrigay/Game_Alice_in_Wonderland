class Level():
  """Esta es una clase padre genérica utilizada para definir un nivel"""

  def __init__(self, Player, platforms_list, enemy_list):
    self.platforms_list = platforms_list
    self.enemy_list = enemy_list
    self.background_1 = None
    self.Player = Player

    # Actualizar todo en este nivel
  def update(self, screen):
    for plataforma in self.platforms_list:
      plataforma.update(screen)
    for enemigo in self.enemy_list:
      enemigo.update(screen)

  # Dibujar todo en este nivel
  def dibujar(self, screen):
    # Dibujar el fondo
    screen.blit(self.background_1, (0,0))

    # Dibujar todas las listas de sprites
    for plataforma in self.platforms_list:
      plataforma.dibujar(screen)

    for enemigo in self.enemy_list:
      enemigo.dibujar(screen)
