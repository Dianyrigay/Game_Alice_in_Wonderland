import pygame
import json

from utilidades import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving
from Item import Portal
from Platform import Platform, MovingPlatform
from collitions import Collition

class Level():
  def __init__(self, player: Player, level) -> None:
    # --List
    self.platforms_list = []
    self.enemy_list = []
    # --Group
    self.items_group = pygame.sprite.Group()
    self.traps_group = pygame.sprite.Group()
    self.bullets_group = pygame.sprite.Group()
    self.bubbles_group = pygame.sprite.Group()
    #-------
    self.piso_rect = None
    self.background = None
    self.player = player
    # --Collitions
    self.collition = None
    # --Cronometro
    self.time_game = 60000
    self.time_actual = pygame.time.get_ticks()
    self.time_transcurrido = 0
    self.time_restante = 60000
    # --Exit portal
    self.portal = None
    # --Data level json
    self.level = level
    self.load_level_data(f"./Levels/{level}.json")
    self.level_data = None
    self.next_level = None

  # Get data JSON and instance of object
  def load_level_data(self, level_data_json):
    with open(level_data_json) as file:
      data = json.load(file)
      self.level_data = data[self.level]

    self.set_background_music()
    self.load_background()
    self.load_platforms()
    self.load_moving_platforms()
    self.load_enemy_shooters()
    self.load_enemy_movings()
    self.create_collisions()
    self.create_floor_surface()
    self.create_portal()

  def set_background_music(self):
    if self.level == "level_1":
      ambient_suspence.play()
    elif self.level == "level_2":
      ambient_suspence.stop()
      ambient_fantasy.play()
    elif self.level == "level_3":
      ambient_fantasy.stop()
      ambient_horror.play()

  def load_background(self):
    self.background = pygame.transform.scale(pygame.image.load(
          self.level_data['background']).convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))

  def load_platforms(self):
    for platform in self.level_data['platforms']:
      path = self.level_data["path_platforms"]
      cantidad = platform['cantidad']
      separacion = platform['separacion']
      x = platform['x']
      y = platform['y']
      animations = None

      if "animations" in platform:
        if platform["animations"] == "mirror":
          animations = mirror
          group = self.traps_group
        else:
          animations = platform['animations']
          group = self.items_group
      else:
        group = self.items_group

      platform = Platform(path, cantidad, separacion,
                              x, y, group, animations)
      self.platforms_list.append(platform)

  def load_moving_platforms(self):
      if 'moving_platforms' in self.level_data:
          for platform in self.level_data["moving_platforms"]:
              path = self.level_data["path_platforms"]
              cantidad = platform['cantidad']
              separacion = platform['separacion']
              x = platform['x']
              y = platform['y']
              limit_left = platform['limit_left']
              limit_right = platform['limit_right']
              change_x = platform['change_x']
              change_y = platform['change_y']
              limit_top = platform['limit_top']
              limit_bottom = platform['limit_bottom']
              group = self.items_group

              platform = MovingPlatform(path, cantidad, separacion, x,
                                        y, group, limit_left, limit_right, change_x, change_y, limit_top, limit_bottom, self.player)
              self.platforms_list.append(platform)

  def load_enemy_shooters(self):
    if 'enemy_shooter' in self.level_data:
      for enemy in self.level_data['enemy_shooter']:
        x = enemy['x']
        y = enemy['y']
        animation_name = enemy['animation']
        animation = dict_animations[animation_name]

        enemy = Enemy_Shooter((x, y), animation)
        self.enemy_list.append(enemy)

  def load_enemy_movings(self):
    if 'enemy_moving' in self.level_data:
      for enemy in self.level_data['enemy_moving']:
        x = enemy['x']
        y = enemy['y']
        animation_name = enemy['animation']
        animation = dict_animations[animation_name]

        enemy = Enemy_Moving((x, y), animation)
        self.enemy_list.append(enemy)

  def create_collisions(self):
    collitions = Collition(self.player, self.enemy_list, self.platforms_list,
                             self.bullets_group, self.bubbles_group, self.items_group, sonidos_caracters, self.traps_group, self.portal)
    self.collition = collitions

  def create_floor_surface(self):
    piso_surf = pygame.Surface((WIDTH_PANTALLA, ALTURA_PISO))
    self.piso_rect = piso_surf.get_rect(topleft=(0, HEIGHT_PANTALLA - ALTURA_PISO))

  def create_portal(self):
    x_portal = self.level_data["exit_portal"]["x"]
    y_portal = self.level_data["exit_portal"]["y"]
    animation_portal = self.level_data["exit_portal"]["animation"]
    animation_portal = obtener_surface_de_spriteSheet(animation_portal, 8, 1, 1)

    self.portal = Portal(x_portal, y_portal, animation_portal)

  # Update all in this level
  def update(self, screen):
    self.player.update(screen, self.platforms_list, self.piso_rect)

    self.bullets_group.update(screen)
    self.bubbles_group.update(screen)
    self.items_group.update()

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.update(self.piso_rect, self.bullets_group)
      else:
        enemigo.update()

    if self.player.key_recogida and self.portal:
      portal_magic.play()
      self.portal.update()
      self.collition.portal = self.portal

    for platform in self.platforms_list:
        platform.update()

    self.collition.update(screen)
    if self.player.enter_portal and self.level == "level_1":
      portal_magic.stop()
      self.next_level = "level_2"
      self.player.enter_portal = False
    elif self.player.enter_portal and self.level == "level_2":
      portal_magic.stop()
      self.next_level = "level_3"
      self.player.enter_portal = False

    self.update_time()

  # Drawing all in this level
  def draw(self, screen):
    screen.fill("black")
    screen.blit(self.background, (0,0))

    for platform in self.platforms_list:
      platform.draw(screen)

    self.bullets_group.draw(screen)
    self.bubbles_group.draw(screen)
    self.items_group.draw(screen)

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.draw(screen)
      else:
        enemigo.draw(screen)

    self.player.draw(screen)

    if self.player.key_recogida and self.portal:
      self.portal.draw(screen)
      portal_magic.stop()

    escribir_screen(screen, 'SCORE: ', "white", str(self.player.score), (20, 20))
    escribir_screen(screen, '00:', "white", str(self.time_restante).zfill(2), (650, 20))

  def update_time(self):
    self.time_transcurrido = pygame.time.get_ticks() - self.time_actual
    self.time_restante = max(0, self.time_game - self.time_transcurrido) // 1000


