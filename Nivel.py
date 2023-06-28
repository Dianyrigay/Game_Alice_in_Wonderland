class Level():
  """Esta es una clase padre genérica utilizada para definir un nivel"""

  def __init__(self, Player, platforms_list, enemy_list):
    self.platforms_list = platforms_list
    self.enemy_list = enemy_list
    self.fondo_imagen = None
    self.Player = Player

    # Actualizar todo en este nivel
  def update(self, pantalla):
    for plataforma in self.platforms_list:
      plataforma.update(pantalla)
    for enemigo in self.enemy_list:
      enemigo.update(pantalla)

  # Dibujar todo en este nivel
  def dibujar(self, pantalla):
    # Dibujar el fondo
    pantalla.blit(self.fondo_imagen, (0,0))

    # Dibujar todas las listas de sprites
    for plataforma in self.platforms_list:
      plataforma.dibujar(pantalla)

    for enemigo in self.enemy_list:
      enemigo.dibujar(pantalla)
