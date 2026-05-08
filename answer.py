import pygame

class Input:
    def __init__(self, input_box, font):
        self.entered_word = ""
        self.input_box=input_box
        self.active2=False
        self.font=font


    def draw(self, surface):
        if self.active2: 
            pygame.draw.rect(surface, "White", self.input_box)

        else:
            pygame.draw.rect(surface, "Red", self.input_box)

            # make it so it draws the number
        text = self.font.render(self.entered_word, True, "Black")

        surface.blit(text,(self.input_box.x + 5, self.input_box.y + 5) )

    def collidepoint(self, pos):
        return self.input_box.collidepoint(pos)