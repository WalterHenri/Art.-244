from Object import Object
from Motorcycle import Motorcycle


class Player(Object):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = ""
        #self.motorcycle = Motorcycle()

    def update(self):
        pass


