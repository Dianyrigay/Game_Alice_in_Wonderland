import pygame
from constantes import *

def obtener_surface_de_spriteSheet(path, columnas, filas, step=1):
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

def reescalar_imagen(lista_animaciones, tamanio):
  for lista_imagenes in lista_animaciones:
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.rotozoom(
            lista_imagenes[i], 0, tamanio)

def escribir_screen(screen, texto, color, cantidad=".", posicion=None):
  # font = pygame.font.SysFont("Arial Narrow", 40)
  text_lives = font.render(texto + "{0}".format(cantidad), True, color)
  if posicion is None:
      center = text_lives.get_rect(center=(WIDTH_PANTALLA/2, HEIGHT_PANTALLA/2))
      screen.blit(text_lives, center)
  elif posicion is not None:
      screen.blit(text_lives, posicion)

