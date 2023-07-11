from constantes import *
from animations import *

from character import Character

class Player(Character):
  """
  Clase que representa al jugador en el juego Alicia in Wonderland.

  Atributos:
  - entrada_cayendo (bool): Indica si el jugador está en estado de caída al inicio.
  - rect (pygame.Rect): Rectángulo de colisión del jugador.
  - rect_lives (pygame.Rect): Rectángulo de visualización de las vidas del jugador.
  - speed_x (int): Velocidad horizontal del jugador.
  - speed_y (int): Velocidad vertical del jugador.
  - gravedad (float): Valor de la gravedad aplicada al jugador.
  - potencia_salto (int): Potencia del salto del jugador.
  - esta_cayendo (bool): Indica si el jugador está en estado de caída.
  - can_double_jump (bool): Indica si el jugador puede realizar un doble salto.
  - contador_cambio_animation (int): Contador para el cambio de animaciones del jugador.
  - cadencia (int): Cadencia para poder disparar.
  - lives (int): Vidas restantes del jugador.
  - score (int): Puntuación del jugador.
  - list_animations (list): Lista de animaciones del jugador.
  - immune_time (int): Tiempo de inmunidad después de una colisión con un enemigo.
  - last_collision_time (int): Tiempo de la última colisión con un enemigo.
  - tiempo_invertido (int): Tiempo restante de inversión de movimientos.
  - invertir_movimientos (bool): Indica si los movimientos del jugador están invertidos.
  - transition_dark (bool): Indica si se está produciendo una transición a la versión oscura del jugador.
  - dark (bool): Indica si el jugador está en su versión oscura.
  - key_recogida (bool): Indica si el jugador ha recogido la llave.
  - enter_portal (bool): Indica si el jugador ha entrado en el portal.
  - boss_death (bool): Indica si el jefe final ha sido derrotado.
  """
  def __init__(self) -> None:
    """
    Inicializa una instancia de la clase Player.
    """
    super().__init__()
    # -- Attributos
    self.entrada_cayendo = True
    self.rect = idle[0].get_rect(topleft=(0, 0))
    self.rect_lives = live[0].get_rect(topleft=(1450, 20))
    self.speed_x = 0
    self.speed_y = 0
    # -- salto
    self.gravedad = 0.9
    self.potencia_salto = -14
    self.esta_cayendo = False
    self.can_double_jump = False
    # --animationes
    self.contador_cambio_animation = 30
    self.cadencia = 10
    self.lives = 5
    self.score = 0
    self.list_animations = list_alice
    self.immune_time = 5000
    self.last_collision_time = 0
    # -- cambios segun niveles
    self.tiempo_invertido = 10 * FPS
    self.invertir_movimientos = False
    self.transition_dark = False
    self.dark = False
    # --cumplimiento nivel
    self.key_recogida = False
    self.enter_portal = False
    self.boss_death = False

  def mover_personaje_x(self):
    """
    Actualiza la posición horizontal del personaje en función de su velocidad.
    """
    self.rect.x += self.speed_x

    if self.rect.left < 0:
        self.rect.left = 0
    elif self.rect.right > WIDTH_PANTALLA:
        self.rect.right = WIDTH_PANTALLA

  def mover_personaje_y(self):
    """
    Actualiza la posición vertical del personaje en función de su velocidad.
    """
    self.rect.y += self.speed_y

    if self.rect.top == HEIGHT_PANTALLA:
      self.rect.top = HEIGHT_PANTALLA

  def calcular_gravedad(self):
    """
    Calcula la gravedad que afecta al personaje y actualiza su velocidad vertical.
    """
    if self.speed_y == 0:
      self.speed_y = 1
    else:
      self.esta_cayendo = True
      self.speed_y += self.gravedad

  def update(self, screen, platforms_list, piso_rect):
    """
    Actualiza el estado del jugador en función de la interacción con el entorno del juego.

    Args:
    - screen (pygame.Surface): Superficie de la pantalla del juego.
    - platforms_list (list): Lista de plataformas en el nivel.
    - piso_rect (pygame.Rect): Rectángulo de colisión del suelo.

    """
    self.cuenta_pasos += 1

    if self.lives > 0:
      self.mover_personaje_x()
      self.mover_personaje_y()
      self.calcular_gravedad()
      self.player_collide_platforms(platforms_list)
      self.player_collide_floor(piso_rect)
      if self.esta_cayendo:
        self.animation = self.list_animations[2]
    elif self.lives <= 0 and self.contador_muerte > 0:
      self.animation = self.list_animations[4]
      self.contador_muerte -= 1
    else:
      self.muerto = True

    if self.animation == self.list_animations[3]:
       self.contador_cambio_animation -= 1

    if self.invertir_movimientos:
      self.tiempo_invertido -= 1
      segundos = int(self.tiempo_invertido / 60)
      write_screen(screen, "00:0", "white", str(segundos))
      if self.tiempo_invertido <= 0:
        self.invertir_movimientos = False
        suspence_invertion.stop()
        self.tiempo_invertido = 0

    if (self.rect.x >= WIDTH_PANTALLA / 2 and self.transition_dark) or self.dark:
      self.list_animations = list_alice_dark
    else:
      self.list_animations = list_alice

  def draw(self, screen):
    """
    Dibuja el jugador en la pantalla.

    Args:
    - screen (pygame.Surface): Superficie de la pantalla del juego.
    """
    self.animar_lives(screen)
    self.animar_personaje(screen)

  # control de moivimientos del Personaje:
  def saltar(self):
    """
    Realiza la acción de salto del jugador.
    """
    if self.left:
      self.speed_x = -3
    else:
      self.speed_x = 3

    if not self.esta_cayendo and not self.can_double_jump:
      self.speed_y = self.potencia_salto
      self.can_double_jump = True
    elif self.can_double_jump:
      self.speed_y = self.potencia_salto
      self.can_double_jump = False

  def flotar(self):
    """
    Realiza la acción de flotar del jugador.
    """
    self.animation = self.list_animations[2]
    self.speed_y = 5

  def mover_left(self):
    """
    Realiza el movimiento hacia la izquierda del jugador.
    """
    self.animation = self.list_animations[1]
    if not self.invertir_movimientos:
      self.left = True
      self.speed_x = -8
    else:
      self.left = False
      self.speed_x = 8

  def mover_derecha(self):
    """
    Realiza el movimiento hacia la derecha del jugador.
    """
    self.animation = self.list_animations[1]
    if not self.invertir_movimientos:
      self.left = False
      self.speed_x = 8
    else:
      self.left = True
      self.speed_x = -8

  def idle(self):
    """
    Realiza la acción de reposo del jugador.
    """
    self.animation = self.list_animations[0]
    self.speed_x = 0

  # Lives player
  def restar_lives(self):
    """
    Resta una vida al jugador.
    """
    self.animation = self.list_animations[3]
    self.lives -= 1

  def animar_lives(self, screen):
    """
    Muestra las vidas restantes del jugador en la pantalla.

    Args:
    - screen (pygame.Surface): Superficie de la pantalla del juego.
    """
    x = self.rect_lives.right
    for _ in range(self.lives):
      x -= self.rect_lives.width + 15
      indice_imagen = self.cuenta_pasos // self.speed_animation % len(live)
      screen.blit(live[indice_imagen], (x, self.rect_lives.y))

  def disparar(self, bubbles_group):
    """
    Realiza la acción de disparar proyectiles del jugador.

    Args:
    - bubbles_group (pygame.sprite.Group): Grupo de burbujas del juego.
    """
    if (self.rect.x >= WIDTH_PANTALLA / 2 and self.transition_dark) or self.dark:
      arma = knife
    else:
      arma = bubble
    super().disparar(bubbles_group, arma)

  def reducir(self):
    """
    Reduce el tamaño del jugador.
    """
    x = self.rect.x
    y = self.rect.y
    self.animation = reducir
    rescale_image(list_alice, 0.5)
    rescale_image(list_alice_dark, 0.5)
    self.rect = idle[0].get_rect(topleft=(x, y))

  def agrandar(self):
    """
    Aumenta el tamaño del jugador.
    """
    x = self.rect.x
    y = self.rect.y
    self.animation = reducir
    rescale_image(list_alice, 1.8)
    rescale_image(list_alice_dark, 1.8)
    pygame.transform.rotozoom(bubble, 0, 0.3)
    pygame.transform.rotozoom(knife, 0, 0.3)
    self.rect = idle[0].get_rect(topleft=(x, y))

  def eventos(self, bubbles_group):
    """
    Maneja los eventos del jugador (teclado) y realiza las acciones correspondientes.

    Args:
    - bubbles_group (pygame.sprite.Group): Grupo de burbujas del juego.
    """
    keys = pygame.key.get_pressed()

    if not self.esta_cayendo or (self.esta_cayendo and self.can_double_jump):
      if self.entrada_cayendo:
        self.flotar()
        self.entrada_cayendo = False
      elif keys[pygame.K_LEFT]:
        self.mover_left()
      elif keys[pygame.K_RIGHT]:
        self.mover_derecha()
      elif (keys[pygame.K_x]):
        self.disparar(bubbles_group)
      else:
        if self.contador_cambio_animation <= 0 and self.animation == self.list_animations[3]:
          self.idle()
          self.contador_cambio_animation = 30
        elif self.animation != self.list_animations[3]:
          self.idle()

  def player_collide_platforms(self, platforms_list):
    """
    Detecta y maneja las colisiones del jugador con las plataformas.

    Args:
    - platforms_list (list): Lista de plataformas en el nivel.
    """
    for plataforma in platforms_list:
        if self.rect.colliderect(plataforma.rect):
            if self.speed_y > 0 and self.esta_cayendo:
                self.speed_y = 0
                self.rect.bottom = plataforma.rect.top
                self.esta_cayendo = False
            elif self.speed_y < 0:
                self.esta_cayendo = False
                self.rect.top = plataforma.rect.bottom
                self.speed_y = 0

            if not self.rect.bottom == plataforma.rect.top and not self.rect.top == plataforma.rect.bottom:
                if self.speed_x > 0:
                    self.rect.right = plataforma.rect.left
                    self.speed_x = 0
                elif self.speed_x < 0:
                    self.rect.left = plataforma.rect.right
                    self.speed_x = 0

  def player_collide_floor(self, piso_rect):
    """
    Detecta y maneja la colisión del jugador con el suelo.

    Args:
    - piso_rect (pygame.Rect): Rectángulo de colisión del suelo.
    """
    if self.rect.colliderect(piso_rect):
      if self.speed_y > 0 and self.esta_cayendo:
        self.speed_y = 0
        self.rect.bottom = piso_rect.top
        self.esta_cayendo = False

  def reset_position(self):
    """
    Reinicia la posición y los atributos del jugador.
    """
    self.entrada_cayendo = True
    self.rect.topleft = (0, 0)
    self.key_recogida = False
    self.enter_portal = False
