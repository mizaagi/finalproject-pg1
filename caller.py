import pygame
import time
import main

def Call(square, lvl_pause):
  #print("c.Call | Test Print")
  _tick = 0
  square.image = pygame.image.load('call_square.png')
  square.tapped = False
  start_time = time.time()
  while square.tapped == False:
    _tick += 1
  # Work on possibly checking if the player has pressed the square within [lvl_pause] seconds (right away).
  end_time = time.time()
  if round((end_time - start_time), 2) > lvl_pause:
    square.gotit = False
    main.ins.accList.append(0)
  else:
    square.gotit = True
    main.ins.accList.append(100)