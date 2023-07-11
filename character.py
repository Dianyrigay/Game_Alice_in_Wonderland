import pygame

from constantes import bubble_sound, knife_sound

from animations import bubble, knife
from bala import Bala

class Character():
  def __init__(self) -> None:
    self.rect = None
    self.cuenta_pasos = 0
    self.animation = None
    self.speed_animation = 10
    self.left = False
    self.muerto = False
    self.contador_muerte = 30

  def animar_personaje(self, screen) -> None:
    indice_imagen = self.cuenta_pasos // self.speed_animation % len(self.animation)
    screen.blit(pygame.transform.flip(self.animation[indice_imagen], self.left, False), self.rect)

  def disparar(self, grupo_municion, imagen_bala):
    if self.cuenta_pasos % self.cadencia == 0:
      if imagen_bala == bubble:
        bubble_sound.play()
      elif imagen_bala == knife:
        knife_sound.play()
      y = self.rect.centery
      if self.left:
        x = self.rect.left
        direccion = -1
      else:
        x = self.rect.right
        direccion = 1
      if not self.muerto:
        municion = Bala(x, y, direccion, imagen_bala)
        grupo_municion.add(municion)