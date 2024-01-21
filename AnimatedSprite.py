import pygame
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spritesheet, frame_width, frame_height, num_frames):
        super().__init__()

        self.frames = []
        self.num_frames = num_frames
        self.width = frame_width
        self.height = frame_height

        for i in range(num_frames):
            frame = spritesheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()

        self.rect.center = (0, 0)
        self.animation_speed = 0.1  # Adjust based on your desired animation speed

    def update(self):
        self.current_frame = (self.current_frame + self.animation_speed) % self.num_frames
        self.image = self.frames[self.current_frame]
