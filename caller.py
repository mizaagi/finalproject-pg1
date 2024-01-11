import pygame
import time

def Call(square, lvl_pause):
  #print("c.Call | Test Print")
  _tick = 0
  square.image = pygame.image.load('call_square.png')
  square.tapped = False
  start_time = time.time()
  while square.tapped == False:
    _tick += 1
  end_time = time.time()
  if round((end_time - start_time), 2) > lvl_pause:
    square.gotit = False
  else:
    square.gotit = True