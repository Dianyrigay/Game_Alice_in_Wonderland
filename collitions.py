import pygame

from animaciones import *
from constantes import *

from Enemigo import Enemy_Moving, Enemy_Shooter
from Player import Player

class Collition:
  def __init__(self, player: Player, enemy_list, platforms_list, bullets_group, bubbles_group, items_group, sonidos_caracters) -> None:
    self.player = player
    self.enemy_list = enemy_list
    self.platforms_list = platforms_list
    self.bullets_group = bullets_group
    self.bubbles_group = bubbles_group
    self.items_group = items_group
    self.sonidos_caracters = sonidos_caracters

  def update(self, screen):
    self.player_collide_bullet()
    self.player_collide_enemy()
    self.enemy_collide_bubbles()
    self.player_pick_up_items(screen)

  def player_collide_bullet(self):
    collide = pygame.sprite.spritecollide(self.player, self.bullets_group, True)

    if collide:
      impact.play()
      self.player.animacion = angry
      self.player.restar_vidas()
      self.player.score -= 20
      self.player.rect.x += -10

  def player_collide_enemy(self):
    #TODO refactorizar ya que hace basicamente lo mismo con la de bullet
    collide = pygame.sprite.spritecollide(self.player, self.enemy_list, False)

    if collide:
      impact.play()
      self.player.animacion = angry
      self.player.restar_vidas()
      self.player.score -= 50
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
          self.player.score += 50
          enemigo.muerto = True
          self.enemy_list.remove(enemigo)

  def player_pick_up_items(self, screen):
    collide = pygame.sprite.spritecollide(self.player, self.items_group, True)

    if collide:
      for item in collide:
        if item.animacion == key_yellow:
          self.player.key_recogida = True
        if item.animacion == pocion_reduce:
          self.player.reducir()
      items_win.play()
      self.player.score += 10



