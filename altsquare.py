import pygame
from pygame.sprite import Sprite

class Square(Sprite):
  def __init__(self, ry_game):
    super().__init__()
    self.screen = ry_game.screen

    self.image = pygame.image.load('square.png')
    self.rect = self.image.get_rect()

    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    