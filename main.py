import pygame
import button
from tetrisGame import *

pygame.init()

screen = pygame.display.set_mode((800, 720))
pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock()
running = True
dt = 0.0

#lastcalled = [0] * 6

das_start = 150
das_repeat = 50
msHeld = [0,0,0,0,0,0]
hasDas = [False,False,True,True,True,False]
tetris_controls = [pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d,pygame.K_SPACE,pygame.K_DOWN]
tetris_commands: list[callable]

FALL = pygame.USEREVENT + 1

pygame.time.set_timer(FALL, int(1 / (1 + 1.4 ** (1)) * 500*5))

game = None

pygame.mixer.music.load("./sounds/TetrisTheme.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

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
        if menu == "tetris":
            if not game.gameEnd:
                if event.type == FALL:
                    if (game.update() == 1):
                        pygame.time.set_timer(FALL, int(1 / (1 + 1.4 ** (game.level + 1)) * 500*5))
                """       
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        menu = "pause"
                        continue
                    if event.key == pygame.K_w:
                        if pygame.time.get_ticks() - lastcalled[0] > 150:
                            game.piece.rotateClockwise()
                            lastcalled[0] = pygame.time.get_ticks()
                    if event.key == pygame.K_s:
                        if pygame.time.get_ticks() - lastcalled[1] > 150:
                            game.piece.rotateCounterclockwise()
                            lastcalled[1] = pygame.time.get_ticks()
                    if event.key == pygame.K_a:
                        if pygame.time.get_ticks() - lastcalled[2] > 150:
                            game.piece.moveLeft()
                            lastcalled[2] = pygame.time.get_ticks()
                    if event.key == pygame.K_d:
                        if pygame.time.get_ticks() - lastcalled[3] > 150:
                            game.piece.moveRight()
                            lastcalled[3] = pygame.time.get_ticks()
                    if event.key == pygame.K_SPACE:
                        if pygame.time.get_ticks() - lastcalled[4] > 20:
                            game.piece.moveDown()
                            lastcalled[4] = pygame.time.get_ticks()
                    if event.key == pygame.K_DOWN:
                        if pygame.time.get_ticks() - lastcalled[5] > 100:
                            while game.piece.moveDown():
                                pass
                            if (game.update() == 1):
                                pygame.time.set_timer(FALL, int(1 / (1 + 1.4 ** (game.level + 1)) * 500*5))
                            lastcalled[5] = pygame.time.get_ticks()
                            """
            
    screen.fill((255, 255, 255))
    screen.blit(background, (0,0))

    pygame.key.set_repeat(1, 1)
    keys = pygame.key.get_pressed()
    
    if menu == "main":
        screen.blit(logo, (136, 100))
        if playButton.draw(screen):
            menu = "tetris"
            #makes new tetris game
            game = Tetris(225, 50, 20, 10)
            
            def harddrop():
                while game.piece.moveDown():
                    pass
                if game.update() == 1:
                    pygame.time.set_timer(FALL, int(1 / (1 + 1.4 ** (game.level + 1)) * 500*5))
                    
            tetris_commands = [
                (lambda : game.piece.rotateClockwise()),
                (lambda : game.piece.rotateCounterclockwise()),
                (lambda : game.piece.moveLeft()),
                (lambda : game.piece.moveRight()),
                (lambda : game.piece.moveDown()),
                harddrop
            ]
        elif settingsButton.draw(screen):
            menu = "settings"
    elif menu == "tetris":
        if pauseButton.draw(screen):
            menu = "pause"
            continue
            
        if not game.gameEnd:
            #process keys
            current_time = pygame.time.get_ticks()
            for i in range(len(tetris_controls)):
                if keys[tetris_controls[i]]:
                    if msHeld[i]:
                        msHeld[i] += dt*1000
                        if msHeld[i] >= das_start and hasDas[i]:
                            tetris_commands[i]()
                            msHeld[i] = das_start - das_repeat
                    else:
                        tetris_commands[i]()
                        msHeld[i] = dt*1000
                else:
                    msHeld[i] = 0
        else:
            #game ended
            if game.endAnimation > 0:
                game.board.board[game.endAnimation//10] = [game.endAnimation//10%(len(game.colors)-1)+1] * game.cols
                game.endAnimation -= 1
        
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
