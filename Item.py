import pygame

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, ruta_imagen) -> None:
    super().__init__()

    # -- Attributos
    self.image = pygame.image.load(ruta_imagen)
    self.rect = self.image.get_rect(topleft=(0, 0))
    self.rect.center = (x, y)
