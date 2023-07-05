import pygame

from animaciones import *
from constantes import *

from Enemigo import Enemy_Moving
from Player import Player

class Collition:
  def __init__(self, player: Player, enemy_list, platforms_list, bullets_group, bubbles_group, items_group, sonidos_caracters, traps_group, portal = None) -> None:
    self.player = player
    self.enemy_list = enemy_list
    self.platforms_list = platforms_list
    self.bullets_group = bullets_group
    self.bubbles_group = bubbles_group
    self.items_group = items_group
    self.traps_group = traps_group
    self.portal = portal
    self.sonidos_caracters = sonidos_caracters

  def update(self, screen):
    self.player_collide_bullet(screen)
    self.player_collide_enemy()
    self.player_collide_traps()
    self.player_pick_up_items()
    self.enemy_collide_bubbles()
    if self.portal:
      self.player_collide_portal()

  def player_collide_bullet(self, screen):
    collide = pygame.sprite.spritecollide(self.player, self.bullets_group, True)

    if collide:
      impact.play()
      self.player.animacion = angry
      self.player.restar_lives(screen)
      self.player.score -= 20
      self.player.rect.x += -10

  def player_collide_enemy(self):
    collide = pygame.sprite.spritecollide(self.player, self.enemy_list, False)

    if collide:
      impact.play()
      self.player.score -= 50
      self.player.animacion = angry
      self.player.rect.x += -10

  def enemy_collide_bubbles(self):
    if self.enemy_list != None:
      for enemigo in self.enemy_list:
        colisiona_burbujas_enemigo = pygame.sprite.spritecollide(enemigo, self.bubbles_group, True)
        if colisiona_burbujas_enemigo:
          if type(enemigo) == Enemy_Moving:
            pig_dead_sound.play()
          else:
            plant_dead_sound.play()
          self.player.score += 100
          enemigo.muerto = True
        if enemigo.contador_muerte == 0:
          self.enemy_list.remove(enemigo)

  def player_pick_up_items(self):
    collide = pygame.sprite.spritecollide(self.player, self.items_group, True)

    if collide:
      for item in collide:
        if item.animacion == key_yellow:
          self.player.key_recogida = True
        if item.animacion == pocion_reduce:
          self.player.reducir()
      items_win.play()
      self.player.score += 50

  def player_collide_traps(self):
    collide = pygame.sprite.spritecollide(self.player, self.traps_group, True)

    if collide:
      self.player.invertir_movimientos = True
      suspence_invertion.play()
      self.player.score -= 50

  def player_collide_portal(self):
    if self.player.rect.colliderect(self.portal.rect):
      self.player.enter_portal = True


