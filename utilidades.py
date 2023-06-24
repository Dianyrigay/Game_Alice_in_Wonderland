import pygame

def getSurfaceFromSpriteSheet(path, columnas, filas, step=1):
  lista = []
  surface_imagen = pygame.image.load(path)
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
