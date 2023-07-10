import pygame
from constantes import *

def get_surface_spritesheet(path, columnas, filas, step=1):
  lista = []
  surface_imagen = pygame.image.load(path).convert_alpha()
  fotograma_ancho = int(surface_imagen.get_width()/columnas)
  fotograma_alto = int(surface_imagen.get_height()/filas)
  x = 0
  for columna in range(0, columnas, step):
      for fila in range(filas):
          x = columna * fotograma_ancho
          y = fila * fotograma_alto
          surface_fotograma = surface_imagen.subsurface(
              x, y, fotograma_ancho, fotograma_alto)
          lista.append(surface_fotograma)
  return lista

def rescale_image(list_animations, size):
  for list_images in list_animations:
    for i in range(len(list_images)):
        list_images[i] = pygame.transform.rotozoom(
            list_images[i], 0, size)

def write_screen(screen, text, color, cantidad=".", position=None):
  text_lives = font.render(text + "{0}".format(cantidad), True, color)
  if position is None:
      center = text_lives.get_rect(center=(WIDTH_PANTALLA/2, HEIGHT_PANTALLA/2))
      screen.blit(text_lives, center)
  elif position is not None:
      screen.blit(text_lives, position)
