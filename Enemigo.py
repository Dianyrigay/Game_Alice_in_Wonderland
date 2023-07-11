import random

from constantes import *
from animations import *

from character import Character
from healthbar import HealthBar

class Enemy(Character):
  def __init__(self, posicion: tuple, animation: list) -> None:
    super().__init__()
    # -- Attributos
    self.speed_animation = 10
    self.posicion = posicion
    self.rect = animation[0].get_rect(midbottom=posicion)
    self.animation = animation
    self.cadencia = TIEMPO_ENTRE_DISPAROS
    self.ultimo_disparo = pygame.time.get_ticks()
    self.animation_death = None
    self.speed_x = 0

  def update(self, platforms_list):
    self.cuenta_pasos += 1
    if not self.muerto:
      self.mover_personaje_x()
      self.check_collision(platforms_list)
    if self.speed_x > 0:
      self.left = False
    else:
      self.left = True

  def draw(self, screen):
    if not self.muerto:
      self.animar_personaje(screen)
    elif self.muerto and self.contador_muerte > 0:
      self.animation = self.animation_death
      self.animar_personaje(screen)
      self.contador_muerte -= 1

  def mover_personaje_x(self):
    self.rect.x += self.speed_x

  def check_collision(self, platforms_list):
    for plataforma in platforms_list:
        if self.rect.colliderect(plataforma.rect):
            self.invert_direction()
            break
    if self.rect.left < 0 or self.rect.right > WIDTH_PANTALLA:
        self.invert_direction()

  def invert_direction(self):
    self.speed_x *= -1

class Enemy_Shooter(Enemy):
  def __init__(self, posicion: tuple, animation: list) -> None:
    super().__init__(posicion, animation)
    self.left = True
    self.animation_death = plant_dead
    self.speed_x = 0

  def update(self, bullets_group, platforms_list):
    super().update(platforms_list)
    if not self.muerto:
      self.disparar(bullets_group)

  def disparar(self, bullets_group):
    super().disparar(bullets_group, bala_plant)

class Enemy_Moving(Enemy):
  def __init__(self, posicion: tuple, animation: list) -> None:
    super().__init__(posicion, animation)
    self.speed_x = 3
    self.animation_death = pig_dead

class Enemy_Attack(Enemy):
  def __init__(self, posicion: tuple, list_animations: list) -> None:
    super().__init__(posicion, list_animations[0])
    self.speed_x = 2
    self.lives = 3
    self.list_animations = list_animations
    self.animation_death = self.list_animations[1]

  def update(self, player_rect, platforms_list):
    super().update(platforms_list)
    if not self.muerto:
      if self.rect.y <= player_rect.y and abs(self.rect.x - player_rect.x) <= 400:
        self.attack_player(player_rect, platforms_list)
      else:
        self.animation = self.list_animations[0]
      if self.speed_x > 0:
        self.left = False
      else:
        self.left = True

  def attack_player(self, player_rect, platforms_list):
    self.animation = self.list_animations[2]
    if self.rect.x < player_rect.x:
        self.speed_x = 3
    else:
        self.speed_x = -3

class Enemy_Boss(Enemy):
  def __init__(self, posicion: tuple, list_animations: list) -> None:
    super().__init__(posicion, list_animations[0])
    self.list_animations = list_animations
    self.lives = 10
    self.is_jumping = False
    self.jump_height = 200
    self.jump_duration = 60
    self.jump_timer = 0
    self.speed_x = 0
    self.left = True
    self.speed_animation = 25
    self.cadencia = 100
    self.spawn_timer = pygame.time.get_ticks()
    self.spawn_interval = 4000
    self.health_bar = HealthBar(100, 15, self.lives)
    self.animation_death = self.list_animations[2]

  def update(self, player_rect, piso_rect, bullets_group, enemy_list, platforms_list):
    super().update(platforms_list)
    if not self.muerto:
      if not self.is_jumping:
        self.check_collision(platforms_list)
        if self.rect.y <= player_rect.y and abs(self.rect.x - player_rect.x) <= 800:
          self.attack_player(player_rect, bullets_group)
        else:
          self.speed_x = 0
          self.animation = self.list_animations[0]
      else:
        self.jump_timer += 1
        if self.jump_timer <= self.jump_duration:
          self.mover_personaje_y()
        else:
          self.is_jumping = False
          self.jump_timer = 0
          self.animation = self.list_animations[0]
          self.rect.y = self.posicion[1]
      if self.speed_x > 0:
        self.left = False
      else:
        self.left = True

      self.player_collide_floor(piso_rect)

      if self.lives < 8 and pygame.time.get_ticks() - self.spawn_timer >= self.spawn_interval:
        self.create_random_enemy(enemy_list)
        self.spawn_timer = pygame.time.get_ticks()

  def draw(self, screen):
    super().draw(screen)
    self.health_bar.draw(screen, (self.rect.centerx, self.rect.top + 50))

  def attack_player(self, player_rect, bullets_group):
    self.animation = self.list_animations[1]
    if self.rect.x < player_rect.x:
      self.speed_x = 3
    else:
      self.speed_x = -3
    self.disparar(bullets_group)

  def mover_personaje_y(self):
    if self.jump_timer <= self.jump_duration // 2:
      self.rect.y -= self.jump_height // (self.jump_duration // 2)
    else:
      self.rect.y += self.jump_height // (self.jump_duration // 2)

  def player_collide_floor(self, piso_rect):
    if self.rect.colliderect(piso_rect) and not self.is_jumping:
      self.rect.bottom = piso_rect.top + 40
      self.is_jumping = False
      self.jump_timer = 0

  def disparar(self, bullets_group):
    super().disparar(bullets_group, bala_dead)

  def create_random_enemy(self, enemy_list):
    enemy_types = [Enemy_Attack]
    random_enemy_type = random.choice(enemy_types)
    random_enemy = random_enemy_type((800,680), cuervo)
    enemy_list.append(random_enemy)

  def check_collision(self, platforms_list):
    if self.rect.left < 0 or self.rect.right > WIDTH_PANTALLA:
      self.invert_direction()

  def invert_direction(self):
    self.speed_x *= -1

  def recibir_disparo(self):
    self.health_bar.health = self.lives
    if not self.is_jumping:
      self.is_jumping = True
      self.animation = self.list_animations[0]