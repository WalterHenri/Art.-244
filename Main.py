import pygame
import AnimatedSprite
from Road import Road
from Road import Segment
from Motorcycle import Motorcycle

pygame.init()

info = pygame.display.Info()

width = info.current_w/2
height = info.current_h/2

screen = pygame.display.set_mode((width, height))


color = (10, 10, 255)

texture = pygame.image.load('Assets/texture.png')

road = Road(5, texture, height)

motorcycle = Motorcycle(width/2, height/2, 10, 10, 100, 1)
road.generate_road(800, 100, 10)


from Banana import Banana
# BAnAanaa
banana = Banana(width/2 , height/2- 50)


while True:

    screen.fill(color)

    road.draw_road(screen)

    road.update(10, 800, 100, 10)

    motorcycle.update(10)
    motorcycle.draw(screen)

    banana.update(0.2)
    banana.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
