import pygame


class Segment:
    def __init__(self, x, y, z, inclination, texture, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.inclination = inclination
        self.texture = texture
        self.width = width
        self.height = height
        self.texture = texture.subsurface(pygame.Rect(0, 0, width, height))

    def draw(self, screen):
        screen.blit(self.texture, (self.x, self.y))


class Road:
    def __init__(self, segments):
        self.segments = segments
