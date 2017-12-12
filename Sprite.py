import pygame
class Sprite: 
	def __init__(self,x,y,lev): 
		self.x=x 
		self.y=y
		self.width=50 
  		self.height=50
  		if lev == 1:
                        self.i0 = pygame.image.load("Sprites/r.bmp")
                        self.i1 = pygame.image.load("Sprites/r.bmp")
                elif lev == 2:
                        self.i0 = pygame.image.load("Sprites/y.bmp")
                        self.i1 = pygame.image.load("Sprites/y.bmp")
                elif lev == 3:
                        self.i0 = pygame.image.load("Sprites/b.bmp")
                        self.i1 = pygame.image.load("Sprites/b.bmp")
                elif lev == 4:
                        self.i0 = pygame.image.load("Sprites/by.bmp")
                        self.i1 = pygame.image.load("Sprites/by.bmp")
                elif lev == 5:
                        self.i0 = pygame.image.load("Sprites/bb.bmp")
                        self.i1 = pygame.image.load("Sprites/bb.bmp")
                        
 
		self.timeTarget=10
		self.timeNum=0
		self.currentImage=0 
 	def update(self,window): 
		self.timeNum+=1
		if (self.timeNum==self.timeTarget): 
			if (self.currentImage==0):
				self.currentImage=1 
			else: 
				self.currentImage=0
			self.timeNum=0
		self.render(window) 
	def render(self,window):
		 if (self.currentImage==0):
			 window.blit(self.i0, (self.x,self.y))
		 else:
			 window.blit(self.i1, (self.x,self.y))
