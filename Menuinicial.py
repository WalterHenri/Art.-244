import pygame
from Game import Game
from Garage import Garage
from ConfigMap import Configuration


class MenuInicial:
    def __init__(self,screen):
        self.width = Configuration.width
        self.height = Configuration.height
        original_background = pygame.image.load("Assets/garage_background.jpg")
        self.background_image = pygame.transform.scale(original_background, (self.width, self.height))
        # Cores
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.hover_color = self.yellow  # hover amarelo
        # Fontes
        self.font = pygame.font.Font(None, 45)
        # botões
        self.texts = ["Jogar", "Opções", "Sair", ]
        self.screen = screen
        self.is_running = True

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def main_loop(self):
        option = 0
        while self.is_running:
            self.screen.blit(self.background_image, (0, 0))  # background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Verifica se algum botão foi clicado
                    pos = pygame.mouse.get_pos()
                    if 300 < pos[0] < 500:
                        if 200 < pos[1] < 240:
                            option = 0
                            self.is_running = False
                        elif 300 < pos[1] < 340:
                            option = 1
                            self.is_running = False
                        elif 400 < pos[1] < 440:
                            pygame.quit()

            # Desenha os botões
            for i, text in enumerate(self.texts):
                color = self.hover_color if self.is_hovered(400, 200 + i * 60, text) else self.white
                self.draw_text(text, 400, 200 + i * 60, color)

            pygame.display.flip()
        if option == 0:
            self.run_game()
        elif option == 1:
            self.run_garage()

    def run_game(self):
        game = Game(self.screen)
        game.run()

    def run_garage(self):
        garage = Garage(self.screen, width=self.width, height=self.height)
        garage.main_loop()

    def is_hovered(self, x, y, text):
        rect = self.font.render(text, True, self.white).get_rect(center=(x, y))
        return rect.collidepoint(pygame.mouse.get_pos())
