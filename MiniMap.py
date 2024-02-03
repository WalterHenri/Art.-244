from Road import Road
from Player import Player
import pygame


class MiniMap:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.road = Road()
        self.player = Player()

    def set_road(self, road):
        self.road = road

    def update(self, player, screen):
        self.player.x = player.x
        self.player.y = player.y
        self.player.z = player.z
        self.draw(screen)

    def draw(self, screen):
        background = pygame.Rect(self.x, self.y, self.width * 2, self.height * 2)
        pygame.draw.rect(screen, (190, 190, 0), background)

        for segment in self.road.segments:
            scale_x = self.width/segment.get_width()
            scale_y = self.height/segment.get_length()
            draw_x = self.x + (segment.get_x() * scale_x)
            draw_y = self.y + (segment.get_z() * scale_y)
            seg_width = segment.get_width() * scale_x
            seg_height = segment.get_length() * scale_y
            rectangle_segment = pygame.Rect(draw_x, draw_y, seg_width, seg_height)
            pygame.draw.rect(screen, (120, 120, 120), rectangle_segment)

        player_x = self.x + (self.player.x * (self.width/screen.get_width()))
        player_y = self.y + (self.player.y * (self.height/screen.get_height()))
        pygame.draw.circle(screen, (0, 0, 0), (player_x, player_y), 5)


