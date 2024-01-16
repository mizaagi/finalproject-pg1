import pygame
import time
import main

def Call(square, lvl_pause, ins):
  #print("c.Call | Test Print")
  _tick = 0
  square.image = pygame.image.load('call_square.png')
  square.tapped = False
  start_time = time.time()
  while square.tapped == False:
    _tick += 1
    ins.yourTick(str(_tick))
  # Work on possibly checking if the player has pressed the square within [lvl_pause] seconds (right away).
  end_time = time.time()
  if round((end_time - start_time), 2) > lvl_pause:
    square.gotit = False
    ins.accList.append(0)
  else:
    square.gotit = True
    ins.accList.append(100)
    ins.score += 1