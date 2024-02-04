import pygame
from Object import Object
import abc


class Enhancement(Object, metaclass=abc.ABCMeta):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.is_animated = False

    @abc.abstractmethod
    def draw(self, screen, x, y, scale):
        pass


class Cactus(Enhancement):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.sprite = pygame.image.load("Assets/Cactus.png")

    def draw(self, screen, x, y, scale):
        scaled_sprite = pygame.transform.scale(self.sprite, (
         int(self.sprite.get_width() * scale), int(self.sprite.get_height() * scale)))
        screen.blit(scaled_sprite, (x, y))


class Tree(Enhancement):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.sprite = pygame.image.load("Assets/")

    def draw(self, screen, x, y, scale):
        scaled_sprite = pygame.transform.scale(self.sprite, (
            int(self.sprite.get_width() * scale), int(self.sprite.get_height() * scale)))
        screen.blit(scaled_sprite, (x, y))