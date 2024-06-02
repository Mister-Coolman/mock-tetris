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

playButton = button.Button(300, 350, pygame.image.load("./bmps/PlayButton.bmp"), 4)
settingsButton = button.Button(300, 500, pygame.image.load("./bmps/SettingsButton.bmp"), 4)
exitButton = button.Button(300, 500, pygame.image.load("./bmps/ExitButton.bmp"), 4)
backButton = button.Button(300, 150, pygame.image.load("./bmps/BackButton.bmp"), 4)
pauseButton = button.Button(25, 25, pygame.image.load("./bmps/PauseButton.bmp"), 3)
background = pygame.transform.scale_by(pygame.image.load("./bmps/Background.bmp"), 2.25)
logo = pygame.image.load("./bmps/Logo.bmp")
logo = pygame.transform.scale_by(logo, 8)
logo.set_colorkey((0,0,0))

menu = "main"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))
    
    keys = pygame.key.get_pressed()
    
    if menu == "main":
        screen.blit(logo, (136, 100))
        if playButton.draw(screen):
            menu = "tetris"
            #makes new tetris game
            game = Tetris(225, 50, 20, 10, 5)
        elif settingsButton.draw(screen):
            menu = "settings"
    
    elif menu == "tetris":
        #if keys[pygame.K_ESCAPE]:
        #    menu = "pause"
        #    continue
        if pauseButton.draw(screen):
            menu = "pause"
            continue
        
        if keys[pygame.K_w]:
            game.piece.rotateClockwise()
        if keys[pygame.K_s]:
            game.piece.rotateCounterclockwise()
        if keys[pygame.K_a]:
            game.piece.moveLeft()
        if keys[pygame.K_d]:
            game.piece.moveRight()
        if keys[pygame.K_SPACE]:
            game.piece.moveDown()
        
        if not game.gameEnd:
            game.update()

        game.render(screen)

    elif menu == "pause":
        #if keys[pygame.K_ESCAPE]:
        #    menu = "tetris"
        if exitButton.draw(screen):
            menu = "main"
            game = None
        elif backButton.draw(screen):
            menu = "tetris"
            
    elif menu == "settings":
        if keys[pygame.K_ESCAPE] or backButton.draw(screen):
            menu = "main"
    
    else:
        assert False

    pygame.display.flip()
    
    dt = clock.tick(60) / 1000
    
pygame.quit()
