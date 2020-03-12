import pygame
from bar import Bar
from ball import Ball
import game_functions as gf

"""This file will function as the main driver for the game It will get functions and init other classes """


def run_game():
    pygame.init()
    pygame.font.init()

    """This sets the score color and establishes the font of the score text"""
    score_color = (255, 255, 0)
    my_font = pygame.font.SysFont('Comic Sans MS', 30)

    """This sets the screen settings and also makes objects from the two class files that represent the ball and the 
    bar. """
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong Game")
    clock = pygame.time.Clock()
    bar = Bar()
    ball = Ball(screen_width, bar)
    score = 0

    """This is the main loop that makes sure that the game runs and updates many of the ongoing things we need the 
    player to see such as the position of the ball. """
    while True:
        clock.tick(30)  # set fps
        screen.fill(
            (0, 0, 0))  # we need this so that the screen is reset and does not overlap with the pervious frames.

        score = gf.update_score(ball, bar, score) # this updates the score
        text_displayed = "Score: " + str(score) # this is what needs to show on the screen
        text_surface = my_font.render(text_displayed, False, score_color) # this establishes the score test and also what the color of it should be
        screen.blit(text_surface, (screen_width - 200, screen_height - 50)) # this sets the score onto the screen

        ball.draw_ball(screen) # this draws the ball onto the screen
        bar.draw_bar(screen) # draws the ball onto the screen
        gf.check_events(bar) # checks user input such as pressing right key
        bar.update_bar(screen_width) # updates the bar's position based on the user input
        ball.update_ball(screen_width) # updates the ball's position every frame

        ball.check_for_collision(bar) # sees if the ball is colliding with anything and makes changes to its velocity respectively

        pygame.display.update()


run_game()
