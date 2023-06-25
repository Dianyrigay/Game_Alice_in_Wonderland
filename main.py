import pygame
from sys import exit

from constantes import *
from animaciones import *

from Personaje_Principal import Personaje_Principal
from Enemigo import EnemigoDisparador, EnemigoMovimientoRango
from Plataforma import Plataforma

pygame.init()

# Configuración pantalla
pantalla = pygame.display.set_mode((WIDTH_PANTALLA, HEIGHT_PANTALLA))
clock = pygame.time.Clock()
pygame.display.set_caption('Alice in Worderland')
icono = pygame.image.load('./images/alice/idle/rigth.png')
pygame.display.set_icon(icono)

# Sistema de puntuaciones
puntuacion = 0

# Sonidos
pygame.mixer.init()
# pygame.mixer.Sound('./sonidos/') # tipo de sonido
ambiente_fantasy = pygame.mixer.Sound('./sonidos/fantasy-ambient.wav')
items_win = pygame.mixer.Sound('./sonidos/items-win.wav')
pig_dead_sound = pygame.mixer.Sound('./sonidos/pig-dead.ogg')
game_over_sound = pygame.mixer.Sound('./sonidos/game_over.wav')

sonidos = [items_win, pig_dead_sound, game_over_sound]

ambiente_fantasy.set_volume(0.05)
ambiente_fantasy.play()
for sonido in sonidos:
  sonido.set_volume(0.15)


fondo_imagenes = []
for i in range(3):
  fondo_imagen = pygame.image.load(f'./images/fondo/area-0{i}.png').convert_alpha()
  fondo_imagen = pygame.transform.scale(fondo_imagen, (WIDTH_PANTALLA, HEIGHT_PANTALLA))
  fondo_imagenes.append(fondo_imagen)

def dibujar_fondo():
  for x in range(3):
    for i in fondo_imagenes:
      pantalla.blit(i, ((x * WIDTH_PANTALLA), 0))

# Superficie piso
piso_surf = pygame.Surface((WIDTH_PANTALLA, ALTURA_PISO))
piso_rect = piso_surf.get_rect(
    topleft=(0, HEIGHT_PANTALLA - piso_surf.get_height()))

# Grupos de sprites
balas_group = pygame.sprite.Group()
burbujas_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()

# Instanciacion del personaje principal
personaje_alice = Personaje_Principal()
# Instanciacion de enemigos
enemigo_plant = EnemigoDisparador((WIDTH_PANTALLA - 200, HEIGHT_PANTALLA - ALTURA_PISO), attack_izq)
enemigo_pig = EnemigoMovimientoRango((WIDTH_PANTALLA/2, 250), pig_fly)
# Instanciacion de plataformas
plataforma1 = Plataforma(AREA_1, 3, 0, (300, 500), items_group)
plataforma2 = Plataforma(AREA_1, 2, 0, (550, 450), items_group)
plataforma3 = Plataforma(AREA_1, 5, 0, (700, 280), items_group)

lista_plataformas = [piso_rect, plataforma1.rect, plataforma2.rect, plataforma3.rect]
lista_enemigos = [enemigo_plant, enemigo_pig]

running_game = True
game_over = False
game_over_image = pygame.image.load("./images/game_over.png")
game_over_image = pygame.transform.scale(game_over_image, (WIDTH_PANTALLA, HEIGHT_PANTALLA))
primera_iteracion = True
timer = 60

while running_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            exit()

    # delta_tiempo = clock.tick(FPS) / 1000
    timer -= 1

    keys = pygame.key.get_pressed()

    if not personaje_alice.esta_cayendo:
      # -- código de control de movimientos
      if primera_iteracion:
        personaje_alice.flotar()
      elif keys[pygame.K_LEFT] and keys[pygame.K_SPACE]:
        # TODO debo arreglar que sigue caminando sola despues
        personaje_alice.saltar()
      elif keys[pygame.K_LEFT]:
        personaje_alice.mover_izquierda()
      elif keys[pygame.K_RIGHT] and keys[pygame.K_SPACE]:
        personaje_alice.saltar()
      elif keys[pygame.K_RIGHT]:
        personaje_alice.mover_derecha()
      elif keys[pygame.K_SPACE]:
        personaje_alice.saltar()
      elif (keys[pygame.K_x] or (keys[pygame.K_RIGHT] and keys[pygame.K_x]) or (keys[pygame.K_RIGHT] and keys[pygame.K_x])) and timer <= 0:
        personaje_alice.disparar(burbujas_group)
        timer = 60
      else:
         personaje_alice.quieto()

    # Background
    dibujar_fondo()

    # Level 1
    if not game_over:
      personaje_alice.update(pantalla, lista_plataformas, lista_enemigos)
      if personaje_alice.muerto:
        game_over = True

      # Colisiones de un sprite con groups
      colision_balas_alice = pygame.sprite.spritecollide(personaje_alice, balas_group, True)
      colision_items = pygame.sprite.spritecollide(personaje_alice, items_group, True)

      for enemigo in lista_enemigos:
        colisiona_burbujas_enemigo = pygame.sprite.spritecollide(enemigo, burbujas_group, True)
        if colisiona_burbujas_enemigo:
          if enemigo.animacion == pig_fly:
            pig_dead_sound.play()
          puntuacion += 50
          enemigo.muerto = True
          lista_enemigos.remove(enemigo)

      if colision_balas_alice:
          personaje_alice.restar_vidas()

      if colision_items:
        items_win.play()
        puntuacion += 10

      enemigo_plant.update(pantalla, piso_rect, personaje_alice)
      enemigo_pig.update(pantalla, piso_rect, personaje_alice)

      if enemigo_plant.cuentaPasos % TIEMPO_ENTRE_DISPAROS == 0:
        enemigo_plant.disparar(balas_group)

      # SUPERFICIES
      plataforma1.dibujar(pantalla)
      plataforma2.dibujar(pantalla)
      plataforma3.dibujar(pantalla)

      # actualización y dibujos de Groups
      # balas
      balas_group.update()
      balas_group.draw(pantalla)
      # burbuja
      burbujas_group.update()
      burbujas_group.draw(pantalla)
      # items
      items_group.update()
      items_group.draw(pantalla)
    else:
      ambiente_fantasy.stop()
      game_over_sound.play()
      pantalla.blit(game_over_image, (0,0))

    escribir_pantalla(pantalla, 'SCORE: ', "white", str(puntuacion).zfill(5), (20, 20))
    escribir_pantalla(pantalla, 'VIDAS: ', "white", str(personaje_alice.vidas), (1250, 20))
    pygame.display.update()

    primera_iteracion = False
    clock.tick(FPS)

pygame.quit()
