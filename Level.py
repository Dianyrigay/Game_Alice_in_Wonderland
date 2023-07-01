import pygame
import json

from utilidades import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter
from Item import Portal
from Platform import Platform
from collitions import Collition

class Level():
  def __init__(self, enemy_list: list, bullets_group, bubbles_group, items_group, traps_group, piso_rect, player: Player, background, level_data) -> None:
    # --List
    self.platforms_list = []
    self.enemy_list = enemy_list
    # --Group
    self.items_group = items_group
    self.traps_group = traps_group
    self.bullets_group = bullets_group
    self.bubbles_group = bubbles_group
    #-------
    self.piso_rect = piso_rect
    self.background = background
    self.player = player
    # --Collitions
    self.collition = None
    # --Cronometro
    self.time_game = 60000
    self.time_actual = pygame.time.get_ticks()
    self.time_transcurrido = 0
    self.time_restante = 60000
    # --Data level json
    self.load_level_data(level_data)
    self.level = "level_1"

  # Get data JSON and instance of object
  def load_level_data(self, level_data):
    with open(level_data) as file:
      data = json.load(file)
      data = data["level_1"]

    self.background = pygame.transform.scale(pygame.image.load(data['background']).convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
    # self.enemy_list = []
    # self.items_group = pygame.sprite.Group()
    # self.traps_group = pygame.sprite.Group()

    for platform in data['platforms']:
      path = data["path_platforms"]
      cantidad = platform['cantidad']
      separacion = platform['separacion']
      x = platform['x']
      y = platform['y']
      animations = platform['animations']
      #TODO me falta agregar el mirror

      platform = Platform(path, cantidad, separacion, x,
                            y, self.items_group, animations)
      self.platforms_list.append(platform)

    # for enemy_data in data['enemy_shooter']:
    #     x = enemy_data['x']
    #     y = enemy_data['y']

    #     enemy = Enemy_Shooter((x, y), attack)
    #     self.enemy_list.append(enemy)

    # Resto de la carga de datos y creación de objetos...
    collitions = Collition(self.player, self.enemy_list, self.platforms_list,
                          self.bullets_group, self.bubbles_group, self.items_group, sonidos_caracters, self.traps_group)
    self.collition = collitions

  # Update all in this level
  def update(self, screen):
    self.player.update(screen, self.platforms_list, self.piso_rect)

    if self.player.key_recogida:
      # TODO add sound
      portal = Portal(WIDTH_PANTALLA - 100, HEIGHT_PANTALLA -
                      ALTURA_PISO, open_portal)
      portal.update(screen)

    self.bullets_group.update()
    self.bubbles_group.update()
    self.items_group.update()

    for enemigo in self.enemy_list:
      if type(enemigo) == Enemy_Shooter:
        enemigo.update(self.piso_rect, self.bullets_group)
      else:
        enemigo.update()

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

    escribir_screen(screen, 'SCORE: ', "white", str(self.player.score), (20, 20))
    escribir_screen(screen, '00:', "white", str(self.time_restante).zfill(2), (WIDTH_PANTALLA/2, 20))

  def update_time(self):
    self.time_transcurrido = pygame.time.get_ticks() - self.time_actual
    self.time_restante = max(0, self.time_game - self.time_transcurrido) // 1000


