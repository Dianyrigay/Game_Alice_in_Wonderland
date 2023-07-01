import pygame
import json

from utilidades import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving
from Item import Portal
from Platform import Platform
from collitions import Collition

class Level():
  def __init__(self, bullets_group, bubbles_group, items_group, traps_group, player: Player, level_data_json) -> None:
    # --List
    self.platforms_list = []
    self.enemy_list = []
    # --Group
    self.items_group = items_group
    self.traps_group = traps_group
    self.bullets_group = bullets_group
    self.bubbles_group = bubbles_group
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
    self.level = "level_1"
    self.load_level_data(level_data_json)
    self.level_data = None

  # Get data JSON and instance of object
  def load_level_data(self, level_data_json):
    with open(level_data_json) as file:
      data = json.load(file)
      self.level_data = data[self.level]

    print(self.portal)
    self.background = pygame.transform.scale(pygame.image.load(self.level_data['background']).convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))

    for platform in self.level_data['platforms']:
      path = self.level_data["path_platforms"]
      cantidad = platform['cantidad']
      separacion = platform['separacion']
      x = platform['x']
      y = platform['y']
      if platform["animations"] == "mirror":
        animations = mirror
        group = self.traps_group
      else:
        animations = platform['animations']
        group = self.items_group

      platform = Platform(path, cantidad, separacion, x, y, group, animations)
      self.platforms_list.append(platform)

    for enemy in self.level_data['enemy_shooter']:
        x = enemy['x']
        y = enemy['y']

        enemy = Enemy_Shooter((x, y), attack)
        self.enemy_list.append(enemy)

    for enemy in self.level_data['enemy_moving']:
      x = enemy['x']
      y = enemy['y']

      enemy = Enemy_Moving((x, y), pig_fly)
      self.enemy_list.append(enemy)

    # colisiones
    collitions = Collition(self.player, self.enemy_list, self.platforms_list,
                          self.bullets_group, self.bubbles_group, self.items_group, sonidos_caracters, self.traps_group, self.portal)
    self.collition = collitions

    # Superficie piso
    piso_surf = pygame.Surface((WIDTH_PANTALLA, ALTURA_PISO))
    self.piso_rect = piso_surf.get_rect(topleft=(0, HEIGHT_PANTALLA - ALTURA_PISO))

    # Portal
    x_portal = self.level_data["exit_portal"]["x"]
    y_portal = self.level_data["exit_portal"]["y"]
    animation_portal = self.level_data["exit_portal"]["animation"]
    animation_portal = obtener_surface_de_spriteSheet(animation_portal, 8, 1, 1)

    self.portal = Portal(x_portal, y_portal, animation_portal)

  # Update all in this level
  def update(self, screen):
    self.player.update(screen, self.platforms_list, self.piso_rect)


    self.bullets_group.update()
    self.bubbles_group.update()
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

    self.collition.update(screen)

    self.update_time()

  # Drawing all in this level
  def draw(self, screen):
    screen.fill("black")
    screen.blit(self.background, (0,0))

    for plataforma in self.platforms_list:
      plataforma.draw(screen)

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

    escribir_screen(screen, 'SCORE: ', "white", str(self.player.score), (20, 20))
    escribir_screen(screen, '00:', "white", str(self.time_restante).zfill(2), (WIDTH_PANTALLA/2, 20))

  def update_time(self):
    self.time_transcurrido = pygame.time.get_ticks() - self.time_actual
    self.time_restante = max(0, self.time_game - self.time_transcurrido) // 1000


