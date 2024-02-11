import pygame
from Menuinicial import MenuInicial
from Garage import Garage
from Game import Game
from Options import Options
from ConfigMap import Configuration

class App:
    def __init__(self):

        self.title = "Art. 244"
        self.size = (Configuration.width, Configuration.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.menu = MenuInicial(self.screen)
        self.is_running = True

    def run(self):
        self.menu.main_loop()


