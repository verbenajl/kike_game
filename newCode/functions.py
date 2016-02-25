##	General functions used in kikeGame

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import random
from math import fabs
import time

Fullscreen=False


def start_screen():
	global event, Fullscreen, SCREEN_SIZE
	for event in pygame.event.get():
		if event.type ==QUIT :
                        exit()
        if event.type == KEYDOWN:
        	if event.key == K_f:
			Fullscreen = not Fullscreen
			if Fullscreen:
        			screen=pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
			else:
				screen=pygame.display.set_mode(SCREEN_SIZE, 0, 32)
		elif event.key == K_ESCAPE:
			exit()




	
	






