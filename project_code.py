import pygame
import sys
pygame.init()
from hangman import Hangman
from triv_ques import Trivia

pygame.mixer.init()
pygame.mixer.music.load("L_B_M.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.9)


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Textbox Example")
input_box = pygame.Rect(550, 500, 250, 70)
active = False
text = ""
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y= event.pos
            game_started=True
            if input_box.collidepoint(event.pos):
                active = True
            
            else:
                active = False
        elif event.type == pygame.KEYDOWN and active:
            if pygame.K_0<= event.key <=pygame.K_9:
                text += str(event.key)
                print(text)
            if event.key == pygame.K_RETURN:
                print("Answer:", text)
                text = ""
        
    screen.fill("pink")
   
    if game_started != True:
        screen.blit(image, (350,150))
    else:  
        hane.draw(screen)
        hane2.draw(screen)
    if active:
        pygame.draw.rect(screen, "White", input_box)
    else:
        pygame.draw.rect(screen, "Red", input_box)


    pygame.display.flip()
    font = pygame.font.Font(None, 25)

    clock.tick(60)


