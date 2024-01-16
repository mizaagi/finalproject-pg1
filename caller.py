import pygame
import time
import main

def Call(square, lvl_pause, ins):
  #print("c.Call | Test Print")
  _tick = 0
  square.image = pygame.image.load('call_square.png')
  square.tapped = False
  time.sleep(lvl_pause)
  if ins.lasttap == square.num:
    square.gotit = True
    ins.accList.append(100)
    ins.score += 1
  else:
    square.gotit = False
    ins.accList.append(0)
