import sys
import pygame
from Options import Options


class MenuInicial:
    def __init__(self):
        # Caminho para imagem
        script_directory = os.path.dirname(os.path.abspath(__file__))
        background_image_path = os.path.join(script_directory, "background.jpg")
        original_background = pygame.image.load(background_image_path)
        self.background_image = pygame.transform.scale(original_background, (self.width, self.height))
        # Cores
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 0)
        self.hover_color = self.yellow  # hover amarelo
        # Fontes
        self.font = pygame.font.Font(None, 45)
        # botões
        self.texts = ["Jogar", "Opções", "Sair", ]
        self.is_running = True

    def draw_text(self, text, x, y, color):
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)

    def main_loop(self, screen):
        while True:
            self.screen.blit(self.background_image, (0, 0))  # background
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Verifica se algum botão foi clicado
                    pos = pygame.mouse.get_pos()
                    if 300 < pos[0] < 500:
                        if 200 < pos[1] < 240:
                            return Options.Game_menu
                        elif 300 < pos[1] < 340:
                            return Options.Options_menu
                        elif 400 < pos[1] < 440:
                            pygame.quit()

            # Desenha os botões
            for i, text in enumerate(self.texts):
                color = self.hover_color if self.is_hovered(400, 200 + i * 60, text) else self.white
                self.draw_text(text, 400, 200 + i * 60, color)

            pygame.display.flip()

    def is_hovered(self, x, y, text):
        rect = self.font.render(text, True, self.white).get_rect(center=(x, y))
        return rect.collidepoint(pygame.mouse.get_pos())
