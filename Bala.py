import pygame

class Bala(pygame.sprite.Sprite):
  def __init__(self, x, y, direccion, ruta_imagen) -> None:
    super().__init__()
    # -- Attributos
    self.velocidad = 10
    self.image = pygame.image.load(ruta_imagen)
    self.rect = self.image.get_rect(topleft = (0,0))
    self.rect.center = (x,y)
    self.direccion = direccion

  def update(self):
    # Mover la bala horizontalmente según la dirección
    self.rect.x += self.velocidad * self.direccion
