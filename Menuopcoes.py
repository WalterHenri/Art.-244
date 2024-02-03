import os
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN
from subprocess import call


class MainApp:
    def __init__(self):
        pygame.init()

        # Obtém as dimensões padrão da janela
        self.window_width = 800
        self.window_height = 600

        # Configuração da tela
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Interface Gráfica")

        # Obtenha o caminho completo do arquivo de imagem
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.image_path = os.path.join(current_directory, "Background.jpg")

        # Verifique se o arquivo existe
        if os.path.exists(self.image_path):
            # Abre a imagem com o Pygame
            original_image = pygame.image.load(self.image_path)

            # Redimensiona a imagem para as dimensões padrão da janela
            self.background_image = pygame.transform.scale(original_image, (self.window_width, self.window_height))

            # Adição de um clock para controlar a taxa de quadros
            self.clock = pygame.time.Clock()

            # Fonte para o texto
            self.font = pygame.font.Font(None, 36)

            # Opções para caixa de tamanho da tela
            self.tamanho_tela_combobox = pygame.Rect(self.window_width * 0.4, self.window_height * 0.2, 100, 40)
            self.tamanho_tela_values = {"Pequena": 1, "Média": 2, "Tela cheia": 3}
            self.tamanho_tela_selected = None

            # Opções para caixa de velocidade
            self.velocidade_combobox = pygame.Rect(self.window_width * 0.4, self.window_height * 0.3, 100, 40)
            self.velocidade_selected = None

            # Variáveis para controlar a exibição dos comboboxes
            self.show_tamanho_tela_combobox = False
            self.show_velocidade_combobox = False
            # Flag para indicar se o botão Tamanho da Tela está sendo pressionado
            self.tamanho_tela_button_pressed = False
            # Loop principal
            self.main_loop()
        else:
            print(f"Arquivo de imagem não encontrado: {self.image_path}")

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    return
                elif event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if 300 < pos[0] < 500:
                        if 200 < pos[1] < 240:
                            self.tamanho_tela_button_pressed = True
                        elif 300 < pos[1] < 340:
                            self.on_velocidade_click()
                        elif 400 < pos[1] < 440:
                            self.close_game()
                        elif 500 < pos[1] < 540:
                            self.on_tela_inicial_click()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.tamanho_tela_button_pressed = False
                    self.on_tamanho_tela_click()
            # Desenha a imagem de fundo
            self.screen.blit(self.background_image, (0, 0))

            # Desenha o texto "Configurações do Jogo"
            text_surface = self.font.render("Configurações do Jogo", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.window_width // 2, 50))
            self.screen.blit(text_surface, text_rect)

            # Desenha os botões
            self.draw_button("Tamanho da Tela", 0.2, 0.2, self.on_tamanho_tela_click)
            self.draw_button("Velocidade", 0.2, 0.3, self.on_velocidade_click)
            self.draw_button("Fechar Jogo", 0.8, 0.1, self.close_game)
            self.draw_button("Tela Inicial", 0.2, 0.9, self.on_tela_inicial_click)

            # Desenha caixas de opções se selecionadas
            if self.show_tamanho_tela_combobox:
                self.draw_combobox(self.tamanho_tela_combobox, self.tamanho_tela_values.keys())
            if self.show_velocidade_combobox:
                self.draw_combobox(self.velocidade_combobox, ["1.5", "2", "2.5", "3"])

            pygame.display.flip()
            self.clock.tick(60)  # Limita a taxa de quadros para 60 FPS

    def draw_button(self, text, relx, rely, callback):
        button = pygame.Rect(self.window_width * relx - 80, self.window_height * rely - 20, 160, 40)
        color = (100, 100, 100) if not self.is_hovered(button) else (150, 150, 150)

        pygame.draw.rect(self.screen, color, button)
        pygame.draw.rect(self.screen, (0, 0, 0), button, 2)

        button_text = self.font.render(text, True, (255, 255, 255))
        text_rect = button_text.get_rect(center=button.center)
        self.screen.blit(button_text, text_rect)

        if self.is_hovered(button):
            pygame.draw.rect(self.screen, (255, 255, 255), button, 2)

        if self.is_clicked(button):
            callback()

    def draw_combobox(self, rect, options):
        pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)

        pygame.draw.rect(self.screen, (100, 100, 100), rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2)

        if self.is_hovered(rect):
            pygame.draw.rect(self.screen, (255, 255, 255), rect, 2)

        if options:
            for i, option in enumerate(options):
                option_rect = pygame.Rect(rect.left, rect.bottom + 1 + i * 45, rect.width, 40)
                pygame.draw.rect(self.screen, (100, 100, 100), option_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), option_rect, 2)
                text_surface = self.font.render(option, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=option_rect.center)
                self.screen.blit(text_surface, text_rect)

                if self.is_hovered(option_rect):
                    pygame.draw.rect(self.screen, (255, 255, 255), option_rect, 2)

                if self.is_clicked(option_rect):
                    if rect == self.tamanho_tela_combobox:
                        self.tamanho_tela_selected = option
                        self.on_tamanho_tela_selected()
                        self.show_tamanho_tela_combobox = False
                    elif rect == self.velocidade_combobox:
                        self.velocidade_selected = option
                        self.on_velocidade_selected()
                        self.show_velocidade_combobox = False

    def is_hovered(self, rect):
        return rect.collidepoint(pygame.mouse.get_pos())

    def is_clicked(self, rect):
        return pygame.mouse.get_pressed()[0] and self.is_hovered(rect)

    def on_tamanho_tela_click(self):
        if not self.tamanho_tela_button_pressed:
            self.show_tamanho_tela_combobox = not self.show_tamanho_tela_combobox
        else:
            self.tamanho_tela_button_pressed = False
        if not self.show_tamanho_tela_combobox:
            self.tamanho_tela_combobox.width = 140
            self.tamanho_tela_combobox.height = 10

    def on_tamanho_tela_selected(self):
        print(f"Tamanho da Tela selecionado: {self.tamanho_tela_selected}")
        # Adicione lógica adicional conforme necessário

    def on_velocidade_click(self):
        self.show_velocidade_combobox = not self.show_velocidade_combobox
        if not self.show_velocidade_combobox:
            self.velocidade_combobox.width = 140
            self.velocidade_combobox.height = 10

    def on_velocidade_selected(self):
        print(f"Velocidade selecionada: {self.velocidade_selected}")
        # Adicione lógica adicional conforme necessário

    def close_game(self):
        pygame.quit()

    def on_tela_inicial_click(self):
        pygame.quit()
        call(["python", "Menuinicial.py"])


if __name__ == "__main__":
    app = MainApp()
