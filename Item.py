import pygame
# from pygame.sprite import _Group

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, animacion) -> None:
    super().__init__()
    # -- Attributos
    self.animacion = animacion
    self.image = pygame.image.load(self.animacion).convert_alpha()
    self.rect = self.image.get_rect(midbottom=(x, y))

class Portal():
  def __init__(self, x, y, animacion) -> None:
    self.velocidad_animacion = 10
    self.cuenta_pasos = 0
    self.izquierda = True
    self.animacion = animacion
    self.rect = self.animacion[0].get_rect(midbottom=(x,y))

  def update(self, pantalla):
    self.cuenta_pasos += 1
    self.animar_objeto(pantalla)

  def animar_objeto(self, pantalla):
    indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(self.animacion)
    pantalla.blit(pygame.transform.flip(self.animacion[indice_imagen], self.izquierda, False), self.rect)

class Trap(pygame.sprite.Sprite):
  def __init__(self, x, y, animacion) -> None:
    super().__init__()
    self.velocidad_animacion = 10
    self.cuenta_pasos = 0
    self.izquierda = True
    self.animacion = animacion
    self.image = self.animacion[0]
    self.rect = self.image.get_rect(midbottom=(x, y))

  def update(self, pantalla):
    self.cuenta_pasos += 1
    self.animar_objeto(pantalla)


  def animar_objeto(self, pantalla):
    indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(
        self.animacion)
    pantalla.blit(pygame.transform.flip(
        self.animacion[indice_imagen], self.izquierda, False), self.rect)
