# New Commits below - this comment is to fix the error.

import pygame
import sys
import time
from settings import Settings
from square import Square
import caller as c
import threading
import random
pygame.init()

font_style = pygame.font.SysFont("sans-serif", 30)
white = (255, 255, 255)
yellow = (255, 255, 100)
black = (0, 0, 0)
red = (210, 50, 80)
green = (0, 255, 0)
blue = (50, 150, 210)
lvl1 = [7, 4, 3, 7, 6, 9, 1, 3, 6, 6, 5, 3]
lvl1_pause = 2.0
lvl2 = [7, 4, 3, 7, 6, 9, 1, 3, 6, 6, 5, 3]
lvl2_pause = 1.5
lvl3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
lvl3_pause = 0.3
done = False


TLcalled = None
MTcalled = None
TRcalled = None
MLcalled = None
MMcalled = None
MRcalled = None
BLcalled = None
MBcalled = None
BRcalled = None

def setGlobals():
  global TLcalled
  global MTcalled
  global TRcalled
  global MLcalled
  global MMcalled
  global MRcalled
  global BLcalled
  global MBcalled
  global BRcalled

def callCheckThread():
  time.sleep(1)
  #print("callCheckThread Started | Test Print")
  global TLcalled
  global MTcalled
  global TRcalled
  global MLcalled
  global MMcalled
  global MRcalled
  global BLcalled
  global MBcalled
  global BRcalled
  while True:
    if TLcalled:
      #print("callCheckThread if TLcalled | Test Print")
      c.Call(ins.squareTL, ins.lvl_pause, ins)
      #print(str(ins.squareTL.gotit))
      ins.callDone = True
      #print(ins.lvl_pause)
      TLcalled = False
    if MTcalled:
      c.Call(ins.squareMT, ins.lvl_pause, ins)
      #print(str(ins.squareMT.gotit))
      ins.callDone = True
      MTcalled = False
    if TRcalled:
      c.Call(ins.squareTR, ins.lvl_pause, ins)
      #print(str(ins.squareTR.gotit))
      ins.callDone = True
      TRcalled = False
    if MLcalled:
      c.Call(ins.squareML, ins.lvl_pause, ins)
      #print(str(ins.squareML.gotit))
      ins.callDone = True
      MLcalled = False
    if MMcalled:
      c.Call(ins.squareMM, ins.lvl_pause, ins)
      #print(str(ins.squareMM.gotit))
      ins.callDone = True
      MMcalled = False
    if MRcalled:
      c.Call(ins.squareMR, ins.lvl_pause, ins)
      #print(str(ins.squareMR.gotit))
      ins.callDone = True
      MRcalled = False
    if BLcalled:
      c.Call(ins.squareBL, ins.lvl_pause, ins)
      #print(str(ins.squareBL.gotit))
      ins.callDone = True
      BLcalled = False
    if MBcalled:
      c.Call(ins.squareMB, ins.lvl_pause, ins)
      #print(str(ins.squareMB.gotit))
      ins.callDone = True
      MBcalled = False
    if BRcalled:
      c.Call(ins.squareBR, ins.lvl_pause, ins)
      ins.callDone = True
      #print(str(ins.squareBR.gotit))
      BRcalled = False

def tapCheckThread():
  time.sleep(1)
  #print("tapCheckThread Started | Test Print")
  while True:
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_KP_1:
          ins.squareBL.tapped = True
        if event.key == pygame.K_KP_2:
          ins.squareMB.tapped = True
        if event.key == pygame.K_KP_3:
          ins.squareBR.tapped = True
        if event.key == pygame.K_KP_4:
          ins.squareML.tapped = True
        if event.key == pygame.K_KP_5:
          ins.squareMM.tapped = True
        if event.key == pygame.K_KP_6:
          ins.squareMR.tapped = True
        if event.key == pygame.K_KP_7:
          #print("tapCheckThread | Test Print")
          ins.squareTL.tapped = True
        if event.key == pygame.K_KP_8:
          ins.squareMT.tapped = True
        if event.key == pygame.K_KP_9:
          ins.squareTR.tapped = True
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_KP_1:
          ins.squareBL.tapped = False
        if event.key == pygame.K_KP_2:
          ins.squareMB.tapped = False
        if event.key == pygame.K_KP_3:
          ins.squareBR.tapped = False
        if event.key == pygame.K_KP_4:
          ins.squareML.tapped = False
        if event.key == pygame.K_KP_5:
          ins.squareMM.tapped = False
        if event.key == pygame.K_KP_6:
          ins.squareMR.tapped = False
        if event.key == pygame.K_KP_7:
          ins.squareTL.tapped = False
        if event.key == pygame.K_KP_8:
          ins.squareMT.tapped = False
        if event.key == pygame.K_KP_9:
          ins.squareTR.tapped = False


class RhythmGame:
  """Overall class to manage game assets and behavior."""

  def __init__(self, xoffset=0, yoffset=0):
    """Initialize the game, and create game resources."""
    pygame.init()
    self.settings = Settings()
    self.xoffset = xoffset
    self.yoffset = yoffset
    self.score = 0
    self.accList = []
    self.acc = 0
    self.level = 1
    self.lvl_pause = lvl1_pause
    self.callDone = False

    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Final Project")

    self.squareTL = Square(self, 80+xoffset, 30+yoffset, "TL")
    self.squareMT = Square(self, 300+xoffset, 30+yoffset, "MT")
    self.squareTR = Square(self, 520+xoffset, 30+yoffset, "TR")
    self.squareML = Square(self, 80+xoffset, 250+yoffset, "ML")
    self.squareMM = Square(self, 300+xoffset, 250+yoffset, "MM")
    self.squareMR = Square(self, 520+xoffset, 250+yoffset, "MR")
    self.squareBL = Square(self, 80+xoffset, 470+yoffset, "BL")
    self.squareMB = Square(self, 300+xoffset, 470+yoffset, "MB")
    self.squareBR = Square(self, 520+xoffset, 470+yoffset, "BR")

    self.bg_color = (25, 60, 105)
  def yourScore(self, score):
    msg = font_style.render("Score: " + str(score) + "    Level: " + str(self.level), True, yellow)
    self.screen.blit(msg, [750+self.xoffset, 30+self.yoffset])

  def yourAcc(self, acc):
    msg = font_style.render("Acc: " + str(acc) + "%", True, yellow)
    self.screen.blit(msg, [750+self.xoffset, 90+self.yoffset])
  
  def yourTick(self, tick):
    msg = font_style.render("Tick: " + str(tick)[-1], True, yellow)
    self.screen.blit(msg, [750+self.xoffset, 150+self.yoffset])

  def yourInstructions(self):
    p1 = font_style.render("Instructions: Press [RETURN] for level 1,", True, yellow)
    p2 = font_style.render("[Y] for level 2, [U] for level 3, or press [R] for", True, yellow)
    p3 = font_style.render("a randomly generated level. Have fun!", True, yellow)
    self.screen.blit(p1, [750 + self.xoffset, 210 + self.yoffset])
    self.screen.blit(p2, [760 + self.xoffset, 240 + self.yoffset])
    self.screen.blit(p3, [760 + self.xoffset, 270 + self.yoffset])

  def RHYTHM(self, level, level_pause):
    global TLcalled
    global MTcalled
    global TRcalled
    global MLcalled
    global MMcalled
    global MRcalled
    global BLcalled
    global MBcalled
    global BRcalled

    time.sleep(1)
    self.level_pause = level_pause
    self.acc = 100
    self.score = 0
    self.accList.clear()

    for beat in level:
      self.done = False
      c = 0
        #time.sleep(self.level_pause)
      if beat == 1: # Lower left
        BLcalled = True

        #time.sleep(self.level_pause)
      if beat == 2: # Lower middle
        MBcalled = True

        #time.sleep(self.level_pause)
      if beat == 3: # Lower right
        BRcalled = True
        #time.sleep(self.level_pause)

      if beat == 4: # Middle left
        MLcalled = True

        #time.sleep(self.level_pause)
      if beat == 5: # Middle
        MMcalled = True

        #time.sleep(self.level_pause)
      if beat == 6: # Middle right
        MRcalled = True

      if beat == 7:  # Upper left
        # print("RHYTHM nameCalled = True | Test Print")
        TLcalled = True  # self.squareTL.call(level_pause)

        # time.sleep(self.level_pause)
      if beat == 8:  # Upper middle
        MTcalled = True

        # time.sleep(self.level_pause)
      if beat == 9:  # Upper right
        TRcalled = True

        #time.sleep(self.level_pause)
      
    

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      # Watch for keyboard and mouse events.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            #print("Pressing Enter | Test Print")
            self.RHYTHM(lvl1, lvl1_pause)
          if event.key == pygame.K_y:
            self.level = 2
            self.level_pause = lvl2_pause
            self.lvl_pause = lvl2_pause
            self.RHYTHM(lvl2, lvl2_pause)
          if event.key == pygame.K_u:
            self.level = 3
            self.level_pause = lvl3_pause
            self.lvl_pause = lvl3_pause
            self.RHYTHM(lvl3, lvl3_pause)
          if event.key == pygame.K_r:
            self.level = 0
            rndLevel_pause = random.random() + random.random() * random.random()
            rndLevel = []
            for _ in range(1, random.randint(9, 27)):
              rndLevel.append(random.randint(1, 9))
            self.RHYTHM(rndLevel, rndLevel_pause)

          if event.key == pygame.K_KP_1:
            self.squareBL.tapped = True
            self.squareBL.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareBL.rect.x = 90+self.xoffset
            self.squareBL.rect.y = 480+self.yoffset
          if event.key == pygame.K_KP_2:
            self.squareMB.tapped = True
            self.squareMB.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareMB.rect.x = 310+self.xoffset
            self.squareMB.rect.y = 480+self.yoffset
          if event.key == pygame.K_KP_3:
            self.squareBR.tapped = True
            self.squareBR.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareBR.rect.x = 530+self.xoffset
            self.squareBR.rect.y = 480+self.yoffset
          if event.key == pygame.K_KP_4:
            self.squareML.tapped = True
            self.squareML.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareML.rect.x = 90+self.xoffset
            self.squareML.rect.y = 260+self.yoffset
          if event.key == pygame.K_KP_5:
            self.squareMM.tapped = True
            self.squareMM.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareMM.rect.x = 310+self.xoffset
            self.squareMM.rect.y = 260+self.yoffset
          if event.key == pygame.K_KP_6:
            self.squareMR.tapped = True
            self.squareMR.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareMR.rect.x = 530+self.xoffset
            self.squareMR.rect.y = 260+self.yoffset
          if event.key == pygame.K_KP_7:
            self.squareTL.tapped = True
            self.squareTL.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareTL.rect.x = 90+self.xoffset
            self.squareTL.rect.y = 40+self.yoffset
          if event.key == pygame.K_KP_8:
            self.squareMT.tapped = True
            self.squareMT.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareMT.rect.x = 310+self.xoffset
            self.squareMT.rect.y = 40+self.yoffset
          if event.key == pygame.K_KP_9:
            self.squareTR.tapped = True
            self.squareTR.image = pygame.transform.scale(pygame.image.load('pressed_square.png'), (175, 175))
            self.squareTR.rect.x = 530+self.xoffset
            self.squareTR.rect.y = 40+self.yoffset

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
      try:
        self.acc = sum(self.accList) / float(len(self.accList))
      except:
        self.acc = 100
      self.yourAcc(self.acc)
      self.yourScore(self.score)
      self.yourInstructions()
      
      # Make the most recently drawn screen visible.
      pygame.display.flip()

      # Check to see if the keys aren't pressed down.
      for event in pygame.event.get(pygame.KEYUP):
        if event.key == pygame.K_KP_1:
          self.squareBL.tapped = False
          self.squareBL.image = pygame.image.load('square.png')
          self.squareBL.rect.x = 80+self.xoffset
          self.squareBL.rect.y = 470+self.yoffset
        if event.key == pygame.K_KP_2:
          self.squareMB.tapped = False
          self.squareMB.image = pygame.image.load('square.png')
          self.squareMB.rect.x = 300+self.xoffset
          self.squareMB.rect.y = 470+self.yoffset
        if event.key == pygame.K_KP_3:
          self.squareBR.tapped = False
          self.squareBR.image = pygame.image.load('square.png')
          self.squareBR.rect.x = 520+self.xoffset
          self.squareBR.rect.y = 470+self.yoffset
        if event.key == pygame.K_KP_4:
          self.squareML.tapped = False
          self.squareML.image = pygame.image.load('square.png')
          self.squareML.rect.x = 80+self.xoffset
          self.squareML.rect.y = 250+self.yoffset
        if event.key == pygame.K_KP_5:
          self.squareMM.tapped = False
          self.squareMM.image = pygame.image.load('square.png')
          self.squareMM.rect.x = 300+self.xoffset
          self.squareMM.rect.y = 250+self.yoffset
          self.score += 1
        if event.key == pygame.K_KP_6:
          self.squareMR.tapped = False
          self.squareMR.image = pygame.image.load('square.png')
          self.squareMR.rect.x = 520+self.xoffset
          self.squareMR.rect.y = 250+self.yoffset
        if event.key == pygame.K_KP_7:
          self.squareTL.tapped = False
          self.squareTL.image = pygame.image.load('square.png')
          self.squareTL.rect.x = 80+self.xoffset
          self.squareTL.rect.y = 30+self.yoffset
        if event.key == pygame.K_KP_8:
          self.squareMT.tapped = False
          self.squareMT.image = pygame.image.load('square.png')
          self.squareMT.rect.x = 300+self.xoffset
          self.squareMT.rect.y = 30+self.yoffset
        if event.key == pygame.K_KP_9:
          self.squareTR.tapped = False
          self.squareTR.image = pygame.image.load('square.png')
          self.squareTR.rect.x = 520+self.xoffset
          self.squareTR.rect.y = 30+self.yoffset

if __name__ == '__main__':
  # Make a game instance, and run the game.
  _callCheckThread = threading.Thread(target=callCheckThread, daemon=True)
  _tapCheckThread = threading.Thread(target=tapCheckThread, daemon=True)
  ins = RhythmGame(xoffset=-60)
  #print("Start Game | Test Print")
  _callCheckThread.start()
  _tapCheckThread.start()
  ins.run_game()
