class Level():
  """Esta es una clase padre genérica utilizada para definir un nivel"""

  def __init__(self, Player, lista_plataformas, lista_enemigos):
    self.lista_plataformas = lista_plataformas
    self.lista_enemigos = lista_enemigos
    self.fondo_imagen = None
    self.Player = Player

    # Actualizar todo en este nivel
  def update(self, pantalla):
    for plataforma in self.lista_plataformas:
      plataforma.update(pantalla)
    for enemigo in self.lista_enemigos:
      enemigo.update(pantalla)

  # Dibujar todo en este nivel
  def dibujar(self, pantalla):
    # Dibujar el fondo
    pantalla.blit(self.fondo_imagen, (0,0))

    # Dibujar todas las listas de sprites
    for plataforma in self.lista_plataformas:
      plataforma.dibujar(pantalla)

    for enemigo in self.lista_enemigos:
      enemigo.dibujar(pantalla)
