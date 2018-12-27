import pygame
import random
from sprites import *

# Initializing pygame and variables
pygame.init()
pygame.font.init()
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
white = (255,255,255)
black = (0,0,0)
#Creating sprite objects and groups
Player1 = Player1()
Player2 = Player2()
ball = Ball()
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.GroupSingle()
all_sprites.add(Player1)
all_sprites.add(Player2)
balls.add(ball)

clock = pygame.time.Clock()
#Defining the start screen before playing the game
def menu_screen():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    
        logofont = pygame.font.SysFont('Comic Sans MS', 100)
        gamelogo = logofont.render('Pong!',True,white)
        startfont = pygame.font.SysFont('Comic Sans MS', 50)
        start = startfont.render('Press space to start',True,white)
        screen.blit(gamelogo,((width/2)-100,(height/2)-50))
        screen.blit(start,((width/2)-150,(height/2)+50))
        pygame.display.update()
        clock.tick(15)
#Pause function for when a player pauses the game
def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
        screen.fill(black)
        pausefont = pygame.font.SysFont('Comic Sans MS', 50)
        pausetext = pausefont.render('To resume game press space',True,white)
        screen.blit(pausetext,((width/2)-175,(height/2)-50))
        pygame.display.update()
        clock.tick(15)
#Game over screen for when a player reaches ten and wins the game
def game_over(Player):
    over = False
    while not over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    over = True
        overfont = pygame.font.SysFont('Comic Sans MS', 50)
        overtext = overfont.render('{} won the game'.format(Player), True, white)
        replaytext = overfont.render('Press space to play again',True,white)
        screen.fill(black)
        screen.blit(overtext, ((width/2)-128,(height/2)-50))
        screen.blit(replaytext,((width/2)-175,(height/2)+50))
        pygame.display.update()
        clock.tick(15)
    game_loop()
#Game loop to control the whole game
def game_loop():
    #defining the score board display
    font = pygame.font.SysFont('Comic Sans MS', 50)
    def score(s1,s2):
        score_player1 = font.render(str(s1),True,white)
        score_player2 = font.render(str(s2),True,white)
        screen.blit(score_player1,(100,0))
        screen.blit(score_player2,(700,0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause()
                
        all_sprites.update()
        balls.update()
        screen.fill(black)
        pygame.draw.line(screen,white,(width/2,0),(width/2,height))
        #detecting collisions between the ball and the players
        hits = pygame.sprite.spritecollide(ball,all_sprites,False)
        if Player1 in hits:
            ball.speedx = 5
            ball.increase +=1
        if Player2 in hits:
            ball.speedx = -5
            ball.increase += 1
        if ball.score1 == 10:
            game_over('Player1')
        if ball.score2 == 10:
            game_over('Player2')
        all_sprites.draw(screen)
        balls.draw(screen)
        score(ball.score1,ball.score2)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
if __name__ == '__main__':
    menu_screen()
    game_loop()
