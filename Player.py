from Object import Object
from Motorcycle import Pop100
from ConfigMap import Configuration


class Player(Object):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = ""
        self.motorcycle = Pop100()
        self.frames = 0

    def update(self):
        self.frames += 1
        self.frames = self.frames/Configuration.fps
        self.motorcycle.update(self.frames)


