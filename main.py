'''
A simple ping pong game made with Pygame, taken from NeuralNine: https://www.youtube.com/watch?v=HNCAi0sjAz8&ab_channel=NeuralNine
'''

from turtle import Screen
import pygame


# Variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 800

pygame.init()
font = pygame.font.Font('./font.ttf', 40)

latency = 30

player_speed = 20

paddle_width = 10
paddle_height = 100

p1_x_pos = WIDTH - paddle_width - 10
p1_y_pos = HEIGHT / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = WIDTH / 2
ball_y_pos = HEIGHT / 2
ball_width = 8
ball_x_vel = -10

Screen = pygame.display.set_mode((WIDTH, HEIGHT))

#drawing objects
