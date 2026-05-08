import pygame
import random
import math

class Memes:
    width=input()
    def __init__(self, image, wid, y, speed):
        self.image= random.choice("jj")
        self.wid(0, WIDTH - self.image.width())
        self.y=random.randit(-600, -200)
        self.speed=random.randit(4,9)

    def update(self):
        self.y+=self.speed

    def draw (self, surface):
        surface.blit(self.image, (self.wid,self.y))