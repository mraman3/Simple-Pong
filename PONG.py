#PONG GAME
#Aman Braich
#May 7th, 2016

import pygame
import sys
pygame.init()
screenSize = (800,600)
displayScreen = pygame.display.set_mode((screenSize),0)
pygame.display.set_caption("U1A2 Test")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

displayScreen.fill(BLACK)
pygame.display.update()
#Paddle #1
plx1 = 15
ply1 = 190
dy1 = 0
#Paddle #2
plx2 = 775
ply2 = 475
dy2 = 0
#Both Paddles
Width = 10
Height = 125
#BALL
x = 400
y = 300
R = 10
#DIRECTION COMMANDS
dx = 5
dy = 5
#SCORE
PL1S = 0
PL2S = 0
fontTitle = pygame.font.SysFont("comicsansms", 50)
#LOOP EVENTS
stop = False
level = False
Start = False
main = False
playagain = False
#Game details
pong = pygame.font.SysFont("Arial", 80)
#Main loop
while not main:
    #START SCREEN LOOP
    while not Start:
        Title = pong.render("PONG", True, WHITE)
        pickstart = fontTitle.render("Press the SpaceBar to Start", True, WHITE)
        Quit = fontTitle.render("Click the X to close the game", True, WHITE)
        displayScreen.blit(Title,(300,50))
        displayScreen.blit(pickstart,(50,200))
        displayScreen.blit(Quit,(50,350))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Start = True
        pygame.display.update()
        displayScreen.fill(BLACK)
        
    #LEVEL SCREEN LOOP
    while not level:
        Level = fontTitle.render("Pick Level Difficulty", True, WHITE)
        Level1 = fontTitle.render("For Easy Press #1", True, WHITE)
        Level2 = fontTitle.render("For Medium Press #2", True, WHITE)
        Level3 = fontTitle.render("For Hard Press #3", True, WHITE)
        displayScreen.blit(Level,(175,50))
        displayScreen.blit(Level1,(175,150))
        displayScreen.blit(Level2,(175,250))
        displayScreen.blit(Level3,(175,350))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Height = 125
                    PL1S = 0
                    PL2S = 0
                    dx = 5
                    dy = 5
                    ply1 = 190
                    ply2 = 475
                    stop = False
                    level = True
                if event.key == pygame.K_2:
                    Height = 80
                    PL1S = 0
                    PL2S = 0
                    dx = 5
                    dy = 5
                    ply1 = 190
                    ply2 = 475
                    stop = False
                    level = True
                if event.key == pygame.K_3:
                    Height = 50
                    PL1S = 0
                    PL2S = 0
                    dx = 5
                    dy = 5
                    ply1 = 190
                    ply2 = 475
                    stop = False
                    level = True
        pygame.display.update()

    #GAME LOOP    
    while not stop:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy2 = -5
                elif event.key == pygame.K_DOWN:
                     dy2 = 5
                elif event.key == pygame.K_w:
                     dy1 = -5
                elif event.key == pygame.K_s:
                     dy1 = 5
                     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    dy2 = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    dy1 = 0

        oldply1 = ply1
        oldply2 = ply2
        
        displayScreen.fill(BLACK)
        #Game screen detials
        pygame.draw.rect(displayScreen, WHITE,(400,0,5,600), 0)
        #SCORE DISPLAY
        PLAYER1SCORE = fontTitle.render(str(PL1S), True, WHITE)
        displayScreen.blit(PLAYER1SCORE,(300,50))
        PLAYER2SCORE = fontTitle.render(str(PL2S), True, WHITE)
        displayScreen.blit(PLAYER2SCORE,(500,50))
        
        #Paddle #1
        ply1 = ply1 + dy1
        pygame.draw.rect(displayScreen, WHITE,(plx1,ply1,Width,Height), 0)
        #Paddle #2
        ply2 = ply2 + dy2
        pygame.draw.rect(displayScreen, WHITE,(plx2,ply2,Width,Height), 0)
        
        #PADDLE RESTRICTIONS
        if ply1>=(600-Height) or ply1<=0:
            ply1 = oldply1
        if ply2>=(600-Height) or ply2<=0:
            ply2 = oldply2
            
        #BALL
        pygame.draw.circle(displayScreen,WHITE,(x,y),R,0)
        y = y + dy
        x = x + dx
        
        #COLLISON DETECTION
        if y<=R:
            dy = -dy
        if (x+R)>=(plx2):
            if (y<=(ply2+Height)) and (y>=ply2):
                dx = -dx
            else:
                #SCORE UPDATE
                PL1S = PL1S+1
                x = 400
                y = 300
        #COLLISON DETECTION
        if y>=(600-R):
            dy = -dy
        if (x-R)<=(plx1+Width):
            if (y<=(ply1+Height)) and (y>=ply1):
                dx = -dx
            else:
                #SCORE UPDATE
                PL2S = PL2S+1
                #BALL RECENTER AFTER SCORE
                x = 400
                y = 300
        if PL1S == 11:
            dy = 0
            dx = 0
            displayScreen.fill(BLACK)
            WIN = "PLAYER 1 WINS!!!"
            stop = True
            playagain = False
        if PL2S == 11:
            dy = 0
            dx = 0
            displayScreen.fill(BLACK)
            WIN = "PLAYER 2 WINS!!!"           
            stop = True
            playagain = False

        pygame.display.update()
        pygame.time.delay(10)
        
    #Play Again
    while not playagain: 
        displayScreen.fill(BLACK)
        PL1WIN = fontTitle.render(WIN, True, WHITE)
        Replay = fontTitle.render("Do you want to play again ", True, WHITE)
        yes = fontTitle.render("Press Y to play again", True, WHITE)
        no = fontTitle.render("Press N to exit", True, WHITE)
        displayScreen.blit(Replay,(125,225))
        displayScreen.blit(yes,(125,325))
        displayScreen.blit(no,(125,425))
        displayScreen.blit(PL1WIN,(125,125))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    level = False
                    playagain = True
                    displayScreen.fill(BLACK)
                    pygame.display.update()
                elif event.key == pygame.K_n:
                    stop = True
                    main = True
                    pygame.quit()
                    sys.exit()
                        

pygame.quit()
sys.exit()
