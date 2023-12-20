import pygame
import sys
import random
import time
from settings import Settings
from square import Square


white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)




def yourScore(score):
  msg = font_style.render("Score: " + str(score), True, yellow)
  DISPLAYSURF.blit(msg, [0, 0])
def RHYTHM(level, level_diff):
  for beat in level:
    if beat == 1: # Upper left
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 2: # Upper middle
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 3: # Upper right
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 4: # Middle left
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 5: # Middle middle
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 6: # Middle right
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 7: # Lower left
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 8: # Lower middle
      pass # Flash the correct square
      time.sleep(level_diff)
    if beat == 9: # Lower right
      pass # Flash the correct square
      time.sleep(level_diff)

class RhythmGame:
  """Overall class to manage game assets and behavior."""

  def __init__(self, xoffset=0, yoffset=0):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.settings = Settings()
    self.xoffset = xoffset
    self.yoffset = yoffset

    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Final Project")

    self.squareTL = Square(self, 80+xoffset, 30+yoffset)
    self.squareMT = Square(self, 300+xoffset, 30+yoffset)
    self.squareTR = Square(self, 520+xoffset, 30+yoffset)
    self.squareML = Square(self, 80+xoffset, 250+yoffset)
    self.squareMM = Square(self, 300+xoffset, 250+yoffset)
    self.squareMR = Square(self, 520+xoffset, 250+yoffset)
    self.squareBL = Square(self, 80+xoffset, 470+yoffset)
    self.squareMB = Square(self, 300+xoffset, 470+yoffset)
    self.squareBR = Square(self, 520+xoffset, 470+yoffset)

    self.bg_color = (25, 60, 105)

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_KP_1:
            pass
          if event.key == pygame.K_KP_2:
            pass
          if event.key == pygame.K_KP_3:
            pass
          if event.key == pygame.K_KP_4:
            pass
          if event.key == pygame.K_KP_5:
            pass
          if event.key == pygame.K_KP_6:
            pass
          if event.key == pygame.K_KP_7:
            self.squareTL.image = pygame.transform.scale(self.squareTL.image, (175, 175))
            self.squareTL.rect.x = 90+self.xoffset
            self.squareTL.rect.y = 40+self.yoffset
          if event.key == pygame.K_KP_8:
            pass
          if event.key == pygame.K_KP_9:
            pass

      # Redraw the screen during each pass through the loop.
      self.screen.fill(self.bg_color)
      self.squareTL.blitme()
      self.squareMT.blitme()
      self.squareTR.blitme()
      self.squareML.blitme()
      self.squareMM.blitme()
      self.squareMR.blitme()
      self.squareBL.blitme()
      self.squareMB.blitme()
      self.squareBR.blitme()
      
      # Make the most recently drawn screen visible.
      pygame.display.flip()

      # Check to see if the keys aren't pressed down.
      for event in pygame.event.get(pygame.KEYUP):
        if event.key == pygame.K_KP_7:
          self.squareTL.image = pygame.image.load('square.png')
          self.squareTL.rect.x = 80+self.xoffset
          self.squareTL.rect.y = 30+self.yoffset

if __name__ == '__main__':
  # Make a game instance, and run the game.
  ins = RhythmGame(xoffset=-65)
  ins.run_game()