import math
from Object import Object


class Camera(Object):
    def __init__(self, x=0.0, y=0.0, z=0.0, fov=100.0):
        super().__init__(x, y, z)
        self.fov = fov
        self.d = 1 / math.tan(0.5 * fov * math.pi / 180)

    def get_fov(self):
        return self.fov

    def get_depth(self):
        return self.d

    def set_fov(self, fov):
        self.fov = fov
        self.d = 1 / math.tan(0.5 * fov * math.pi / 180)

    def project(self, seg, player, w, h):
        x_translated = seg.get_x() - self.x - player.get_x()
        y_translated = seg.get_y() - self.y
        z_translated = seg.get_z() - self.z + 1
        x_proj = x_translated * self.d / z_translated
        y_proj = y_translated * self.d / z_translated
        w_proj = seg.get_width() * self.d / z_translated
        x_screen = (w / 2) * (1 + x_proj)
        y_screen = (h / 2) * (1 - y_proj)
        w_screen = (w / 2) * w_proj
        return x_screen, y_screen, w_screen

    def project_en(self, seg, player, w, h):
        x_translated = seg.get_x() - self.x - player.get_x()
        y_translated = seg.get_y() - self.y
        z_translated = seg.get_z() - self.z + 1
        x_proj = x_translated * self.d / z_translated
        y_proj = y_translated * self.d / z_translated
        w_proj = seg.get_width() * self.d / z_translated
        x_screen = (w / 2) * (1 + x_proj)
        y_screen = y_proj
        w_screen = (w / 2) * w_proj
        return x_screen, y_screen, w_screen
