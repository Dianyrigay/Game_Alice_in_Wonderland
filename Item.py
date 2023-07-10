import pygame
import random

from Enemigo import Enemy_Moving
from animaciones import pig_fly

class Item(pygame.sprite.Sprite):
  def __init__(self, x, y, animacion) -> None:
    super().__init__()
    # -- Attributos
    self.animacion = animacion
    self.image = pygame.image.load(self.animacion).convert_alpha()
    self.rect = self.image.get_rect(midbottom=(x, y))
    self.move = False

class Portal():
  def __init__(self, x, y, animacion) -> None:
    self.velocidad_animacion = 10
    self.cuenta_pasos = 0
    self.izquierda = True
    self.animacion = animacion
    self.rect = self.animacion[0].get_rect(midbottom=(x,y))

  def update(self):
    self.cuenta_pasos += 1

  def draw(self, screen):
    indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(self.animacion)
    screen.blit(pygame.transform.flip(self.animacion[indice_imagen], self.izquierda, False), self.rect)

class Trap(pygame.sprite.Sprite):
  def __init__(self, x, y, animacion) -> None:
    super().__init__()
    self.velocidad_animacion = 10
    self.cuenta_pasos = 0
    self.izquierda = True
    self.animacion = animacion
    self.image = self.animacion[0]
    self.rect = self.image.get_rect(midbottom=(x, y))

  def update(self, screen):
    self.cuenta_pasos += 1
    self.animar_objeto(screen)

  def animar_objeto(self, screen):
    indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(
        self.animacion)
    screen.blit(pygame.transform.flip(
        self.animacion[indice_imagen], self.izquierda, False), self.rect)

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
