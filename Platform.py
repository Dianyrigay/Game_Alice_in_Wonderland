import pygame
from constantes import *
from animations import *
from Item import Item, Trap
from player import Player

class Platform:
  def __init__(self, path, cantidad, separacion, x, y, group, animation_items = None) -> None:
    # -- Attributos
    self.cantidad = cantidad
    self.separacion = separacion
    self.path = path
    self.animation_items = animation_items
    self.x = x
    self.y = y
    self.image = pygame.transform.rotozoom(
        pygame.image.load(self.path), 0, 0.6).convert_alpha()
    self.rect = self.image.get_rect(topleft = (x,y))
    self.rect.width = self.image.get_width() * self.cantidad + \
        self.separacion * (self.cantidad - 1)
    # Instancia los Items
    self.group = group
    self.draw_items()

  def draw_items(self):
    if self.animation_items != None:
        for i in range(self.cantidad):
            y_item = self.rect.top - 10
            if type(self.animation_items) == type(str()):
                if self.animation_items == key_yellow or self.animation_items == pocion_reduce or self.animation_items == key_red or self.animation_items == live_item:
                    x_item = self.rect.left + self.rect.width / 2
                    item = Item(x_item, y_item, self.animation_items)
                else:
                    x_item = self.rect.left + i * (self.image.get_width() + self.separacion)
                    item = Item(x_item, y_item, self.animation_items)
            else:
                x_item = self.rect.left + self.rect.width / 2
                item = Trap(x_item, y_item, self.animation_items)
            self.group.add(item)

  def update(self):
    self.rect.x = self.x

  def draw(self, screen):
    x = self.rect.left
    for _ in range(self.cantidad):
      screen.blit(self.image, (x, self.rect.y))
      x += self.image.get_width() + self.separacion
    if self.animation_items != None:
        if type(self.animation_items) == type(str()):
            self.group.draw(screen)
        else:
            self.group.update(screen)

class MovingPlatform(Platform):
  def __init__(self, path, cantidad, separacion, x, y, group, limit_left, limit_rigth, change_x, change_y, limit_top, limit_bottom, player: Player, animation_items):
      super().__init__(path, cantidad, separacion, x, y, group, animation_items)

      self.change_x = change_x
      self.change_y = change_y

      self.limit_top = limit_top
      self.limit_bottom = limit_bottom
      self.limit_left = limit_left
      self.limit_right = limit_rigth

      self.player = player

#   def draw_items(self):
#     super().draw_items()

  def draw(self, screen):
     super().draw(screen)

  def update(self):
    self.rect.x += self.change_x

    for item in self.group:
        if item.animation == taza1:
            item.rect.x += self.change_x

    hit = pygame.sprite.collide_rect(self, self.player)
    if hit:
        if self.change_x < 0:
            self.player.rect.right = self.rect.left
        else:
            self.player.rect.left = self.rect.right

    if self.player.rect.bottom == self.rect.top:
        if self.change_x != 0:
            self.player.rect.x += self.change_x
        else:
            self.player.rect.y += self.change_y

    self.rect.y += self.change_y

    hit = pygame.sprite.collide_rect(self, self.player)
    if hit:
        if self.change_y < 0:
            self.player.rect.bottom = self.rect.top
        else:
            self.player.rect.top = self.rect.bottom

    if self.rect.bottom > self.limit_bottom or self.rect.top < self.limit_top:
        self.change_y *= -1

    if self.rect.left < self.limit_left or self.rect.right > self.limit_right:
        self.change_x *= -1

