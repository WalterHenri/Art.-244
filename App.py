from RoadRender import RoadRender
import ConfigMap
import pygame
import os
from Motorcycle import Motorcycle


class App:
    def __init__(self):
        self.title = "Pseudo 3D"
        self.size = (ConfigMap.Configuration.width, ConfigMap.Configuration.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.title)
        self.running = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(os.path.join('fonts', 'arial.ttf'), 22)
        self.update_text = False
        self.text_surface = self.font.render("Initial text", True, (0, 0, 0, 150))
        self.FPS = ConfigMap.Configuration.fps
        self.road_render = RoadRender(self.screen)
        self.Motorcycle = Motorcycle(ConfigMap.Configuration.width/2, ConfigMap.Configuration.height/1.5,
                                     0,
                                     10, 1, 1)

    def is_running(self):
        return self.running

    def reset(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        self.Motorcycle.update(1)
        self.road_render.handle_events()

    def update(self):
        self.road_render.update()

        self.Motorcycle.draw(self.screen)
        if self.update_text:
            text_str = (f"Speed: {self.road_render.speed}\nDelta: {self.road_render.delta}\nFOV: "
                        f"{self.road_render.cam.fov}")
            self.text_surface = self.font.render(text_str, True, (0, 0, 0, 150))
            self.update_text = False

        self.screen.blit(self.text_surface, (0, 0))  # Draw the text

    @staticmethod
    def display():
        pygame.display.flip()  # Update the display

    def run(self):
        while self.is_running():
            self.handle_events()
            self.update()
            self.display()
            self.clock.tick(self.FPS)
