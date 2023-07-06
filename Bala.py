import pygame

class Bala(pygame.sprite.Sprite):
  def __init__(self, x, y, direccion, imagen) -> None:
    super().__init__()
    # -- Attributos
    self.velocidad = 10
    self.image = imagen
    self.rect = self.image.get_rect(topleft = (0,0))
    self.rect.center = (x,y)
    self.direccion = direccion

  def update(self, screen):
    self.rect.x += self.velocidad * self.direccion
    self.draw(screen)

  def draw(self, screen):
    if self.direccion == 1:
      izquierda = False
    else:
      izquierda = True
    screen.blit(pygame.transform.flip(self.image, izquierda, False), self.rect)
