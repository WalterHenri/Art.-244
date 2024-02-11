import pygame
from Menuinicial import MenuInicial
from Garage import Garage
from Game import Game
from Options import Options


class App:
    def __init__(self):
        pygame.init()
        self.menu = MenuInicial()
        self.garagem = Garage()
        self.Game = Game()
        self.title = "Art. 244"
        self.size = (ConfigMap.Configuration.width, ConfigMap.Configuration.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.currentScreen = 0

    def run(self):
        if self.currentScreen == Options.Start_menu:
            self.currentScreen = self.menu.main_loop(self.screen)
        elif self.currentScreen == Options.Garage_menu:
            self.currentScreen = self.garagem.main_loop(self.screen)
        elif self.currentScreen == Options.Game_menu:
            self.currentScreen = self.Game.Run()

