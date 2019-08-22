# Pygame template - skeleton for a new pygame project
import pygame
import random




def template():
    WIDTH = 720
    HEIGHT = 1280
    FPS = 30

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # initial coordinates
    X_valRact=10
    y_valRact=10
    vel=5
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    xvelocitypv=False
    xvelocitynv=False
    yvelocitypv=False
    yvelocitynv=False
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
        screen.fill((BLACK))
        #GRIDLINES
        for i in range(10,HEIGHT,50):
            pygame.draw.line(screen,WHITE,[0,i],[WIDTH,i],1)
        for j in range(10,WIDTH,50):
            pygame.draw.line(screen,WHITE,[j,0],[j,HEIGHT],2)
        #MOVING THE OBJECT
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            xvelocitypv=False
            xvelocitynv=True
            yvelocitypv=False
            yvelocitynv=False
        if (keys[pygame.K_RIGHT] or keys[pygame.K_s]):
            xvelocitypv=True
            xvelocitynv=False
            yvelocitypv=False
            yvelocitynv=False
        if (keys[pygame.K_UP] or keys[pygame.K_w]):
            xvelocitypv=False
            xvelocitynv=False
            yvelocitypv=False
            yvelocitynv=True
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
            xvelocitypv=False
            xvelocitynv=False
            yvelocitypv=True
            yvelocitynv=False

        if xvelocitypv and X_valRact<WIDTH-50-10:
            X_valRact+=5

        if xvelocitynv and X_valRact>10:
            X_valRact-=5

        if yvelocitypv and y_valRact<HEIGHT-50-vel-5:
            y_valRact+=5

        if yvelocitynv and y_valRact>vel+5:
            y_valRact-=5
        #THE OBJECT
        pygame.draw.rect(screen, RED, (X_valRact,y_valRact,50,50))
        pygame.draw.circle(screen, BLUE, [X_valRact+75, y_valRact+25], 25)
        
        pygame.display.flip()

    pygame.quit()
template()