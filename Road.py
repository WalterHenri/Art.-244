from Random import Random
import ConfigMap
from Utilities import Utilities
from Object import Object
from Enhancement import *


class Segment(Object):
    def __init__(self, x=0.0, y=0.0, z=0.0, length=200.0, width=2000.0, curve=0.0):
        super().__init__(x, y, z)
        self._length = length
        self._width = width
        self._curve = curve

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_curve(self):
        return self._curve

    def set_length(self, length):
        self._length = length

    def set_width(self, width):
        self._width = width

    def set_curve(self, curve):
        self._curve = curve


class Road:
    def __init__(self):
        self.segments = []
        self.enhancements = []
        self.en_index = []
        self.rng = Random()
        self.config = ConfigMap.Configuration
        self.n_laps = 3
        self.lap = 0

    def on_win(self, player):
        pass

    def get_length(self):
        return len(self.segments)

    def add_segment(self, n_enter: int, n_hold: int, n_leave: int, curve: float, hill: float):
        z = len(self.segments) * self.config.road_seg_len
        for i in range(n_enter):
            segment = Segment(0.0, Utilities.ease_in_out(0, hill, i / n_enter), z + i * self.config.road_seg_len,
                              self.config.road_seg_len, self.config.road_width, Utilities.ease_in(0, curve, i / n_enter))
            self.segments.append(segment)
        for i in range(n_enter, n_enter + n_hold):
            segment = Segment(0.0, hill, z + i * self.config.road_seg_len, self.config.road_seg_len,
                              self.config.road_width, curve)
            self.segments.append(segment)
        for i in range(n_enter + n_hold, n_enter + n_hold + n_leave):
            segment = Segment(0.0, Utilities.ease_in_out(hill, 0, (i - n_enter - n_hold) / n_leave),
                              z + i * self.config.road_seg_len, self.config.road_seg_len, self.config.road_width,
                              Utilities.ease_out(curve, 0, (i - n_enter - n_hold) / n_leave))
            self.segments.append(segment)

    def add_enhancement(self, type, x, y, z):
        if type == TypeEnhancement.tree:
            tree = Tree(x, y, z*ConfigMap.Configuration.road_seg_len)
            self.enhancements.append(tree)
            self.en_index[z].append(self.enhancements.__len__() - 1)
        elif type == TypeEnhancement.cactus:
            cactus = Cactus(x, y, z*ConfigMap.Configuration.road_seg_len)
            cactus.type = self.rng.rand_uint(0, 2)
            self.enhancements.append(cactus)
            self.en_index[z].append(self.enhancements.__len__() - 1)




    def random_road(self):
        n_segments = self.rng.rand_uint(self.config.road_segments_min, self.config.road_segments_max)
        for _ in range(n_segments):
            enter = self.rng.rand_uint(self.config.enter_length_min, self.config.enter_length_max)
            hold = self.rng.rand_uint(self.config.hold_length_min, self.config.hold_length_max)
            leave = self.rng.rand_uint(self.config.leave_length_min, self.config.leave_length_max)
            if self.rng.rand_uint(0, 1):
                curve = self.rng.rand_float(self.config.curve_min, self.config.curve_max)
            else:
                curve = 0.0
            if self.rng.rand_uint(0, 1):
                hill = self.config.road_seg_len * self.rng.rand_float(self.config.hill_min, self.config.hill_max)
            else:
                hill = 0.0
            self.add_segment(enter, hold, leave, curve, hill)

    def create_non_random_road(self):
        self.add_segment(3, 500, 20, 0, -60)
        self.add_segment(2, 4, 30, -5, 8)
        self.add_segment(100, 300, 40, 0, 60000)
        self.add_segment(200, 4, 30, 5, 4)
        self.add_segment(300, 500, 200, 10, -2000)
        self.add_segment(3, 50, 200, -10, -60)

        for i in range(self.segments.__len__()):
            self.en_index.append([])

        segPerTree = 24
        for i in range(50):
            if self.segments.__len__() > i*segPerTree:
                self.add_enhancement(TypeEnhancement.tree,self.config.road_width//1.5, self.segments[i*segPerTree].y, i * segPerTree)
                self.add_enhancement(TypeEnhancement.cactus,-self.config.road_width//1.5, self.segments[i*segPerTree].y, i * segPerTree)


    def __getitem__(self, i: int):
        return self.segments[i]

