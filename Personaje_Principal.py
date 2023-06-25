from constantes import *
from animaciones import *
from Personaje import Personaje
from Bala import Bala

class Personaje_Principal(Personaje):
  def __init__(self) -> None:
    super().__init__()
    # -- Attributos
    self.rect = quieto_der[0].get_rect(topleft=(0, 0))
    self.velocidad_x = 0
    self.velocidad_y = 0
    self.gravedad = 0.5
    self.potencia_salto = -13
    self.limite_velocidad_caida = 15
    self.esta_cayendo = False
    self.vidas = 3
    self.cadencia = TIEMPO_ENTRE_DISPAROS
    self.ultimo_disparo = pygame.time.get_ticks()
    self.contador_muerte = 30

  def mover_personaje_x(self):
    self.rect.x += self.velocidad_x

  def mover_personaje_y(self):
    self.rect.y += self.velocidad_y

  def calcular_gravedad(self):
    if self.velocidad_y == 0:
      self.velocidad_y = 1
    else:
      self.esta_cayendo = True
      self.velocidad_y += self.gravedad

    # Verifico si esta en el suelo
    if self.rect.bottom == HEIGHT_PANTALLA - ALTURA_PISO and self.velocidad_y >= 0:
      self.velocidad_y = 0

  def update(self, pantalla, lista_plataformas, lista_enemigos):
    self.cuentaPasos += 1

    if self.vidas > 0:
      self.mover_personaje_x()
      self.mover_personaje_y()
      self.calcular_gravedad()
      self.verificar_colisiones_plataformas(lista_plataformas)
      if self.esta_cayendo:
        self.animacion = floating
    elif self.vidas <= 0 and self.contador_muerte > 0:
      self.contador_muerte -= 1
      self.animacion = dead
    else:
      self.muerto = True


    self.animar_personaje(pantalla)

  # control de moivimientos del Personaje:
  def saltar(self):
    if self.izquierda:
      self.velocidad_x = -2
    else:
      self.velocidad_x = 2
    self.animacion = floating
    self.velocidad_y = self.potencia_salto

  def flotar(self):
    self.animacion = floating
    self.velocidad_y = 1

  def mover_izquierda(self):
    self.animacion = camina_der
    self.izquierda = True
    self.velocidad_x = -8

  def mover_derecha(self):
    self.animacion = camina_der
    self.izquierda = False
    self.velocidad_x = 8

  def quieto(self):
    self.animacion = quieto_der
    self.velocidad_x = 0

  def restar_vidas(self):
    #TODO arreglar porque no se esta reproduciendo
    self.animacion = angry
    self.vidas -= 1

  def disparar(self, burbujas_group):
    disparo_ahora = pygame.time.get_ticks()
    if disparo_ahora - self.ultimo_disparo > self.cadencia:
      y = self.rect.centery
      if self.izquierda:
        x = self.rect.left
        direccion = -1
      else:
        x = self.rect.right
        direccion = 1
      # Instanciacion de balas_group
      burbuja = Bala(x, y, direccion, burbuja_bala)
      burbujas_group.add(burbuja)
      self.ultimo_disparo = disparo_ahora

  def verificar_colisiones_plataformas(self, lista_plataformas):
    for plataforma in lista_plataformas:
        if self.rect.colliderect(plataforma):
            self.esta_cayendo = False
            if self.velocidad_y > 0:
                self.velocidad_y = 0
                self.rect.bottom = plataforma.top
            elif self.velocidad_y < 0:
                self.rect.top = plataforma.bottom
                self.velocidad_y = 0

            if not self.rect.bottom == plataforma.top and not self.rect.top == plataforma.bottom:
                if self.velocidad_x > 0:
                    self.rect.right = plataforma.left
                    self.velocidad_x = 0
                elif self.velocidad_x < 0:
                    self.rect.left = plataforma.right
                    self.velocidad_x = 0
