## general Classes for the kike Game

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
import random
from math import fabs
import time

from functions import *
#from variables import *

class initial():
	def __init__(self):
		pass 

	def start(self):
		global dispInfo
		pygame.mixer.pre_init()
		pygame.init()
		pygame.display.set_caption("kike Game | by JL Verbena")
		pygame.mouse.set_visible(False)
		dispInfo=pygame.display.Info()

		self.SCREEN_SIZE = (dispInfo.current_w,dispInfo.current_h )
		self.SCREEN_SIZEb = Vector2(1680,1050)
		self.factor=Vector2((dispInfo.current_w/self.SCREEN_SIZEb.x),((dispInfo.current_h/self.SCREEN_SIZEb.y)))
		screen=pygame.display.set_mode(self.SCREEN_SIZE,0,32)
		return screen
		
		


class Screen():
	def __init__(self):
		self.Fullscreen=False
		dispInfo=pygame.display.Info()
		self.SCREEN_SIZE = (dispInfo.current_w,dispInfo.current_h )

	def start_screen(self):
		global event
		for event in pygame.event.get():
                	if event.type ==QUIT :
                        	exit()
        	if event.type == KEYDOWN:
                	if event.key == K_f:
                        	self.Fullscreen = not self.Fullscreen
                        	if self.Fullscreen:
                               		screen=pygame.display.set_mode(self.SCREEN_SIZE, FULLSCREEN, 32)
                        	else:
                               		screen=pygame.display.set_mode(self.SCREEN_SIZE, 0, 32)
               		elif event.key == K_ESCAPE:
                       		exit()

	
		


class Bullet():
	def __init__(self):
		pass
		self.pos=Vector2(0,0)
	
	
	def movement(self,screen,play,ccc,init):
		pygame.draw.circle(screen, play.color, (int(ccc.x),int(ccc.y)), 10 )
		ccc.x += play.shoot_speed*init.factor.x
		self.pos=Vector2(ccc)	
	
	def movement_left(self,screen,play,ddd,init):
		pygame.draw.circle(screen, play.color, (int(ddd.x),int(ddd.y)), 10 )
		ddd.x -= play.shoot_speed*init.factor.x
		self.pos=Vector2(ddd)
	
	def gone(self):
		del self

			

class Character():
	def __init__(self,init):
		self.bullet_here=False
		self.hit_sound=pygame.mixer.Sound('../sounds/punch2.wav')	
		self.hit_sound.set_volume(1)
		self.blood=pygame.image.load('../images/blood.png').convert_alpha()
		self.width=self.blood.get_width()
                self.height=self.blood.get_height()
		self.blood=pygame.transform.scale(self.blood,(int(self.width*init.factor.x),int(self.height*init.factor.y)))	

	def display_health(self,screen,init):
		if self.health > 0:
			pygame.draw.rect(screen,self.color,(self.bar_pos.x,self.bar_pos.y,
			400*(self.health/self.h)*init.factor.x,40*init.factor.y))
			
		else:
			pass		
	
	def update_center(self):
		self.center = Vector2(self.pos.x+self.width/2, self.pos.y+self.height/2)	

	def init_bullet(self):
		if not self.bullet_here:
                        self.bullet=Bullet()
                        self.bullet_here=True

	def blit(self,screen,image,pos):
		screen.blit(image,(pos.x,pos.y))

	def im_hit(self,enem,screen):
                if enem.bullet_here and enem.bullet.pos.x+50 >= self.pos.x and enem.bullet.pos.x <= self.pos.x + self.width and \
                enem.bullet.pos.y >= self.pos.y+20 and enem.bullet.pos.y <= self.pos.y +self.height :
                        self.imhit=True
			self.hit_sound.play()
                else:
                        self.imhit=False
                if self.imhit:
                        self.health -= enem.strength	
			screen.blit(self.blood,(self.pos.x-120,self.pos.y-50))

		

	def im_hit_left(self,enem,screen):
		if enem.bullet_here and self.pos.x <= enem.bullet.pos.x-50 and self.pos.x+self.width >= enem.bullet.pos.x  and \
                self.pos.y + 20 <= enem.bullet.pos.y and self.pos.y+self.height >= enem.bullet.pos.y :
                        self.imhit=True
			self.hit_sound.play()
                else:
                        self.imhit=False
                if self.imhit:
                        self.health -= enem.strength
			screen.blit(self.blood,(self.pos.x-120,self.pos.y-50))


class Player(Character):
	
	def __init__(self,init):
		Character.__init__(self,init)
		self.pos=Vector2(250,250)
		self.health = 10
		self.speed = 10		
		self.shoot_speed=10
		self.sh=False
		self.center=Vector2(250,250)
		self.game_time=0
		self.level=0	
		self.cont=False
		self.bar_pos=Vector2(10*init.factor.x,10*init.factor.y)

	def move(self,init):
		global ccc	
		self.update_center()
               	if event.type == KEYDOWN and event.key == K_LEFT:
			self.pos.x -= self.speed*init.factor.x
		if event.type == KEYDOWN and event.key == K_RIGHT:
			self.pos.x += self.speed*init.factor.x
		if event.type == KEYDOWN and event.key == K_UP:
			self.pos.y -= self.speed*init.factor.y
		if event.type == KEYDOWN and event.key == K_DOWN:
			self.pos.y += self.speed*init.factor.y
		if not self.bullet_here:
			ccc=Vector2(self.center.x,self.center.y)


	def shoot(self,screen,init):
		#global ccc
		if event.type == KEYDOWN and event.key == K_SPACE:
			self.init_bullet()
		if self.bullet_here:
			self.bullet.movement(screen,self,ccc,init)
			if ccc.x > dispInfo.current_w:
				self.bullet.gone()
				self.bullet_here=False
		
	def check_level(self):
		
			self.game_time=0
		


class Enemy(Character):
	def __init__(self,init):
		dispInfo=pygame.display.Info()
		Character.__init__(self,init)
		self.health=50
		self.h=self.health
		self.speed=12
		self.bar_pos=Vector2(dispInfo.current_w-400,dispInfo.current_h-100)	
		self.h=50
		self.timeB=0

		
	def blit(self,screen,image,pos):
                screen.blit(image,(pos.x,pos.y))

	def im_beaten(self,play):
		global time_passed
		if self.health==0:
			if self.timeB < 15000:
				screen.blit(pygame.transform.rotate(self.image,90),(pos.x,pos.y))
			else :
				play.level +=1	
		self.timeB += time_passed
			


class IntroScreen():
        def __init__(self,init):
		global dispInfo
                self.n=1
		self.play='kike'
		self.choosing=True
		self.level=False
		self.time=0	
		self.song=pygame.mixer.Sound('../music/introOutro2.wav')
		self.song.set_volume(0.5)
		self.outro=pygame.mixer.Sound('../music/shesHornyRemX.wav')
		self.outro.set_volume(0.15)
		self.bet=pygame.mixer.Sound('../music/outro1.wav')
		self.opening_song=pygame.mixer.Sound('../music/introOutro1.wav')
		self.opening_bool=True
		self.cover=pygame.image.load('../images/cover.png').convert()
		self.cover_width=self.cover.get_width()
		self.cover_height=self.cover.get_height()
		self.ymove = (dispInfo.current_h+(50*init.factor.y))
		self.cover=pygame.transform.scale(self.cover,(int(self.cover_width*init.factor.x), \
			int(self.cover_height*init.factor.y)))

		self.end=pygame.image.load('../images/end.png').convert()
                self.end_width=self.end.get_width()
                self.end_height=self.end.get_height()
                self.end=pygame.transform.scale(self.end,(int(self.end_width*init.factor.x),int(self.end_height*init.factor.y)))

	def opening(self,screen,font,init):
		self.opening_song.play()
		screen.blit(self.cover,(0,0))
		#screen.blit(font.render('KIKE GAME', True, (250,0,0)),(500*init.factor.x,400*init.factor.y))
		if event.type == KEYUP and event.key == K_SPACE:
			self.level=True
			self.opening_song.stop()
			self.opening_bool=False
                        
		
	def closing(self,screen, font,init):
		self.ymove -=  1*init.factor.y

		screen.blit(font.render('POR JL VERBENA', True, (250,0,0)), ( 100*init.factor.x,self.ymove))
		screen.blit(font.render('PARA KIKE', True, (250,0,0)), ( 100*init.factor.x,self.ymove+(70*init.factor.y)))	
		screen.blit(font.render('MONSE', True, (250,0,0)), ( 100*init.factor.x,(self.ymove+((70*2)*init.factor.y))))
		screen.blit(font.render('Y JOSE ANGEL', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((70*3)*init.factor.y)))

		screen.blit(font.render('MUSICA', True, (250,0,0)), ( 100*init.factor.x,self.ymove+(800*init.factor.y)))
                screen.blit(font.render('POR JL VERBENA', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((800+70)*init.factor.y)))   
                screen.blit(font.render('ERIC CISNEROS', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((800+(70*2))*init.factor.y)))
                screen.blit(font.render('Y SPORCO', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((800+(70*3))*init.factor.y)))

		screen.blit(font.render('PERSONAJES', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((1600)*init.factor.y)))
                screen.blit(font.render('POR JL VERBENA', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((1600+70)*init.factor.y)))
                screen.blit(font.render('KIKE', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((1600+(70*2))*init.factor.y)))
                screen.blit(font.render('Y ERIC CISNEROS', True, (250,0,0)), ( 100*init.factor.x,self.ymove+((1600+(70*3))*init.factor.y)))	
	


        def choose(self,play):
                global n

		if self.choosing:
                	if event.type == KEYDOWN and event.key == K_LEFT:
                        	if self.n ==1:
                                	self.n=3
                        	else:
                                	self.n -= 1
				self.choosing=False
                	elif event.type == KEYDOWN and event.key == K_RIGHT:
                        	if self.n==3:
                                	self.n =1
                        	else:
                                	self.n += 1
				self.choosing=False
                	else:
                        	pass
		else:
			pass
		
			if event.type == KEYUP and event.key == K_LEFT or \
			event.type == KEYUP and event.key == K_RIGHT:
				self.choosing=True		
		if event.type == KEYDOWN and event.key == K_SPACE:
			self.song.stop()
			self.level=False
			play.level+=1


                if self.n==1:
                        self.play='kike'
                if self.n==2:
                        self.play='monse'
                if self.n==3:
                        self.play='bebe'
		play.game_time = 0

					
		

	def display(self,screen,play):
		play=self.choose()
                screen.blit(play.image,(play.pos.x, play.pos.y))



