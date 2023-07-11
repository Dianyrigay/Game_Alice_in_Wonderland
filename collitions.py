import pygame

from animations import *
from constantes import *

from enemigo import Enemy_Moving, Enemy_Attack, Enemy_Boss
from player import Player
from item import Portal

class Collition:
  def __init__(self, player: Player, enemy_list: list, platforms_list: list, bullets_group, bubbles_group, items_group, sonidos_caracters, traps_group, portal: Portal = None) -> None:
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
      self.player_collide_portal(screen)

  def player_collide_bullet(self, screen):
    collide = pygame.sprite.spritecollide(self.player, self.bullets_group, True)

    if collide:
      impact.play()
      self.player.animation = self.player.list_animations[3]
      self.player.restar_lives(screen)
      self.player.rect.x += -10

  def player_collide_enemy(self):
    collide = pygame.sprite.spritecollide(self.player, self.enemy_list, False)

    if collide:
      impact.play()
      self.player.animation = self.player.list_animations[3]

  def enemy_collide_bubbles(self):
    if self.enemy_list != None:
      for enemigo in self.enemy_list:
        colisiona_burbujas_enemigo = pygame.sprite.spritecollide(enemigo, self.bubbles_group, True)
        if colisiona_burbujas_enemigo:
          if type(enemigo) == Enemy_Moving:
            pig_dead_sound.play()
            enemigo.muerto = True
          elif type(enemigo) == Enemy_Attack or type(enemigo) == Enemy_Boss:
            impact2.play()
            enemigo.lives -= 1
            enemigo.animation = enemigo.list_animations[1]
            if enemigo.lives == 0:
              if type(enemigo) == Enemy_Boss:
                scream.play()
              enemigo.animation = enemigo.list_animations[1]
              enemigo.muerto = True
            if type(enemigo) == Enemy_Boss:
              enemigo.recibir_disparo()
          else:
            plant_dead_sound.play()
            enemigo.muerto = True
          self.player.score += 100
        if enemigo.contador_muerte == 0:
          self.enemy_list.remove(enemigo)

  def player_pick_up_items(self):
    collide = pygame.sprite.spritecollide(self.player, self.items_group, True)

    if collide:
      for item in collide:
        if item.animation == key_yellow or item.animation == key_red:
          self.player.key_recogida = True
        if item.animation == pocion_reduce:
          self.player.reducir()
        if item.animation == tarta:
          self.player.agrandar()
        if item.animation == live_item:
          self.player.lives += 1
          break
      items_win.play()
      self.player.score += 100

  def player_collide_traps(self):
    collide = pygame.sprite.spritecollide(self.player, self.traps_group, True)

    if collide:
      for trap in collide:
        trap.create_random_enemy(self.enemy_list)
      self.player.invertir_movimientos = True
      suspence_invertion.play()
      self.player.score -= 50

  def player_collide_portal(self, screen):
    if self.player.rect.colliderect(self.portal.rect):
      self.player.rect.right = self.portal.rect.left + 5
      if self.player.rect.height > self.portal.rect.height:
        write_screen(screen, "DRINK ME", "white", "", (1200, 500))
      else:
        self.player.enter_portal = True


