import pygame
from constantes import *

class Personaje():
  """Esta es una clase padre genérica utilizada para definir un personaje"""
  def __init__(self) -> None:
    self.rect = None
    self.cuentaPasos = 0
    self.animacion = None
    self.velocidad_animacion = 10
    self.izquierda = False

  def animar_personaje(self, pantalla):
    # Asegurar que el índice esté dentro del rango válido
    indice_imagen = self.cuentaPasos // self.velocidad_animacion % len(self.animacion)
    pantalla.blit(pygame.transform.flip(self.animacion[indice_imagen], self.izquierda, False), self.rect)
