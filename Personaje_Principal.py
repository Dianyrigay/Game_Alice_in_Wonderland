from constantes import *
from animaciones import *

from Personaje import Personaje

class Personaje_Principal(Personaje):
  def __init__(self) -> None:
    super().__init__()
    # -- Attributos
    self.rect = quieto[0].get_rect(topleft=(0, 0))
    self.velocidad_x = 0
    self.velocidad_y = 0
    self.gravedad = 0.9
    self.potencia_salto = -19
    self.esta_cayendo = False
    self.vidas = 3
    self.cadencia = 10

  def mover_personaje_x(self):
    self.rect.x += self.velocidad_x

    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > WIDTH_PANTALLA:
        self.rect.right = WIDTH_PANTALLA

  def mover_personaje_y(self):
    self.rect.y += self.velocidad_y

    if self.rect.bottom > HEIGHT_PANTALLA:
      self.rect.bottom = HEIGHT_PANTALLA

  def calcular_gravedad(self):
    if self.velocidad_y == 0:
      self.velocidad_y = 1
    else:
      self.esta_cayendo = True
      self.velocidad_y += self.gravedad

    # Verifico si esta en el suelo
    if self.rect.bottom == HEIGHT_PANTALLA - ALTURA_PISO and self.velocidad_y >= 0:
      self.velocidad_y = 0

  def update(self, pantalla, lista_plataformas):
    self.cuenta_pasos += 1

    if self.vidas > 0:
      self.mover_personaje_x()
      self.mover_personaje_y()
      self.calcular_gravedad()
      self.verificar_colisiones_plataformas(lista_plataformas)
      if self.esta_cayendo:
        self.animacion = floating
    elif self.vidas <= 0 and self.contador_muerte > 0:
      self.animacion = dead
      self.contador_muerte -= 1
    else:
      self.muerto = True

    self.animar_personaje(pantalla)

  # control de moivimientos del Personaje:
  def saltar(self):
    if self.izquierda:
      self.velocidad_x = -2
    else:
      self.velocidad_x = 2
    self.animacion = floating
    self.velocidad_y = self.potencia_salto

  def flotar(self):
    self.animacion = floating
    self.velocidad_y = 5

  def mover_izquierda(self):
    self.animacion = camina
    self.izquierda = True
    self.velocidad_x = -8

  def mover_derecha(self):
    self.animacion = camina
    self.izquierda = False
    self.velocidad_x = 8

  def quieto(self):
    self.animacion = quieto
    self.velocidad_x = 0

  def restar_vidas(self):
    #TODO arreglar porque no se esta reproduciendo
    self.animacion = angry
    self.vidas -= 1

  def disparar(self, burbujas_group):
    super().disparar(burbujas_group, burbuja_bala)

  def verificar_colisiones_plataformas(self, lista_plataformas):
    for plataforma in lista_plataformas:
        if self.rect.colliderect(plataforma):
            self.esta_cayendo = False
            if self.velocidad_y > 0:
                self.velocidad_y = 0
                self.rect.bottom = plataforma.top
            elif self.velocidad_y < 0:
                self.rect.top = plataforma.bottom
                self.velocidad_y = 0

            if not self.rect.bottom == plataforma.top and not self.rect.top == plataforma.bottom:
                if self.velocidad_x > 0:
                    self.rect.right = plataforma.left
                    self.velocidad_x = 0
                elif self.velocidad_x < 0:
                    self.rect.left = plataforma.right
                    self.velocidad_x = 0
