import pygame
import time

class Square:
  """Class for the squares."""

  def __init__(self, ry_game, x, y):
    self.screen = ry_game.screen
    self.screen_rect = ry_game.screen.get_rect()
    self.image = pygame.image.load('square.png')
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.rect.size = (50, 50)
    self.baseWid = self.rect.width
    self.tapped = False
    self.gotit = None

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def call(self, lvl_pause):
    _tick = 0
    self.image = pygame.image.load('call_square.png')
    self.tapped = False
    start_time = time.time()
    time.sleep(lvl_pause)
    while self.tapped == False:
      _tick += 1
    end_time = time.time()
    if round((end_time - start_time), 2) > lvl_pause:
      self.gotit = False
    else:
      self.gotit = True