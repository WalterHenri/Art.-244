from Object import Object
from Motorcycle import Motorcycle
from Motorcycle import Pop100


class Player(Object):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = ""
        self.motorcycle = Pop100()

    def update(self):
        pass


