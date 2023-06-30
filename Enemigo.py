from constantes import *
from animaciones import *

from Personaje import Personaje

class Enemigo(Personaje):
  def __init__(self, posicion, animacion) -> None:
    super().__init__()
    # -- Attributos
    self.posicion = posicion
    self.rect = animacion[0].get_rect(
        midbottom=posicion)
    self.animacion = animacion
    self.cadencia = TIEMPO_ENTRE_DISPAROS
    self.ultimo_disparo = pygame.time.get_ticks()

  def update(self):
    self.cuenta_pasos += 1

  def draw(self, screen, animacion_muerte):
    if not self.muerto:
      self.animar_personaje(screen)
    elif self.muerto and self.contador_muerte > 0:
      self.animacion = animacion_muerte
      self.animar_personaje(screen)
      self.contador_muerte -= 1

class Enemy_Shooter(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)
    self.izquierda = True

  def update(self, piso_rect, bullets_group):
    super().update()
    if not self.muerto:
      self.mover_personaje_x(piso_rect)
      self.disparar(bullets_group)

  def draw(self, screen):
    super().draw(screen, plant_dead)

  def disparar(self, bullets_group):
    super().disparar(bullets_group, bala_plant)

  def mover_personaje_x(self, piso_rect):
    self.rect.bottom = piso_rect.top

class Enemy_Moving(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)
    self.velocidad_x = 4

  def update(self):
    super().update()
    if not self.muerto:
      self.mover_personaje_x()

  def draw(self, screen):
    super().draw(screen, pig_dead)

  def mover_personaje_x(self):
    if not self.izquierda:
      self.rect.x += self.velocidad_x
      if self.rect.right > MARGEN_DERECHO:
        self.izquierda = True

    if self.izquierda:
      self.rect.x -= self.velocidad_x
      if self.rect.left < MARGEN_IZQUIERDO:
        self.izquierda = False
