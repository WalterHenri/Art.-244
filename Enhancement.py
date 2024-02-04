import pygame
from Object import Object
import abc
from enum import Enum


class TypeEnhancement(Enum):
    cactus = 1
    tree = 2


class Enhancement(Object, metaclass=abc.ABCMeta):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.is_animated = False
        self.width = 0

    @abc.abstractmethod
    def draw(self, screen, x, y, scale):
        pass

    @abc.abstractmethod
    def get_width(self):
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
        self.sprite = pygame.image.load("Assets/Tree_SpriteSheet_Outlined.png")
        self.sprite = self.sprite.subsurface((0, 40, 71, 88))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def draw(self, screen, x, y, scale):
        scale = scale / self.width
        x = x - ((self.width / 2) * scale)
        y = y - self.height
        scaled_sprite = pygame.transform.scale(self.sprite, (
            int(self.sprite.get_width() * scale), int(self.sprite.get_height() * scale)))
        screen.blit(scaled_sprite, (x, y))

    def get_width(self):
        return self.width
