import pygame
import random

from enemigo import Enemy_Moving
from animations import pig_fly

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, animation) -> None:
    super().__init__()
    # -- Attributos
    self.animation = animation
    self.image = pygame.image.load(self.animation).convert_alpha()
    self.rect = self.image.get_rect(midbottom=(x, y))
    self.move = False

class Portal():
  def __init__(self, x, y, animation) -> None:
    self.speed_animation = 10
    self.cuenta_pasos = 0
    self.left = True
    self.animation = animation
    self.rect = self.animation[0].get_rect(midbottom=(x,y))

  def update(self):
    self.cuenta_pasos += 1

  def draw(self, screen):
    indice_imagen = self.cuenta_pasos // self.speed_animation % len(self.animation)
    screen.blit(pygame.transform.flip(self.animation[indice_imagen], self.left, False), self.rect)

class Trap(pygame.sprite.Sprite):
  def __init__(self, x, y, animation) -> None:
    super().__init__()
    self.speed_animation = 10
    self.cuenta_pasos = 0
    self.left = True
    self.animation = animation
    self.image = self.animation[0]
    self.rect = self.image.get_rect(midbottom=(x, y))

  def update(self, screen):
    self.cuenta_pasos += 1
    self.animar_objeto(screen)

  def animar_objeto(self, screen):
    indice_imagen = self.cuenta_pasos // self.speed_animation % len(
        self.animation)
    screen.blit(pygame.transform.flip(
        self.animation[indice_imagen], self.left, False), self.rect)

  def create_random_enemy(self, enemy_list):
    y = 200
    x = 850
    for _ in range(3):
      enemy_types = [Enemy_Moving]
      random_enemy_type = random.choice(enemy_types)
      random_enemy = random_enemy_type((x, y), pig_fly)
      enemy_list.append(random_enemy)
      y += 200
      x += 100
