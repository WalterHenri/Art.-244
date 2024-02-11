import pygame

class Motoca:
    def __init__(self, nome, marca, cilindradas, freio, aceleracao, path_image_mark, path_image_view):
        self.nome = nome
        self.marca = marca
        self.cilindradas = cilindradas
        self.freio = freio
        self.aceleracao = aceleracao
        self.path_image_mark = path_image_mark
        self.path_image_view = path_image_view

class ImageButton:
    def __init__(self, x, y, image_path):
        self.rect = pygame.Rect(x, y, 21, 21)
        self.image = pygame.image.load(image_path)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class Garage:
    def __init__(self,screen, width, height):
        self.is_running = True
        self.vetor_motos = [
            Motoca("Moto de alcides", "Marca1", "500cc", "ABS", "0-60 mph in 3.5s", "./Assets/logo_bmw.png", "./Assets/bmw.jpg"),
            Motoca("popi cem", "Marca1", "500cc", "ABS", "0-60 mph in 3.5s", "./Assets/logo_honda.png", "./Assets/pop100.png"),
            Motoca("xre 300 cabeçote trincado", "Marca1", "500cc", "ABS", "0-60 mph in 3.5s", "./Assets/logo_honda.png","./Assets/xre300.png"),
            Motoca("monark rebaixada", "Marca1", "500cc", "ABS", "0-60 mph in 3.5s", "./Assets/logo_monark.png ", "./Assets/monark.jpg"),
        ]
        self.indice = 0
        self.screen = screen
        self.WIDTH = width
        self.HEIGHT = height
        self.background = pygame.image.load("./assets/garage_background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load("./assets/logo.png")
        self.font_path = "./fonts/helvetica.otf"
        self.font_helvetica = pygame.font.Font(self.font_path, 24)

        self.button1 = ImageButton(125, 105, "./assets/arrow_left.png")
        self.button2 = ImageButton(self.WIDTH - 150, 105, "./assets/arrow_right.png")

    def draw_rounded_rectangle(self, surface, color, rect, radius, opacity, gradient_color, border_color, border_width, image_path):
        rect = pygame.Rect(rect)
        alpha_color = color[:3] + (int(opacity * 255),)

        shape_surf = pygame.Surface(rect.size, pygame.SRCALPHA)

        pygame.draw.rect(shape_surf, alpha_color, shape_surf.get_rect(), border_radius=radius)

        if gradient_color:
            gradient = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(gradient, gradient_color[0], gradient.get_rect(), border_radius=radius)
            shape_surf.blit(gradient, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

        if border_color and border_width > 0:
            pygame.draw.rect(shape_surf, border_color, shape_surf.get_rect(), border_radius=radius, width=border_width)

        if image_path:
            image = pygame.image.load(image_path)
            shape_surf.blit(image, ((rect.width - image.get_width()) // 2, (rect.height - image.get_height()) // 2))

        surface.blit(shape_surf, rect.topleft)

    def draw_text(self, text, position, color, font_size):
        text_surface = self.font_helvetica.render(text, True, color)
        self.screen.blit(text_surface, position)

    def draw_text_center(self, text, y, color, font_size):
        text_surface = self.font_helvetica.render(text, True, color)
        text_rect = text_surface.get_rect(center=(self.WIDTH//2, y))
        self.screen.blit(text_surface, text_rect)

    def rgb(self, hex_color):
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


    def draw_image(self, surface, image_path, max_dimensions, position):
        if image_path:
            image = pygame.image.load(image_path)

            image_width, image_height = image.get_size()

            max_width, max_height = max_dimensions
            aspect_ratio = image_width / image_height

            if image_width > max_width:
                new_width = max_width
                new_height = int(new_width / aspect_ratio)
            elif image_height > max_height:
                new_height = max_height
                new_width = int(new_height * aspect_ratio)
            else:
                new_width, new_height = image_width, image_height

            image = pygame.transform.scale(image, (new_width, new_height))

            x, y = position
            image_position = (x - new_width // 2, y - new_height // 2)

            surface.blit(image, image_position)

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.button1.is_clicked(pos):
                    self.indice -= 1
                    if self.indice < 0:
                        self.indice = len(self.vetor_motos) - 1

                elif self.button2.is_clicked(pos):
                    self.indice += 1
                    if self.indice > len(self.vetor_motos) - 1:
                        self.indice = 0

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                elif event.key == pygame.K_LEFT:
                    self.indice -= 1
                    if self.indice < 0:
                        self.indice = len(self.vetor_motos) - 1
                elif event.key == pygame.K_RIGHT:
                    self.indice += 1
                    if self.indice > len(self.vetor_motos) - 1:
                        self.indice = 0

        self.screen.blit(self.background, (0, 0))

        self.draw_rounded_rectangle(self.screen, (0, 0, 0), ((self.WIDTH - 580) / 2, 28, 580, 150), 10, 0.7, None, None, 0, None)
        self.draw_rounded_rectangle(self.screen, (255, 255, 255), ((self.WIDTH - 562) / 2, 77, 562, 7), 10, 0.6, None, None, 0, None)
        self.draw_rounded_rectangle(self.screen, (255, 255, 255), ((self.WIDTH - 562) / 2, 89, 562, 60), 10, 0.6, None, None, 0, None)
        self.draw_rounded_rectangle(self.screen, (0, 0, 0), ((self.WIDTH - 120) / 2, 89, 120, 60), 10, 0.7, (self.rgb("2b2b2b"), self.rgb("777777")), (110, 202, 103), 3, self.vetor_motos[self.indice].path_image_mark)
        self.draw_text("Oficina du grau", (530, 43), (110, 202, 103), 36)
        self.button1.draw(self.screen)
        self.button2.draw(self.screen)
        self.draw_text_center(self.vetor_motos[self.indice].nome, 165, (110, 202, 103), 36)
        self.draw_image(self.screen, self.vetor_motos[self.indice].path_image_view, (400, 270), ((self.WIDTH//2), (self.HEIGHT//2) + 50))
        self.screen.blit(self.image, (0, 0))

        pygame.display.flip()

    @staticmethod
    def quit_game():
        pygame.quit()

    def main_loop(self):
        while self.is_running:
            self.draw()
