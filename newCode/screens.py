# Intro, scenes and that stuff

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import random
from math import fabs
import time

from functions import *
from objects import *

class IntroScreen():
	def __init__(self):
		self.n=1

	def display(self,screen):
		global event
		
		if event.type == KEYUP and event.key == K_LEFT:
			if n ==1:
				n=3
			else:
				self.n -= 1
		elif event.type == KEYUP and event.key == K_RIGHT:
			if n==3:
				n =1
			else:
				self.n += 1
		else:
			pass
		

		if self.n==1:
			play=kike
		if self.n==2:
			play=monse
		if self.n==3:
			play=bebe

		screen.blit(play.image,(play.pos.x, play.pos.y))
		





