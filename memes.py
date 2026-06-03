import pygame
import math

class Memes:
    def __init__(self, x_cord, y_cord, speed, angle):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.speed = 700
        self.image = pygame.image.load("shark.png").convert_alpha()
        self.angle = angle

        self.font = pygame.font.SysFont(None, 72)

        self.start_time = None

    def jump(self):
        self.start_time = pygame.time.get_ticks()

    def pos(self, offset=0):

        if self.start_time is None:
            return self.x_cord, self.y_cord

        elapsed = ((pygame.time.get_ticks() - self.start_time) / 1000) + offset

        new_x = self.x_cord + (self.speed * elapsed)

        new_y = self.y_cord + (120 * elapsed - 60) ** 2 * 0.02

        return new_x, new_y

    def draw(self, surface, width):

        x, y = self.pos()

        future_x, future_y = self.pos(0.01)

        dx = future_x - x
        dy = future_y - y

        angle = math.degrees(math.atan2(-dy, dx))

        rotated = pygame.transform.rotate(self.image, angle)

        rect = rotated.get_rect(center=(x, y))

        surface.blit(rotated, rect)

        if self.start_time is not None:
            elapsed = ((pygame.time.get_ticks() - self.start_time) / 1000)

            if elapsed >= 5:
                text = self.font.render("GAME OVER!!!", True, "Black")

                surface.blit(
                    text,
                    ((width - text.get_width()) // 2, 150)
                )