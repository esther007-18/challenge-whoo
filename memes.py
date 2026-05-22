import pygame
import random
import math

class Memes:
    def __init__(self, x_cord, y_cord, speed, angle):
        self.x_cord=x_cord
        self.y_cord=y_cord
        self.speed=speed
        self.image = pygame.image.load("shark.png").convert_alpha()
        self.speed=100
        self.angle=angle
        self.start_time=pygame.time.get_ticks()

        # angle from movement direction
        angle = math.degrees(math.atan2(-x_cord, y_cord))

    def pos(self, offset=0):

        elapsed = ((pygame.time.get_ticks() - self.start_time) / 1000) + offset

        new_x = self.x_cord + (self.speed * elapsed)
        new_y = self.y_cord +0.01*(self.speed * elapsed - 300) ** 2

        return new_x, new_y

    def draw (self, surface):
    
        #self.image = pygame.transform.rotate(self.image, self.angle)
        x, y = self.pos()

            # tiny future step
        future_x, future_y =self.pos(0.01)

            # movement direction
        dx = future_x - x
        dy = future_y - y

        angle = math.degrees(math.atan2(-dy, dx))

        rotated = pygame.transform.rotate(self.image, angle)

        # keep image centered
        rect = rotated.get_rect(center=(x, y))

        # draw
        surface.blit(rotated, rect)

        print (self.pos())

    def draw2(self,surface):
        self.start_time=pygame.time.get_ticks()

   
       

    