import pygame

class Square:
  """Class for the squares."""

  def __init__(self, ry_game, x, y, name):
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
    self.name = name

  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def call(self, lvl_pause):
    #print("Square Call / exec nameCalled = True | Test Print")
    exec(self.name + "called = True")