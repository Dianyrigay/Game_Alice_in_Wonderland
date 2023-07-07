import pygame

class HealthBar():
  def __init__(self, width, height, max_health):
      self.health = max_health
      self.max_health = max_health
      self.width = width
      self.height = height

  def draw(self, screen, pos):
      ratio = self.health / self.max_health

      pygame.draw.rect(screen, (255, 0, 0), (pos[0] - self.width //2, pos[1] - 50, self.width, self.height))
      pygame.draw.rect(screen, (178, 191, 0), (pos[0] - self.width // 2, pos[1] - 50, self.width * ratio, self.height))
