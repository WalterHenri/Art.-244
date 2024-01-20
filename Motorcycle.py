from enum import Enum


class State(Enum):
    accelerating = 1
    decelerating = 2
    curving_right = 3
    curving_left = 4
    facing_up = 5


class Motorcycle:
    def __init__(self, sprite, acceleration, deceleration, max_speed, max_acceleration, state):
        self.sprite = sprite
        self.acceleration = acceleration
