from enum import Enum

import pygame
from AnimatedSprite import AnimatedSprite


class State(Enum):
    accelerating = 1
    decelerating = 2
    curving_right = 3
    curving_left = 4
    facing_up = 5


texturesForMotorCycle = pygame.image.load('Assets/mota.png')


class Motorcycle:
    def __init__(self, x, y, acceleration, deceleration, max_speed, state):
        self.x = x
        self.y = y
        self.sprite = texturesForMotorCycle
        self.turnAmount = 0
        self.anim = AnimatedSprite(texturesForMotorCycle, 48, 64, 6)
        self.acceleration = acceleration
        self.deceleration = deceleration
        self.max_speed = max_speed
        self.state = state
        self.speed = 0

    def update(self, delta_time):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.turnAmount -= 0.1 * delta_time

        if keys[pygame.K_d]:
            self.turnAmount += 0.1 * delta_time

        if keys[pygame.K_SPACE]:
            self.change_state(State.accelerating)

        if keys[pygame.K_BACKSPACE]:
            self.change_state(State.decelerating)


        self.turnAmount = min(max(self.turnAmount, -3), 3)

        self.anim.update(delta_time)
        if self.state == State.accelerating:
            self.speed += self.acceleration * delta_time
            self.speed = min(self.speed, self.max_speed)
        elif self.state == State.decelerating:
            self.speed -= self.deceleration * delta_time
            self.speed = max(self.speed, 0)



    def change_state(self, new_state):
        self.state = new_state

    def draw(self, screen):
        speedState = max(min(int((self.speed / self.max_speed) * 3), 2), 0);
        turnState = abs(int(self.turnAmount))
        if turnState != 0:
            speedState = 2
        sprite = self.anim.frames[speedState + turnState]
        sprite = pygame.transform.scale_by(sprite, 2) # Assign the result back to sprite
        if self.turnAmount < 0:
            sprite = pygame.transform.flip(sprite, True, False)
            screen.blit(sprite, (self.x, self.y))
        else:
            screen.blit(sprite, (self.x, self.y))
