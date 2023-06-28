from constantes import *
from animaciones import *

from Personaje import Personaje

class Player(Personaje):
  def __init__(self) -> None:
    super().__init__()
    # -- Attributos
    self.rect = quieto[0].get_rect(topleft=(0, 0))
    self.velocidad_x = 0
    self.velocidad_y = 0
    self.gravedad = 0.9
    self.potencia_salto = -19
    self.esta_cayendo = False
    self.entrada_cayendo = True
    self.vidas = 3
    self.cadencia = 10
    self.contador_cambio_animacion = 30
    self.score = 300
    self.key_recogida = False

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

  def update(self, screen, platforms_list):
    self.cuenta_pasos += 1

    if self.vidas > 0:
      self.mover_personaje_x()
      self.mover_personaje_y()
      self.calcular_gravedad()
      self.verificar_colisiones_plataformas(platforms_list)
      if self.esta_cayendo:
        self.animacion = floating
    elif self.vidas <= 0 and self.contador_muerte > 0:
      self.animacion = dead
      self.contador_muerte -= 1
    else:
      self.muerto = True

    if self.animacion == angry or self.animacion == reducir:
       self.contador_cambio_animacion -= 1

    self.animar_personaje(screen)

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
    self.animacion = angry
    self.vidas -= 1

  def disparar(self, bubbles_group):
    super().disparar(bubbles_group, burbuja_bala)

  def reducir(self):
    x = self.rect.x
    y = self.rect.y
    self.animacion = reducir
    reescalar_imagen(lista_animaciones_alice, 0.35)
    #TODO reducir la burbuja tambien, ver donde debo reducirla
    # reescalar_imagen([[burbuja_bala]],0.01)
    self.rect = quieto[0].get_rect(topleft=(x, y))

  def eventos(self, keys, bubbles_group):

    if not self.esta_cayendo:
      if self.entrada_cayendo:
        self.flotar()
        self.entrada_cayendo = False
      elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        self.saltar()
      elif keys[pygame.K_LEFT]:
        self.mover_izquierda()
      elif keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        self.saltar()
      elif keys[pygame.K_RIGHT]:
        self.mover_derecha()
      elif keys[pygame.K_SPACE]:
        self.saltar()
      elif (keys[pygame.K_x]):
        #TODO agregar que pueda disparar mientras camina
        self.disparar(bubbles_group)
      else:
        if self.contador_cambio_animacion <= 0 and self.animacion == angry:
          self.quieto()
          self.contador_cambio_animacion = 30
        elif self.animacion != angry:
          self.quieto()

  def verificar_colisiones_plataformas(self, platforms_list):
    for plataforma in platforms_list:
        if self.rect.colliderect(plataforma):
            if self.velocidad_y > 0 and self.esta_cayendo:
                self.velocidad_y = 0
                self.rect.bottom = plataforma.top
                self.esta_cayendo = False
            elif self.velocidad_y < 0:
                self.esta_cayendo = False
                self.rect.top = plataforma.bottom
                self.velocidad_y = 0

            if not self.rect.bottom == plataforma.top and not self.rect.top == plataforma.bottom:
                if self.velocidad_x > 0:
                    self.rect.right = plataforma.left
                    self.velocidad_x = 0
                elif self.velocidad_x < 0:
                    self.rect.left = plataforma.right
                    self.velocidad_x = 0