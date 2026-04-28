import pygame
import sys
pygame.init()
from hangman import Hangman

pygame.mixer.init()
pygame.mixer.music.load("L_B_M.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.9)


screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
GREEN = (0, 0, 255)
hane= Hangman("dodgerblue4", "firebrick3", 70, (427, 400))
hane2= Hangman("green", "dodgerblue4", 70, (853, 400))
image=pygame.image.load("ytube.png")
game_started = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()

        elif event.type ==pygame.MOUSEBUTTONDOWN:
            x,y= event.pos
            game_started=True
            print(x,y)
    screen.fill("pink")
   
    if game_started != True:
        screen.blit(image, (350,150))
    else:  
        hane.draw(screen)
        hane2.draw(screen)
    pygame.display.flip()

    clock.tick(60)


