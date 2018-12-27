import pygame
import random


pygame.init()
white = (255,255,255)
width = 800
height = 600
#Defining the Player1 sprite or class
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def update(self):
        self.speedy = 0
        events = pygame.key.get_pressed()
        if events[pygame.K_DOWN]:
            self.speedy = 10
        if events[pygame.K_UP]:
            self.speedy = -10
        self.rect.y += self.speedy
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0
#Defining th Player2 sprite
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = 790
        self.rect.y = 0
    def update(self):
        self.speedy = 0
        events = pygame.key.get_pressed()
        if events[pygame.K_s]:
            self.speedy = 10
        if events[pygame.K_w]:
            self.speedy = -10
        self.rect.y += self.speedy
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0
#Definning the Ball sprite or class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,random.randint(0,height))
        self.speedx = random.choice([-5,5])
        self.speedy = random.choice([-5,5])
        self.score1 = 0
        self.score2 = 0
        self.increase = 0
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.speedy = random.randrange(3,5)
        if self.rect.bottom > height:
            self.speedy = random.randrange(-5,-3)
        if self.rect.left > width:
            self.rect.center = (width/2,random.randint(0,height))
            self.speedx = random.choice([-5,5])
            self.speedy = random.choice([-5,5])
            self.score1+=1
        if self.rect.right < 0:
            self.rect.center = (width/2,random.randint(0,height))
            self.speedx = random.choice([-5,5])
            self.speedy = random.choice([-5,5])
            self.score2+=1
        if self.increase > 5:
            self.speedx += 2
            self.increase = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
