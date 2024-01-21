import random

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
    def __init__(self, speed, texture, screen_height):
        self.speed = speed
        self.texture = texture
        self.screen_height = screen_height
        self.segments = []

    def generate_road(self, screen_width, segment_width, num_segments):
        for i in range(num_segments):
            x = i * segment_width
            y = int(self.speed * i) + self.screen_height // 2
            inclination = random.uniform(-0.1, 0.1)
            segment = Segment(x, y, 0, inclination, self.texture, segment_width, segment_width)
            self.segments.append(segment)

    def update(self, speed, screen_width, segment_width, num_segments):
        self.speed = speed
        #self.generate_road(screen_width, segment_width, num_segments)

    def draw_road(self, screen):
        for segment in self.segments:
            segment.draw(screen)
