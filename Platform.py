import pygame
from constantes import *
from animaciones import *
from Item import Item, Trap

class Platform:
  def __init__(self, path, cantidad, separacion, x, y, group, animacion_items = None) -> None:
    # -- Attributos
    self.cantidad = cantidad
    self.separacion = separacion
    self.path = path
    self.animacion_items = animacion_items
    self.x = x
    self.y = y
    self.image = pygame.transform.rotozoom(
        pygame.image.load(self.path), 0, 0.6).convert_alpha()
    self.rect = self.image.get_rect(topleft = (x,y))
    self.rect.width = self.image.get_width() * self.cantidad + \
        self.separacion * (self.cantidad - 1)
    # Crear los objetos Item una sola vez
    self.group = group

    self.draw_items()

  def draw_items(self):
    for i in range(self.cantidad):
        y_item = self.rect.top - 10
        if type(self.animacion_items) == type(str()):
            if self.animacion_items == (key_yellow or pocion_reduce):
                x_item = self.rect.left + self.rect.width / 2
                item = Item(x_item, y_item, self.animacion_items)
            else:
                x_item = self.rect.left + i * (self.image.get_width() + self.separacion)
                item = Item(x_item, y_item, self.animacion_items)
        else:
            x_item = self.rect.left + self.rect.width / 2
            item = Trap(x_item, y_item, self.animacion_items)
        self.group.add(item)

  def draw(self, screen):
    self.rect.x = self.x
    x = self.rect.left
    for _ in range(self.cantidad):
      screen.blit(self.image, (x, self.rect.y))
      x += self.image.get_width() + self.separacion
    if type(self.animacion_items) == type(str()):
        self.group.draw(screen)
    else:
        self.group.update(screen)

class MovingPlatform(Platform):
  def __init__(self):
      super().__init__()

      self.change_x = 0
      self.change_y = 0

      self.limit_top = 0
      self.limit_bottom = 0
      self.limit_left = 0
      self.limit_right = 0

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

    #   cur_pos = self.rect.x - self.level.world_shift
    #   if cur_pos < self.limit_left or cur_pos > self.limit_right:
    #       self.change_x *= -1
