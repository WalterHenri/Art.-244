import pygame
from App import App

def main():
    pygame.init()
    app = App()
    app.run()

if __name__ == "__main__":
    main()

"""""
import AnimatedSprite
from Road import Road
from Road import Segment
from Motorcycle import Motorcycle

pygame.init()

info = pygame.display.Info()

width = info.current_w/2
height = info.current_h/2

screen = pygame.display.set_mode((width, height))


color = (10, 10, 255)
>>>>>>> 0e5168d76fd9ccef8a0087c1d83be0400016b259


if __name__ == "__main__":
    main()

<<<<<<< HEAD
=======
motorcycle = Motorcycle(width/2, height/2, 10, 10, 100, 1)
road.generate_road(800, 100, 10)


from Banana import Banana
# BAnAanaa
banana = Banana(width/2 , height/2- 50)



while True:

    screen.fill(color)

    road.draw_road(screen)

    road.update(10, 800, 100, 10)

    motorcycle.update(10)
    motorcycle.draw(screen)

    banana.update(0.2)
    banana.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
>>>>>>> 0e5168d76fd9ccef8a0087c1d83be0400016b259
"""