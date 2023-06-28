import pygame
from constantes import *
from animaciones import *
from Item import Item

class Platform:
  def __init__(self, ruta_imagen, cantidad, separacion, x, y, items_group, animacion_items) -> None:
    # -- Attributos
    self.cantidad = cantidad
    self.separacion = separacion
    self.ruta_imagen = ruta_imagen
    self.x = x
    self.y = y
    self.image = pygame.transform.rotozoom(
        pygame.image.load(self.ruta_imagen), 0, 0.6).convert_alpha()
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


class MovingPlatform(Platform):
  """ This is a fancier platform that can actually move. """
  def __init__(self, sprite_sheet_data):

      super().__init__(sprite_sheet_data)

      self.change_x = 0
      self.change_y = 0

      self.limit_top = 0
      self.limit_bottom = 0
      self.limit_left = 0
      self.limit_right = 0

      self.level = None
      self.player = None


  def update(self):
      # Move left/right
      self.rect.x += self.change_x

      # ver si golpeamos al jugador
      hit = pygame.sprite.collide_rect(self, self.player)
      if hit:
          # Choca con el jugador. Empuja al jugador y
          # asume que él/ella no golpeará nada más.

            # Si nos estamos moviendo a la derecha, establece nuestro lado derecho
          # al lado izquierdo del elemento que golpeamos
          if self.change_x < 0:
              self.player.rect.right = self.rect.left
          else:
              # De lo contrario, si nos estamos moviendo hacia la izquierda, haga lo contrario.
              self.player.rect.left = self.rect.right

      # Move up/down
      self.rect.y += self.change_y

      # Compruebe y vea si nosotros el jugador
      hit = pygame.sprite.collide_rect(self, self.player)
      if hit:
          # Choca con el jugador. Empuja al jugador y
          # asume que él/ella no golpeará nada más.

          # Restablecer nuestra posición en función de la parte superior/inferior del objeto.
          if self.change_y < 0:
              self.player.rect.bottom = self.rect.top
          else:
              self.player.rect.top = self.rect.bottom

      if self.rect.bottom > self.limit_bottom or self.rect.top < self.limit_top:
          self.change_y *= -1

      cur_pos = self.rect.x - self.level.world_shift
      if cur_pos < self.limit_left or cur_pos > self.limit_right:
          self.change_x *= -1
