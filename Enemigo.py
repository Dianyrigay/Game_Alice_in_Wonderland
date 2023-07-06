from constantes import *
from animaciones import *

from Personaje import Personaje

class Enemigo(Personaje):
  def __init__(self, posicion: tuple, animacion: list) -> None:
    super().__init__()
    # -- Attributos
    self.velocidad_animacion = 10
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
  def __init__(self, posicion: tuple, animacion: list) -> None:
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
  def __init__(self, posicion: tuple, animacion: list, limit_left: int, limit_right: int) -> None:
    super().__init__(posicion, animacion)
    self.velocidad_x = 3
    self.limit_left = limit_left
    self.limit_right = limit_right

  def update(self):
    super().update()
    if not self.muerto:
      self.mover_personaje_x()

  def draw(self, screen):
    super().draw(screen, pig_dead)

  def mover_personaje_x(self):
    if not self.izquierda:
      self.rect.x += self.velocidad_x
      if self.rect.right > self.limit_right:
        self.izquierda = True

    if self.izquierda:
      self.rect.x -= self.velocidad_x
      if self.rect.left < self.limit_left:
        self.izquierda = False

class Enemy_Attack(Enemigo):
  def __init__(self, posicion: tuple, animacion: list) -> None:
    super().__init__(posicion, animacion)
    self.velocidad_x = 2
    self.lives = 3

  def update(self, player_rect, platforms_list):
    super().update()
    if not self.muerto:
      self.mover_personaje_x()
      self.check_collision(platforms_list)
      if self.rect.y <= player_rect.y and abs(self.rect.x - player_rect.x) <= 500:
        self.attack_player(player_rect, platforms_list)
      else:
        self.animacion = cuervo_walk
      if self.velocidad_x > 0:
        self.izquierda = False
      else:
        self.izquierda = True

  def draw(self, screen):
    super().draw(screen, cuervo_hit)

  def attack_player(self, player_rect, platforms_list):
    self.check_collision(platforms_list)
    self.animacion = cuervo_attack
    if self.rect.x < player_rect.x:
        self.velocidad_x = 3
    else:
        self.velocidad_x = -3

  def mover_personaje_x(self):
    self.rect.x += self.velocidad_x

  def check_collision(self, platforms_list):
      for plataforma in platforms_list:
          if self.rect.colliderect(plataforma.rect):
              self.invert_direction()
              break
      if self.rect.left < 0 or self.rect.right > WIDTH_PANTALLA:
          self.invert_direction()

  def invert_direction(self):
      self.velocidad_x *= -1
