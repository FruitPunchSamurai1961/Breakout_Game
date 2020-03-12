import random
import pygame

"""This is the ball class that we will add functions to such as moving it."""


class Ball:

    def __init__(self, screen_width, bar):
        """Most of this could have gone into anther settings file, but I felt that keeping it like this would help me
        better as I code this. """
        self.x = random.randint(1, screen_width) # the use of random is to set the ball onto a random part of the
        # screen when it starts out
        self.y = random.randint(1, bar.y)
        self.color = (0, 225, 0)
        self.radius = 15
        self.x_speed = 10
        self.y_speed = 10

    def draw_ball(self, screen):
        """This will be the fucntion that will draw the ball itself"""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update_ball(self, screen_width):
        """This will update the ball's location every frame"""
        self.x -= self.x_speed
        self.y -= self.y_speed
        if self.x <= self.radius or self.x >= (screen_width - self.radius - 5):
            self.x_speed = -self.x_speed
        elif self.y <= self.radius:
            self.y_speed = -self.y_speed

    def check_for_collision(self, bar):
        """This function will check for collision of the ball with the bar"""
        if bar.y <= self.y <= (bar.y + bar.height):
            if self.x <= bar.x < (self.x + self.radius) or bar.x <= self.x < (bar.x + bar.width):
                self.y_speed = -self.y_speed
