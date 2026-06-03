import pygame
import sys

pygame.init()

from hangman import Hangman
from triv_ques import Trivia
from answer import Input
from memes import Memes

pygame.mixer.init()
pygame.mixer.music.load("L_B_M.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.9)

W_S = 1280, 650
screen = pygame.display.set_mode(W_S)

pygame.display.set_caption("Textbox Example")

clock = pygame.time.Clock()
running = True

image = pygame.image.load("ytube.png")

image2 = pygame.image.load("scary background.jpg")
image2 = pygame.transform.scale(image2, W_S)


def reset_game():
    global hane, hane2, input_box, question2_0, shark
    global shark_jump, game_started

    hane = Hangman("dodgerblue4","firebrick3",70,(427, 400),pygame.font.Font(None, 25),"clipart2.png")

    hane2 = Hangman("green","dodgerblue4",70,(853, 400),pygame.font.Font(None, 25),"clipart.png")

    input_box = Input(pygame.Rect(550, 500, 250, 70),pygame.font.Font(None, 25))

    question2_0 = Trivia("trivia.txt",pygame.font.Font(None, 50))

    shark = Memes(0, 500, 2, 350)

    shark_jump = False
    game_started = False


reset_game()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.mixer.music.stop()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_started = True

            if input_box.collidepoint(event.pos):
                input_box.active2 = True
            else:
                input_box.active2 = False

        elif event.type == pygame.KEYDOWN:

            # Restart game after game over
            if shark_jump and event.key == pygame.K_r:
                reset_game()
                continue

            if input_box.active2:

                if pygame.K_0 <= event.key <= pygame.K_9:
                    if len(input_box.entered_word) <= 9:
                        input_box.entered_word += str(
                            event.key - pygame.K_0
                        )

                if event.key == pygame.K_RETURN:
                    if input_box.entered_word=="":
                        pass
                    else:
                        hane2.make_a_guess(
                        int(question2_0.answer)
                        )

                        hane.make_a2nd_guess(
                            int(question2_0.answer),
                            input_box.entered_word
                        )

                        input_box.entered_word = ""

                        question2_0.get_next_QnA()

                if event.key == pygame.K_BACKSPACE:
                    input_box.entered_word = (
                        input_box.entered_word[:-1]
                    )

    if not shark_jump:

        if hane.pos[1] >= 592 or hane2.pos[1] >= 592:
            shark.jump()
            shark_jump = True

    screen.blit(image2, (0, 0))

    if not game_started:

        screen.blit(image, (350, 150))

    else:

        hane.draw(screen)
        hane2.draw(screen)

        question2_0.draw(screen, 1280)

        input_box.draw(screen)

        shark.draw(screen, W_S[0])

    if shark_jump:

        game_over_font = pygame.font.Font(None, 90)
        restart_font = pygame.font.Font(None, 50)

        game_over_text = game_over_font.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )

        restart_text = restart_font.render(
            "Press R to Restart",
            True,
            (255, 255, 255)
        )

        screen.blit(restart_text, (450, 340))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()