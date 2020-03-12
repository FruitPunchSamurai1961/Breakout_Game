import pygame
import sys


def update_score(ball, bar, score):
    """This is check the score and increase it every time the bar and ball touch"""
    if bar.y <= ball.y <= (bar.y + bar.height):
        if ball.x <= bar.x < (ball.x + ball.radius) or bar.x <= ball.x < (bar.x + bar.width):
            score += 1
    return score


def check_events(bar):
    """This will be the main checker of user input and make the necessary adjustments to the bar"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                bar.moving_right = True
            elif event.key == pygame.K_LEFT:
                bar.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                bar.moving_right = False
            elif event.key == pygame.K_LEFT:
                bar.moving_left = False
