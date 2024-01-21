import pygame


class Quad:
    def __init__(self, x1=0.0, x2=0.0, y1=0.0, y2=0.0, w1=0.0, w2=0.0, color=(255, 255, 255)):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.w1 = w1
        self.w2 = w2
        self.color = color

    def draw(self, surface):
        points = [(self.x1 - self.w1 / 2, self.y1), (self.x2 - self.w2 / 2, self.y2),
                  (self.x2 + self.w2 / 2, self.y2), (self.x1 + self.w1 / 2, self.y1)]
        pygame.draw.polygon(surface, self.color, points)

    def get_x1(self):
        return self.x1

    def get_x2(self):
        return self.x2

    def get_y1(self):
        return self.y1

    def get_y2(self):
        return self.y2

    def get_w1(self):
        return self.w1

    def get_w2(self):
        return self.w2

    def get_color(self):
        return self.color

    def set_xyw_color(self, x1, x2, y1, y2, w1, w2, color):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.w1 = w1
        self.w2 = w2
        self.color = color

    def set_xyw(self, x1, x2, y1, y2, w1, w2):
        self.set_xyw_color(x1, x2, y1, y2, w1, w2, self.color)

    def set_x1(self, x1):
        self.x1 = x1

    def set_x2(self, x2):
        self.x2 = x2

    def set_y1(self, y1):
        self.y1 = y1

    def set_y2(self, y2):
        self.y2 = y2

    def set_w1(self, w1):
        self.w1 = w1

    def set_w2(self, w2):
        self.w2 = w2



