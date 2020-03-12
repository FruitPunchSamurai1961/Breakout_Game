import pygame


class Bar:
    def __init__(self):
        self.x = 600
        self.y = 700
        self.width = 100
        self.height = 30
        self.vel = 30
        self.color = (225, 0, 0)
        self.moving_right = False
        self.moving_left = False

    def draw_bar(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update_bar(self, screen_width):
        if self.moving_right and self.x < screen_width - self.width:
            self.x += self.vel
        elif self.moving_left and self.x > 0:
            self.x -= self.vel
