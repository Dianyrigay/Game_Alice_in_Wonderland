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
    self.izquierda = False
    self.animacion = animacion
    self.muerto = False

  def update(self, pantalla, piso_rect, personaje_principal):
    self.cuentaPasos += 1
    self.rect.x = self.posicion[0]
    if self.animacion == attack_izq or self.animacion == enemy_dead:
      self.rect.bottom = piso_rect.top
    else:
      self.mover_personaje_x()

    self.verificar_colision_personaje_principal(personaje_principal)

    self.animar_personaje(pantalla)

  def verificar_colision_personaje_principal(self, personaje_principal):
    if self.rect.colliderect(personaje_principal.rect):
        if not personaje_principal.muerto:
          self.muerto = True


class EnemigoDisparador(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)

  def update(self, pantalla, piso_rect, personaje_principal):
    self.cuentaPasos += 1
    if not self.muerto:
      self.rect.x = self.posicion[0]
      self.rect.bottom = piso_rect.top
      self.verificar_colision_personaje_principal(personaje_principal)
    else:
      self.animacion = enemy_dead

    self.animar_personaje(pantalla)

  def disparar(self, balas_group):
    x = self.rect.centerx
    y = self.rect.centery
    direccion = -1  # Disparo hacia la izquierda
    # Instanciacion de balas_group
    if not self.muerto:
      bala = Bala(x, y, direccion, './images/municion_enemiga/bala_plant.py.gif')
      balas_group.add(bala)

class EnemigoMovimientoRango(Enemigo):
  def __init__(self, posicion, animacion) -> None:
    super().__init__(posicion, animacion)
    self.velocidad_x = 4

  def update(self, pantalla, personaje_principal):
    self.cuentaPasos += 1
    if not self.muerto:
      self.mover_personaje_x()
      self.verificar_colision_personaje_principal(personaje_principal)
      self.animar_personaje(pantalla)
    else:
      self.animacion = pig_dead

    self.animar_personaje(pantalla)

  def mover_personaje_x(self):
    if not self.izquierda:
      self.rect.x += self.velocidad_x
      if self.rect.right > MARGEN_DERECHO:
        self.izquierda = True

    if self.izquierda:
      self.rect.x -= self.velocidad_x
      if self.rect.left < MARGEN_IZQUIERDO:
        self.izquierda = False
