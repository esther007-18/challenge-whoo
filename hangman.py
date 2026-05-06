import pygame

class Hangman:
    def __init__(self, rope, col, size, pos):
        self.rope=rope
        self.col=col
        self.size=size
        self.pos=pos
        self.score=0
    def draw(self, surface):
        pygame.draw.line(surface, self.rope, (self.pos[0],0), (self.pos), 3)

        pygame.draw.circle(surface, self.col, (self.pos), self.size) 
    
    