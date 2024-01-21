
import pygame

texturesForBanana = pygame.image.load('Assets/banana.png')


class Banana:
    def __init__(self, x, y):
        self.x = x
        self.y = y - 0
        self.yStart = y
        self.wait = 0
        self.sprite = texturesForBanana

    def update(self, delta_time):

        if self.y > self.yStart + 100:
            self.wait += delta_time
            if self.wait > 20:
                self.y = self.yStart
                self.wait = 0

        else:
            self.y += delta_time

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))