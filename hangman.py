import pygame
import random

class Hangman:
    def __init__(self, rope, col, size, pos,font):
        self.rope=rope
        self.col=col
        self.size=size
        self.pos=list(pos)
        self.font=font
        self.score=0
    def draw(self, surface):
        pygame.draw.line(surface, self.rope, (self.pos[0],0), (self.pos), 3)

        pygame.draw.circle(surface, self.col, (self.pos), self.size) 

        text = self.font.render(str(self.score), True, "White")
        surface.blit(text,(self.pos))

    def make_a_guess(self, answer):
        arty= random.randint((int(answer)-2), (int(answer)+1))
        if int(arty)==int(answer):
            self.score+=1
            self.m_up()
        else:
            self.score+=0
            self.m_down()
    
    def m_down(self):
        self.pos[1] += 10

    def m_up(self):
        self.pos[1] -= 10

    def make_a2nd_guess(self, answer, guess):
            if int(guess)==int(answer):
                self.score+=1
                self.m_up()
            else:
                self.score+=0
                self.m_down()

    