###	main file for kikeGame

import pygame
from pygame.locals import *
from sys import exit, argv
from gameobjects.vector2 import Vector2
import random
from math import fabs
import time


from functions import *

#from variables import *
from objects import *
from enemies import *
#from screens import *

n=4
clock = pygame.time.Clock()





init=initial()


screenO=init.start()
screenb=pygame.display.set_mode(init.SCREEN_SIZE, FULLSCREEN, 32)
screen=Screen()

introScreen=IntroScreen(init)



bebe=Bebe(init)
jl=JLL(init)
kike=Kike(init)
monse=Monse(init)
ramon=Ramon(init)
cholo=Cholo(init)

player=monse
game_time=0


def intro_screen():
	global screenO, font3, init
	introScreen.song.play()
	if introScreen.play == "kike":
		kike.blit(screenO ,kike.image,kike.pos)
		player=kike
	elif introScreen.play == "monse":
		monse.blit(screenO ,monse.image,monse.pos)
		player=monse
	elif introScreen.play == "bebe":
                bebe.blit(screenO,bebe.image,bebe.pos)
		player=bebe
	screenO.blit(font3.render(introScreen.play,True,(0,0,0)),(800*init.factor.x,800*init.factor.y))
	return player
	



def im_beaten_enem(play,enem):
	if enem.health <= 0 and enem.health != -1000:
		enem.health=-1000		
		play.game_time =0
	if play.game_time <= 1500 and  enem.health ==-1000: 
		
		introScreen.bet.play()	
		play.health += .04 
		screenO.blit(pygame.transform.rotate(enem.image,-90),enem.pos)
	if  play.game_time >= 1500 and enem.health ==-1000:
		play.level +=1
		play.game_time =0
		enem.health=enem.h

#	play.game_time += time_passed	
	

def im_beaten_play(play, enem):
        if play.health < 0 and play.health != -1000:
                play.health=-1000
                play.game_time =0
        if play.game_time <= 1500 and  play.health ==-1000:		
                screenO.blit(pygame.transform.rotate(play.image,90),play.pos)
        if  play.game_time >= 1500 and play.health ==-1000:
                play.health = play.h
                introScreen.level = True
                play.game_time =0
		play.level=0
		enem.health=enem.h
		play.pos = Vector2(250,250)


#        play.game_time += time_passed
	

def the_game(play, enem):
	global screenO, init

	play.display_health(screenO,init)
        enem.display_health(screenO,init)
	screenO.blit(font3.render(play.name,True,play.color),(play.bar_pos.x,play.bar_pos.y+40))
	screenO.blit(font3.render(enem.name,True,(enem.color)),(enem.bar_pos.x,enem.bar_pos.y+40))


	if play.health > 0:
        	play.blit(screenO,play.image, play.pos)

	if enem.health > 0:
		enem.blit(screenO, enem.image, enem.pos)
		
		enem.song.play()		
	if play.game_time <= 1500 and enem.health > 0 and play.health > 0:
		
		screenO.blit(font3.render('VS',True,(0,0,0)),(800*init.factor.x,800*init.factor.y))	

        	enem.blit(screenO, enem.image, enem.pos)
	elif enem.health > 0 and play.health > 0:
	
        	play.move(init)
        	enem.move(init)
        	play.shoot(screenO,init)
        	enem.shoot(screenO,init)

        	enem.im_hit(play,screenO)
       		play.im_hit_left(enem,screenO)

		



	if enem.health < 0 or play.health < 0 :
		enem.bullet.gone()
		play.bullet.gone()
		enem.song.stop()
		im_beaten_enem(play,enem)
		im_beaten_play(play,enem)


		

	play.game_time += time_passed 




font3=pygame.font.SysFont("arial", int(60*init.factor.y))

while True:
	screen.start_screen()		

	screenO.fill((192,192,192))
	
	if introScreen.opening_bool :
		
		introScreen.opening(screenO,font3,init)
		introScreen.opening_song.play


	if introScreen.level:	

		introScreen.choose(player)
		player=intro_screen()

		

	elif player.level == 1:
		introScreen.song.stop() 
		the_game(player, cholo)


	elif player.level ==2:
		the_game(player, ramon)

	
	elif player.level ==3:
                the_game(player, jl)


	elif player.level ==4:
		screenO.blit(introScreen.end, (0,0))
		screenO.blit(player.image_win, (700*init.factor.x,200*init.factor.y))
		screenO.blit(font3.render('CAMPEON',True,player.color),(700*init.factor.x,800*init.factor.y))
		introScreen.closing(screenO,font3,init)
		introScreen.outro.play()

	#screenc=pygame.transform.scale(screenO, init.SCREEN_SIZE)
        #screenb.blit(screenc,(0,0))



#	screenO.blit(font3.render(str((dispInfo.current_w,dispInfo.current_h)),True,(0,0,0)),(100,800))
#	screenO.blit(font3.render(str(introScreen.level),True,(0,0,0)),(100,900))
#	screenO.blit(font3.render(str(introScreen.ymove),True,(0,0,0)),(100,1000))



	time_passed = clock.tick()
	pygame.display.update()	


	



	

