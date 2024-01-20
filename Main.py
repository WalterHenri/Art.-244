import pygame
from Road import Road
from Road import Segment

pygame.init()

info = pygame.display.Info()

width = info.current_w/2
height = info.current_h/2

screen = pygame.display.set_mode((width, height))


color = (255, 240, 255)

texture = pygame.image.load('Assets/texture.png')

road = Road([Segment(0, 0, 0, 0, texture),Segment(1, 1, 1, 0.1, texture)])

while True:

    screen.fill((0, 0, 0))

    for segment in road.segments:
        segment.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
