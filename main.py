import pygame
import button
from tetrisGame import *

pygame.init()

screen = pygame.display.set_mode((800, 720))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()
running = True
dt = 0.0

game = None

playButton = button.Button(300, 500, pygame.image.load("./bmps/PlayButton.bmp"), 4)
background = pygame.transform.scale_by(pygame.image.load("./bmps/Background.bmp"), 2.25)

menu = "main"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    
    keys = pygame.key.get_pressed()
    
    if menu == "main":
        if (playButton.draw(screen)):
            menu = "tetris"
            #makes new tetris game
            game = Tetris(0, 0, 24, 10, 5)
    
    elif menu == "tetris":
        if keys[pygame.K_ESCAPE]:
            menu = "pause"
            continue
        game.update()

    elif menu == "pause":
        if keys[pygame.K_ESCAPE]:
            menu = "tetris"
            
    elif menu == "settings":
        pass
    
    else:
        assert(False)

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()
