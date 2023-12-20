import pygame

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
    #self.rect.width = self.image.get_rect().width
    #self.rect.length = self.image.get_rect().width
    #if w and l:
      #self.rect.width = w
      #self.rect.length = l
    #exec(f"self.rect.{pos} = self.screen_rect.{pos}")
    #self.rect.topleft = self.screen_rect.topleft

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def change_size(self, w, l):
    pass