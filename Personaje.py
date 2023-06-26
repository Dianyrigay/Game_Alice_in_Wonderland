import pygame

from constantes import *

from Bala import Bala

class Personaje():
  """Esta es una clase padre genérica utilizada para definir un personaje"""
  def __init__(self) -> None:
    self.rect = None
    self.cuenta_pasos = 0
    self.animacion = None
    self.velocidad_animacion = 10
    self.izquierda = False
    self.muerto = False
    self.contador_muerte = 30

  def animar_personaje(self, pantalla):
    # Asegurar que el índice esté dentro del rango válido
    indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(self.animacion)
    pantalla.blit(pygame.transform.flip(self.animacion[indice_imagen], self.izquierda, False), self.rect)

  def disparar(self, grupo_municion, imagen_bala):
    if self.cuenta_pasos % self.cadencia == 0:
      y = self.rect.centery
      if self.izquierda:
        x = self.rect.left
        direccion = -1
      else:
        x = self.rect.right
        direccion = 1
      if not self.muerto:
        # Instanciacion de Bala
        municion = Bala(x, y, direccion, imagen_bala)
        grupo_municion.add(municion)
