from constantes import *
from animaciones import *
from Bala import Bala
from Personaje import Personaje

class Enemigo(Personaje):
  def __init__(self, posicion, animacion) -> None:
    super().__init__()
    # -- Attributos
    self.posicion = posicion
    self.rect = animacion[0].get_rect(
        midbottom=posicion)
    # self.izquierda = False
    self.animacion = animacion
    # self.muerto = False
    self.contador_muerte = 30

  def update(self, pantalla, piso_rect, personaje_principal, animacion_muerte):
    self.cuentaPasos += 1

    if not self.muerto:
      # self.verificar_colision_personaje_principal(personaje_principal)
      self.animar_personaje(pantalla)
    elif self.muerto and self.contador_muerte > 0:
      self.animacion = animacion_muerte
      self.animar_personaje(pantalla)
      self.contador_muerte -= 1

  # def verificar_colision_personaje_principal(self, personaje_principal):
  #   if self.rect.colliderect(personaje_principal.rect):
  #       if not personaje_principal.muerto:
  #         self.muerto = True

class EnemigoDisparador(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)

  def update(self, pantalla, piso_rect, personaje_principal):
    super().update(pantalla,piso_rect, personaje_principal, enemy_dead)
    if not self.muerto:
      self.mover_personaje_x(piso_rect)

  def disparar(self, balas_group):
    x = self.rect.centerx
    y = self.rect.centery
    direccion = -1
    if not self.muerto:
    # Instanciacion de balas_group
      bala = Bala(x, y, direccion, bala_plant)
      balas_group.add(bala)

  def mover_personaje_x(self, piso_rect):
    self.rect.bottom = piso_rect.top

class EnemigoMovimientoRango(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)
    self.velocidad_x = 2

  def update(self, pantalla, piso_rect, personaje_principal):
    super().update(pantalla, piso_rect, personaje_principal, pig_dead)
    if not self.muerto:
      self.mover_personaje_x()

  def mover_personaje_x(self):
    if not self.izquierda:
      self.rect.x += self.velocidad_x
      if self.rect.right > MARGEN_DERECHO:
        self.izquierda = True

    if self.izquierda:
      self.rect.x -= self.velocidad_x
      if self.rect.left < MARGEN_IZQUIERDO:
        self.izquierda = False
