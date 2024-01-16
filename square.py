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
    if self.name == "TL":
      self.num = 7
    elif self.name == "MT":
      self.num = 8
    elif self.name == "TR":
      self.num = 9
    elif self.name == "ML":
      self.num = 4
    elif self.name == "MM":
      self.num = 5
    elif self.name == "MR":
      self.num = 6
    elif self.name == "BL":
      self.num = 1
    elif self.name == "MB":
      self.num = 2
    elif self.name == "BR":
      self.num = 3
  def blitme(self):
    self.screen.blit(self.image, self.rect)

  def call(self, lvl_pause):
    #print("Square Call / exec nameCalled = True | Test Print")
    exec(self.name + "called = True")