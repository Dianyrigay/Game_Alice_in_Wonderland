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
  def __init__(self, posicion: tuple, list_animations: list) -> None:
    super().__init__(posicion, list_animations[0])
    self.velocidad_x = 2
    self.lives = 3
    self.list_animations = list_animations

  def update(self, player_rect, platforms_list):
    super().update()
    if not self.muerto:
      self.mover_personaje_x()
      self.check_collision(platforms_list)
      if self.rect.y <= player_rect.y and abs(self.rect.x - player_rect.x) <= 200:
        self.attack_player(player_rect, platforms_list)
      else:
        self.animacion = self.list_animations[0]
      if self.velocidad_x > 0:
        self.izquierda = False
      else:
        self.izquierda = True

  def draw(self, screen):
    super().draw(screen, self.list_animations[1])

  def attack_player(self, player_rect, platforms_list):
    self.check_collision(platforms_list)
    self.animacion = self.list_animations[2]
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

class Enemy_Boss(Enemigo):
  def __init__(self, posicion: tuple, list_animations: list) -> None:
    super().__init__(posicion, list_animations[0])
    self.list_animations = list_animations
    self.lives = 5
    self.is_jumping = False
    self.jump_height = 150
    self.jump_duration = 60
    self.jump_timer = 0
    self.velocidad_x = 0
    self.izquierda = True
    self.velocidad_animacion = 40
    self.cadencia = 100

  def update(self, player_rect, platforms_list, bullets_group):
    super().update()
    if not self.muerto:
      if not self.is_jumping:
        self.mover_personaje_x()
        self.check_collision()
        if self.rect.y <= player_rect.y and abs(self.rect.x - player_rect.x) <= 300:
          self.attack_player(player_rect, bullets_group)
        else:
          self.velocidad_x = 0
          self.animacion = self.list_animations[0]
      else:
        self.jump_timer += 1
        if self.jump_timer <= self.jump_duration:
          self.mover_personaje_y()
        else:
          self.is_jumping = False
          self.jump_timer = 0
          self.animacion = self.list_animations[0]
          self.rect.y = self.posicion[1]
      if self.velocidad_x > 0:
        self.izquierda = False
      else:
        self.izquierda = True

  def draw(self, screen):
    super().draw(screen, self.list_animations[2])

  def attack_player(self, player_rect, bullets_group, ):
    self.animacion = self.list_animations[1]
    if self.rect.x < player_rect.x:
      self.velocidad_x = 3
    else:
      self.velocidad_x = -3
    self.disparar(bullets_group)

  def mover_personaje_x(self):
    self.rect.x += self.velocidad_x

  def mover_personaje_y(self):
    if self.jump_timer <= self.jump_duration // 2:
      self.rect.y -= self.jump_height // (self.jump_duration // 2)
    else:
      self.rect.y += self.jump_height // (self.jump_duration // 2)

  def disparar(self, bullets_group):
    super().disparar(bullets_group, bala_dead)
    if self.lives < 5:
      self.create_random_enemy()

  def create_random_enemy(self):
    print('generar enemigo random')
    pass

  def check_collision(self):
    if self.rect.left < 0 or self.rect.right > WIDTH_PANTALLA:
      self.invert_direction()

  def invert_direction(self):
    self.velocidad_x *= -1

  def recibir_disparo(self):
    if not self.is_jumping:
      self.is_jumping = True
      self.animacion = self.list_animations[2]
