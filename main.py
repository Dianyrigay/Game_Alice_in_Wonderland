import pygame
from sys import exit

from constantes import *
from animaciones import *

from Player import Player
from Enemigo import Enemy_Shooter, Enemy_Moving
from Plataforma import Plataforma
from Item import Portal

pygame.init()

# Configuración pantalla
pantalla = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png')
pygame.display.set_icon(icono)

# Cronómetro del juego
tiempo_total = 60000  # Duración total del cronómetro en milisegundos
tiempo_actual = pygame.time.get_ticks()  # Tiempo transcurrido inicialmente

# Sistema de puntuaciones
puntuacion = 100

# Sonidos
sonidos_015 = [items_win, game_over_sound,pig_dead_sound, impact, plant_dead_sound]
sonidos_005 = [ambiente_fantasy]

for sonido in sonidos_005:
  sonido.set_volume(0.05)

for sonido in sonidos_015:
  sonido.set_volume(0.15)

ambiente_fantasy.play()

def dibujar_fondo():
  fondo_imagen = pygame.transform.scale(pygame.image.load(
      "./images/fondo/area.png").convert_alpha(), (WIDTH_PANTALLA, HEIGHT_PANTALLA))
  pantalla.blit(fondo_imagen, (0, 0))

# Superficie pisxo
piso_surf = pygame.Surface((WIDTH_PANTALLA, ALTURA_PISO))
piso_rect = piso_surf.get_rect(
    topleft=(0, HEIGHT_PANTALLA - piso_surf.get_height()))

# Grupos de sprites
balas_group = pygame.sprite.Group()
burbujas_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()

# Instanciacion del personaje principal
player = Player()
# Instanciacion de enemigos
enemigo_plant = Enemy_Shooter((WIDTH_PANTALLA - 200, HEIGHT_PANTALLA - ALTURA_PISO), attack)
enemigo_pig = Enemy_Moving((WIDTH_PANTALLA/2, 250), pig_fly)
# Instanciacion de plataformas
plataforma1 = Plataforma(AREA_1, 3, 0, 300, 500, items_group, hongo_violet)
plataforma2 = Plataforma(AREA_1, 2, 0, 550, 450, items_group, hongo_yellow)
plataforma3 = Plataforma(AREA_1, 5, 0, 700, 280, items_group, taza1)
plataforma4 = Plataforma(AREA_1, 3, 0, 270, 250, items_group, key_yellow)
plataforma5 = Plataforma(AREA_1, 1, 0, 1200, 500, items_group, pocion_reduce)

lista_rectangulos = [piso_rect, plataforma1.rect, plataforma2.rect, plataforma3.rect, plataforma4.rect, plataforma5.rect]
lista_plataformas = [plataforma1, plataforma2, plataforma3, plataforma4, plataforma5]
lista_enemigos = [enemigo_plant, enemigo_pig]

running_game = True
game_over = False
game_over_image = pygame.image.load("./images/game_over.png")
game_over_image = pygame.transform.scale(game_over_image, (WIDTH_PANTALLA, HEIGHT_PANTALLA))
primera_iteracion = True
game_win = False

while running_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            exit()

    tiempo_transcurrido = pygame.time.get_ticks() - tiempo_actual
    tiempo_restante = max(0, tiempo_total - tiempo_transcurrido) // 1000

    player.eventos(burbujas_group)

    # Background
    dibujar_fondo()

    # Level 1
    if not game_over:
      if player.muerto or tiempo_restante == 0:
        game_over = True

      # -- Colisiones de sprite con groups
      colision_alice_balas = pygame.sprite.spritecollide(player, balas_group, True)
      colision_alice_items = pygame.sprite.spritecollide(player, items_group, True)
      colision_alice_enemigos = pygame.sprite.spritecollide(player, lista_enemigos, False)

      for enemigo in lista_enemigos:
        colisiona_burbujas_enemigo = pygame.sprite.spritecollide(enemigo, burbujas_group, True)
        if colisiona_burbujas_enemigo:
          if enemigo.animacion == pig_fly:
            pig_dead_sound.play()
          else:
            plant_dead_sound.play()
          puntuacion += 50
          enemigo.muerto = True
          lista_enemigos.remove(enemigo)

      if colision_alice_balas or colision_alice_enemigos:
        impact.play()
        player.animacion = angry
        player.restar_vidas()
        if colision_alice_balas:
          puntuacion -= 20
        else:
          puntuacion -= 50
          player.rect.x += -50

      if colision_alice_items:
        for item in colision_alice_items:
          if item.animacion == key_yellow:
            portal = Portal(WIDTH_PANTALLA - 100, HEIGHT_PANTALLA - ALTURA_PISO, open_portal)
            game_win = True
          if item.animacion == pocion_reduce:
            player.reducir()
        items_win.play()
        puntuacion += 10

      player.update(pantalla, lista_rectangulos)

      if game_win:
        portal.update(pantalla)
      # -- Enemigos
      enemigo_plant.update(pantalla, piso_rect, balas_group)
      enemigo_pig.update(pantalla)

      # --Plataformas
      for plataforma in lista_plataformas:
        plataforma.dibujar(pantalla)

      # --Actualización y dibujos de Groups
      # balas
      balas_group.update()
      balas_group.draw(pantalla)
      # burbuja
      burbujas_group.update()
      burbujas_group.draw(pantalla)
      # items
      items_group.update()
      items_group.draw(pantalla)

      escribir_pantalla(pantalla, 'SCORE: ', "white", str(puntuacion), (20, 20))
      escribir_pantalla(pantalla, 'VIDAS: ', "white", str(player.vidas), (1250, 20))
      escribir_pantalla(pantalla, '00:', "white", str(tiempo_restante).zfill(2), (WIDTH_PANTALLA/2, 20))
    else:
      ambiente_fantasy.stop()
      game_over_sound.play()
      pantalla.blit(game_over_image, (0,0))

    pygame.display.update()

    primera_iteracion = False
    clock.tick(FPS)

pygame.quit()
