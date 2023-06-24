import pygame
from constantes import *
from Item import Item

class Plataforma:
  def __init__(self, ruta_imagen, cantidad, separacion, posicion, items_group) -> None:
    # -- Attributos
    self.cantidad = cantidad
    self.separacion = separacion
    self.ruta_imagen = ruta_imagen
    self.posicion = posicion
    self.image = pygame.transform.rotozoom(
        pygame.image.load(self.ruta_imagen), 0, 0.6)
    self.rect = self.image.get_rect(topleft = self.posicion)
    self.rect.width = self.image.get_width() * self.cantidad + \
        self.separacion * (self.cantidad - 1)
    # Crear los objetos Item una sola vez
    self.items = items_group

    for i in range(self.cantidad):
        x_item = self.rect.left + i * (self.image.get_width() + self.separacion)
        y_item = self.rect.top - 20
        item = Item(x_item, y_item, './images/items/hongo-yellow.png')
        self.items.add(item)

  def dibujar(self, pantalla):
    self.rect.x = self.posicion[0]
    x = self.rect.left
    for _ in range(self.cantidad):
      pantalla.blit(self.image, (x, self.rect.y))
      x += self.image.get_width() + self.separacion
    self.items.draw(pantalla)

