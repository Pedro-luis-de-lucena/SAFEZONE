import pygame
from player import Data
from support import import_folder
from settings import *
from player import Player

class P(Player):
	def __init__(self,groups,obstacle_sprites,network):
		super().__init__((2000,1430),groups,obstacle_sprites,network)

	
	def recv_data(self,data:Data):
		#imported information
		(x,y) = data.position
		self.pos2.x = x
		self.pos2.y = y  
		self.status = data.status
 
 
	def update(self):
    		#self.input()
		#self.move(self.speed)
		self.hitbox.x = self.pos2.x
		self.hitbox.y = self.pos2.y
		self.rect.center = self.hitbox.center
		self.animate()
		print(self.pos2)
	
