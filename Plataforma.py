import pygame
from constantes import *
from animaciones import *
from Item import Item

class Plataforma:
  def __init__(self, ruta_imagen, cantidad, separacion, x, y, items_group, animacion_items) -> None:
    # -- Attributos
    self.cantidad = cantidad
    self.separacion = separacion
    self.ruta_imagen = ruta_imagen
    self.x = x
    self.y = y
    self.image = pygame.transform.rotozoom(
        pygame.image.load(self.ruta_imagen), 0, 0.6)
    self.rect = self.image.get_rect(topleft = (x,y))
    self.rect.width = self.image.get_width() * self.cantidad + \
        self.separacion * (self.cantidad - 1)
    # Crear los objetos Item una sola vez
    self.items = items_group

    for i in range(self.cantidad):
        y_item = self.rect.top - 30
        if animacion_items == (key_yellow or pocion_reduce):
          x_item = self.rect.left + self.rect.width / 2
          item = Item(x_item, y_item, animacion_items)
        else:
          x_item = self.rect.left + i * (self.image.get_width() + self.separacion)
          item = Item(x_item, y_item, animacion_items)

        self.items.add(item)

  def dibujar(self, pantalla):
    self.rect.x = self.x
    x = self.rect.left
    for _ in range(self.cantidad):
      pantalla.blit(self.image, (x, self.rect.y))
      x += self.image.get_width() + self.separacion
    self.items.draw(pantalla)

