from RoadRender import RoadRender
import ConfigMap
import pygame
import os
from Motorcycle import Motorcycle
from Player import Player
from Menuinicial import MenuInicial


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = ConfigMap.Configuration.fps
        self.player = Player()
        self.Motorcycle = self.player.motorcycle
        self.road_render = RoadRender(self.screen, self.player)

    def is_running(self):
        return self.running

    def reset(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.player.update()
        self.road_render.handle_events()

    def update(self):
        self.road_render.update()
        self.Motorcycle.draw(self.screen)

    @staticmethod
    def display():
        pygame.display.flip()  # Update the display

    def run(self):
        while self.is_running():
            self.handle_events()
            self.update()
            self.display()
            self.clock.tick(self.FPS)
