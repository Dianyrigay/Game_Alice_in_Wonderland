from constantes import *
from animaciones import *

from Personaje import Personaje

class Player(Personaje):
  def __init__(self) -> None:
    super().__init__()
    # -- Attributos
    self.entrada_cayendo = True
    self.rect = idle[0].get_rect(topleft=(0, 0))
    self.rect_lives = live[0].get_rect(topleft=(1450, 20))
    self.velocidad_x = 0
    self.velocidad_y = 0
    # -- salto
    self.gravedad = 0.9
    self.potencia_salto = -15
    self.esta_cayendo = False
    self.can_double_jump = False
    # --animaciones
    self.contador_cambio_animacion = 30
    self.cadencia = 10
    self.lives = 5
    self.score = 0
    self.list_animations = list_alice
    # -- cambios segun niveles
    self.tiempo_invertido = 10 * FPS
    self.invertir_movimientos = False
    self.transition_dark = False
    self.dark = False
    # --cumplimiento nivel
    self.key_recogida = False
    self.enter_portal = False

  def mover_personaje_x(self):
    self.rect.x += self.velocidad_x

    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > WIDTH_PANTALLA:
        self.rect.right = WIDTH_PANTALLA

  def mover_personaje_y(self):
    self.rect.y += self.velocidad_y

    if self.rect.top == HEIGHT_PANTALLA:
      self.rect.top = HEIGHT_PANTALLA

  def calcular_gravedad(self):
    if self.velocidad_y == 0:
      self.velocidad_y = 1
    else:
      self.esta_cayendo = True
      self.velocidad_y += self.gravedad

  def update(self, screen, platforms_list, piso_rect):
    self.cuenta_pasos += 1

    if self.lives > 0:
      self.mover_personaje_x()
      self.mover_personaje_y()
      self.calcular_gravedad()
      self.player_collide_platforms(platforms_list)
      self.player_collide_floor(piso_rect)
      if self.esta_cayendo:
        self.animacion = self.list_animations[2]
    elif self.lives <= 0 and self.contador_muerte > 0:
      #TODO arreglar animacion de muerte
      self.animacion = self.list_animations[4]
      self.contador_muerte -= 1
    else:
      self.muerto = True

    if self.animacion == self.list_animations[3] or self.animacion == reducir:
       self.contador_cambio_animacion -= 1

    if self.invertir_movimientos:
      self.tiempo_invertido -= 1
      segundos = int(self.tiempo_invertido / 60)
      escribir_screen(screen, "00:0", "white", str(segundos))
      if self.tiempo_invertido <= 0:
        self.invertir_movimientos = False
        suspence_invertion.stop()
        self.tiempo_invertido = 0

    if (self.rect.x >= WIDTH_PANTALLA / 2 and self.transition_dark) or self.dark:
      self.list_animations = list_alice_dark
    else:
      self.list_animations = list_alice

    # if self.enter_portal:
    #   animar_pantalla(screen, transition_alice)

  def draw(self, screen):
    self.animar_lives(screen)
    self.animar_personaje(screen)

  # control de moivimientos del Personaje:
  def saltar(self):
    if self.izquierda:
      self.velocidad_x = -3
    else:
      self.velocidad_x = 3

    #TODO arreglar doble salto
    if not self.esta_cayendo and not self.can_double_jump:
      self.velocidad_y = self.potencia_salto
      self.can_double_jump = True
    elif self.can_double_jump:
      self.velocidad_y = self.potencia_salto
      self.can_double_jump = False

  def flotar(self):
    self.animacion = self.list_animations[2]
    self.velocidad_y = 5

  def mover_izquierda(self):
    self.animacion = self.list_animations[1]
    if not self.invertir_movimientos:
      self.izquierda = True
      self.velocidad_x = -8
    else:
      self.izquierda = False
      self.velocidad_x = 8

  def mover_derecha(self):
    self.animacion = self.list_animations[1]
    if not self.invertir_movimientos:
      self.izquierda = False
      self.velocidad_x = 8
    else:
      self.izquierda = True
      self.velocidad_x = -8

  def idle(self):
    self.animacion = self.list_animations[0]
    self.velocidad_x = 0

  # Lives player
  def restar_lives(self, screen):
    # self.animacion = self.list_animations[3]
    self.lives -= 1

  def animar_lives(self, screen):
    x = self.rect_lives.right
    for _ in range(self.lives):
      x -= self.rect_lives.width + 15
      indice_imagen = self.cuenta_pasos // self.velocidad_animacion % len(live)
      screen.blit(live[indice_imagen], (x, self.rect_lives.y))

  def disparar(self, bubbles_group):
    if (self.rect.x >= WIDTH_PANTALLA / 2 and self.transition_dark) or self.dark:
      arma = knife
    else:
      arma = bubble
    super().disparar(bubbles_group, arma)

  def reducir(self):
    x = self.rect.x
    y = self.rect.y
    self.animacion = reducir
    reescalar_imagen(list_alice, 0.35)
    #TODO reducir la burbuja tambien, ver donde debo reducirla
    # reescalar_imagen([[bubble]],0.01)
    self.rect = idle[0].get_rect(topleft=(x, y))

  def eventos(self, bubbles_group):
    keys = pygame.key.get_pressed()

    if not self.esta_cayendo or (self.esta_cayendo and self.can_double_jump):
      if self.entrada_cayendo:
        self.flotar()
        self.entrada_cayendo = False
      elif keys[pygame.K_LEFT]:
        self.mover_izquierda()
      elif keys[pygame.K_RIGHT]:
        self.mover_derecha()
      elif (keys[pygame.K_x]):
        #TODO agregar que pueda disparar mientras walk
        self.disparar(bubbles_group)
      else:
        if self.contador_cambio_animacion <= 0 and self.animacion == self.list_animations[3]:
          self.idle()
          self.contador_cambio_animacion = 30
        elif self.animacion != self.list_animations[3]:
          self.idle()

  def player_collide_platforms(self, platforms_list):
    for plataforma in platforms_list:
        if self.rect.colliderect(plataforma.rect):
            if self.velocidad_y > 0 and self.esta_cayendo:
                self.velocidad_y = 0
                self.rect.bottom = plataforma.rect.top
                self.esta_cayendo = False
            elif self.velocidad_y < 0:
                self.esta_cayendo = False
                self.rect.top = plataforma.rect.bottom
                self.velocidad_y = 0

            if not self.rect.bottom == plataforma.rect.top and not self.rect.top == plataforma.rect.bottom:
                if self.velocidad_x > 0:
                    self.rect.right = plataforma.rect.left
                    self.velocidad_x = 0
                elif self.velocidad_x < 0:
                    self.rect.left = plataforma.rect.right
                    self.velocidad_x = 0

  def player_collide_floor(self, piso_rect):
    if self.rect.colliderect(piso_rect):
      if self.velocidad_y > 0 and self.esta_cayendo:
        self.velocidad_y = 0
        self.rect.bottom = piso_rect.top
        self.esta_cayendo = False

  def reset_position(self):
    self.entrada_cayendo = True
    self.rect.topleft = (0, 0)
    self.key_recogida = False
    self.enter_portal = False
