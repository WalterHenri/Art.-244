from enum import Enum

import pygame
import AnimatedSprite


class State(Enum):
    accelerating = 1
    decelerating = 2
    curving_right = 3
    curving_left = 4
    facing_up = 5


texturesForMotorCycle = pygame.image.load('Assets/acc.png')


class Motorcycle:
    def __init__(self, x, y, acceleration, deceleration, max_speed, state):
        self.x = x
        self.y = y
        self.sprite = texturesForMotorCycle
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.max_speed = max_speed
        self.state = state
        self.speed = 0

    def update(self, delta_time):
        if self.state == State.accelerating:
            self.speed += self.acceleration * delta_time
            self.speed = min(self.speed, self.max_speed)
        elif self.state == State.decelerating:
            self.speed -= self.deceleration * delta_time
            self.speed = max(self.speed, 0)

    def change_state(self, new_state):
        self.state = new_state

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))