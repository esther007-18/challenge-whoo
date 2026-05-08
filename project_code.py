import pygame
import sys
pygame.init()
from hangman import Hangman
from triv_ques import Trivia
from answer import Input

pygame.mixer.init()
pygame.mixer.music.load("L_B_M.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.9)


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Textbox Example")
active = False
text = ""
clock = pygame.time.Clock()
running = True
WHITE = (255, 255, 255)
GREEN = (0, 0, 255)
hane= Hangman("dodgerblue4", "firebrick3", 70, (427, 400))
hane2= Hangman("green", "dodgerblue4", 70, (853, 400))
input_box=Input(pygame.Rect(550, 500, 250, 70), pygame.font.Font(None, 25))
question2_0=Trivia("trivia.txt", pygame.font.Font(None, 25))
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
                input_box.active2 = True
            
            else:
                input_box.active2 = False
        elif event.type == pygame.KEYDOWN and input_box.active2:
            if pygame.K_0<= event.key <=pygame.K_9:
                input_box.entered_word += str(event.key-pygame.K_0)
                print(input_box.entered_word)
            if event.key == pygame.K_RETURN:
                input_box.entered_word = ""
        
    screen.fill("pink")
   
    if game_started != True:
        screen.blit(image, (350,150))
    else:  
        hane.draw(screen)
        hane2.draw(screen)

    input_box.draw(screen)
    question2_0.draw(screen, 1280)
    pygame.display.flip()
    clock.tick(60)


