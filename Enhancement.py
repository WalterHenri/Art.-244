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
        self.width = 1
        self.height = 1
        self.base_scale = 1

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
        self.sub_sprites = [self.sprite.subsurface(16, 42, 24, 48), self.sprite.subsurface(40, 42, 24, 48), self.sprite.subsurface(64, 42, 24, 48)]
        self.sprite = self.sub_sprites[0]
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.base_scale = 40
        self.type = 0

    def draw(self, screen, x, y, scale):
        self.sprite = self.sub_sprites[self.type]

        final_scale = self.base_scale * scale

        x = x - ((self.width / 2) * final_scale)
        y = y - self.height * final_scale
        scaled_sprite = pygame.transform.scale(self.sprite, (
            int(self.sprite.get_width() * final_scale), int(self.sprite.get_height() * final_scale)))
        screen.blit(scaled_sprite, (x, y))

    def get_width(self):
        return self.width


class Tree(Enhancement):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.sprite = pygame.image.load("Assets/Tree_SpriteSheet_Outlined.png").subsurface((0, 40, 71, 88))
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
        self.base_scale = 40

    def draw(self, screen, x, y, scale):
        final_scale = self.base_scale*scale

        x = x - ((self.width / 2) * final_scale)
        y = y - self.height*final_scale
        scaled_sprite = pygame.transform.scale(self.sprite, (
            int(self.sprite.get_width() * final_scale), int(self.sprite.get_height() * final_scale)))
        screen.blit(scaled_sprite, (x, y))

    def get_width(self):
        return self.width
