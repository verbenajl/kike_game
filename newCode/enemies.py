# Characters and their methods and attributes

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import random
from math import fabs
import time

from functions import *

#from variables import *
from objects import *

class Monse(Player):
        def __init__(self,init):
                Player.__init__(self,init)
                self.im=pygame.image.load('../images/paperMonse.png').convert_alpha()
                self.image=pygame.transform.scale(self.im,(150,220))

                self.pos=Vector2(250*init.factor.x,250*init.factor.y)
                self.health=33
                self.speed=14
                self.color=(237,33,215)
                self.strength=0.35
                self.width=self.image.get_width()
                self.height=self.image.get_height()
                self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
                #self.bar_pos=Vector2(1200,900)
                self.h=self.health
		self.name='monse'
		self.image_win=pygame.transform.scale(self.image,(int(300*init.factor.x),
                int(500*init.factor.y)))


class Kike(Player):
        def __init__(self,init):
                Player.__init__(self,init)
                self.im=pygame.image.load('../images/paperKike.png').convert_alpha()
                self.image=pygame.transform.scale(self.im,(150,250))
                self.pos=Vector2(250*init.factor.x,250*init.factor.y)
                self.health=35
                self.speed=12
                self.color=(76,39,198)
                self.strength=0.4
                self.width=self.image.get_width()
                self.height=self.image.get_height()
                self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
                #self.bar_pos=Vector2(1200,900)
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
                self.h=self.health
		self.name='kike'
		self.image_win=pygame.transform.scale(self.image,(int(300*init.factor.x),
                int(500*init.factor.y)))



class Bebe(Player):
	def __init__(self,init):
		Player.__init__(self,init)
		self.im=pygame.image.load('../images/paperBebe.png').convert_alpha()
		self.image=pygame.transform.scale(self.im,(150,200))		
		self.pos=Vector2(250*init.factor.x,250*init.factor.y)
		self.health=30
		self.speed=15
		self.color=(220,0,0)	
		self.strength=0.3
                self.width=self.image.get_width()
                self.height=self.image.get_height()
            	self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
                #self.bar_pos=Vector2(1200,20)
                self.h=self.health
		self.name='bebe'
		self.image_win=pygame.transform.scale(self.image,(int(300*init.factor.x),
                int(500*init.factor.y)))


class JL(Player):
        def __init__(self,init):
                Player.__init__(self,init)
                self.image=pygame.image.load('../images/standing.png').convert_alpha()
                self.pos=Vector2(250,250)
                self.health=50
                self.speed=10
                self.color=(0,0,0)
		self.strength=0.3
		self.width=self.image.get_width()
		self.height=self.image.get_height()
		self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
		#self.bar_pos=Vector2(50,900)
		self.h=self.health
		self.name='JL'
	




class Cholo(Enemy):
	def __init__(self,init):
		Enemy.__init__(self,init)
		self.image=pygame.image.load('../images/cholo.png').convert_alpha()
		self.pos=Vector2(1000,101)
		self.imhit=False	
		self.strength=0.2
		self.speed=7
		self.color=(0,0,240)
		self.shoot_speed=13
		self.down=True
		self.up=False
		self.width=self.image.get_width()
		self.height=self.image.get_height()
		self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
		
		self.name='cholo'
		self.song=pygame.mixer.Sound('../music/03amanda.wav')
		self.song.set_volume(0.15)

	def move(self,init):
		global ddd
		self.update_center()
		if self.down:
			self.pos.y += self.speed*init.factor.y
		if self.up:
			self.pos.y -= self.speed*init.factor.y
		if self.up and self.pos.y < 000:
			self.down=True
			self.up = False
		if self.down and self.pos.y >700*init.factor.y:
			self.up=True
			self.down = False
		if not self.bullet_here:
                        ddd=Vector2(self.center.x,self.center.y)
		
	def shoot(self,screen,init):
		global ddd
		self.init_bullet()
		if self.bullet_here:
			self.bullet.movement_left(screen,self,ddd,init)
			if ddd.x < 2:
				self.bullet.gone()
                                self.bullet_here=False

			
class JLL(Cholo):
        def __init__(self,init):
		Enemy.__init__(self,init)
                self.im=pygame.image.load('../images/standing.png').convert_alpha()
		self.image=pygame.transform.flip(self.im,True,False)
                self.pos=Vector2(1000*init.factor.x,9*init.factor.y)
                self.imhit=False
                self.strength=0.4
                self.speed=9
                self.color=(0,0,0)
                self.shoot_speed=21*init.factor.x
                self.down=False
                self.up=False
                self.width=self.image.get_width()
                self.height=self.image.get_height()
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
		self.xx=1
		self.right=False
		self.left=False
		self.name='JL'
		self.song=pygame.mixer.Sound('../music/01onemealX.wav')
		self.song.set_volume(0.15)
	
	def down_left(self):
		self.right=False
		self.left=True
		self.up=False
		self.down=True
	
	def down_right(self):
                self.right=True
                self.left=False
                self.up=False
                self.down=True


	def right_up(self):
		self.right=True
                self.left=False
                self.up=True
                self.down=False

	def left_up(self):
                self.right=False
                self.left=True
                self.up=True
                self.down=False		


	def move(self,init):
		global ddd
		self.update_center()
		if self.xx == 1:
			if  self.pos.y <10*init.factor.y or (self.pos.y >400*init.factor.y and self.pos.y <410*init.factor.y):
				self.down_left()
			if self.pos.y >250*init.factor.y and self.pos.y <260*init.factor.y or \
			(self.pos.y >550*init.factor.y and self.pos.y <560*init.factor.y):
				self.down_right()
			if self.pos.y >800*init.factor.y:
				self.xx=2
			if self.left and self.down:
				self.pos.x -= self.speed*init.factor.x
				self.pos.y += self.speed*init.factor.y
			if self.right and self.down:
                                self.pos.x += self.speed*init.factor.x
                                self.pos.y += self.speed*init.factor.y

			
		if self.xx ==2: 
			if self.pos.y > 800*init.factor.y or (self.pos.y >400*init.factor.y \
			and self.pos.y <410*init.factor.y):
				self.right_up()
			if self.pos.y >550*init.factor.y and self.pos.y <560*init.factor.y or (
			self.pos.y >250*init.factor.y and self.pos.y <260*init.factor.y):			
				self.left_up()
			if self.pos.y < 10*init.factor.y:
                                self.xx=1
			if self.right and self.up :
				self.pos.x += self.speed*init.factor.x
				self.pos.y -= self.speed*init.factor.y
			if self.left and self.up :
                                self.pos.x -= self.speed*init.factor.x
                                self.pos.y -= self.speed*init.factor.y
		


		if not self.bullet_here:
			ddd=Vector2(self.center.x,self.center.y)


class Ramon(Cholo):
	def __init__(self,init):
		Cholo.__init__(self,init)
		self.health=100
		self.h=100
		self.speed=7.5
		self.im=pygame.image.load('../images/ramon.png').convert_alpha()
		self.image=pygame.transform.scale(self.im,(200,300))
		self.width=self.image.get_width()
		self.height=self.image.get_height()
		self.center=Vector2(self.pos.x+self.width/2,self.pos.y+self.height/2)
		self.strength=0.8
		self.image=pygame.transform.scale(self.image,(int(self.width*init.factor.x),
		int(self.height*init.factor.y)))
		self.color=(0,250,0)	
		self.level = False
		self.pos=Vector2(1000*init.factor.x,101*init.factor.y)	
		self.left=True
		self.right=False
		self.down=False
		self.up=False
		self.name='ramon'	
		self.shoot_speed=15
		self.song=pygame.mixer.Sound('../music/vampGalX.wav')
		self.song.set_volume(0.15)

	def allFalse(self,dire1,dire2,dire3,dire4):
		dire1=True
		dire2=False
		dire3=False
		dire4=False

	def move(self,init):	
		global ddd
		self.update_center()
		if self.pos.x >800*init.factor.y  and self.pos.x <850*init.factor.y \
		and  (self.pos.y < 110*init.factor.y and self.pos.y >90*init.factor.y \
		or self.pos.y > 640*init.factor.y and self.pos.y < 650*init.factor.y) :
			self.right=True
			self.left=False
			self.down=False
			self.up=False
		elif self.pos.x > 1100*init.factor.y and self.pos.x < 1200*init.factor.y \
		and self.pos.y < 110*init.factor.y and self.pos.y >90*init.factor.y and self.right:
			self.right=False
			self.down=True
			self.up=False
			self.left=False
		elif self.pos.y > 640*init.factor.y and self.pos.y < 650*init.factor.y \
		and self.pos.x  >1100*init.factor.y  and self.pos.x <1200*init.factor.y and (self.down or self.up):
			self.left=True
			self.down=False
			self.right=False
			self.up=False
		elif self.pos.y > 90*init.factor.y and self.pos.y < 110*init.factor.y \
	  	and self.pos.x  >1100*init.factor.y  and self.pos.x <1200*init.factor.y and self.up:
                        self.left=True
                        self.down=False
                        self.right=False
                        self.up=False
		elif self.pos.y > 640*init.factor.y and self.pos.y < 650*init.factor.y \
		and self.right and self.pos.x  >1100*init.factor.y  and self.pos.x <1200*init.factor.y:
			self.up=True
			self.left=False
			self.down=False
			self.right=False


		if self.down:
			self.pos.y += self.speed*init.factor.y
		if self.up:
			self.pos.y -= self.speed*init.factor.y	
		if self.left:
			self.pos.x -= self.speed*init.factor.x
		if self.right:
			self.pos.x += self.speed*init.factor.x
		if not self.bullet_here:
                        ddd=Vector2(self.center.x,self.center.y)


		
 	

	
	
