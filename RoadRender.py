from Road import Road
from Camera import Camera
from Quad import Quad
from Object import Object
import ConfigMap
import pygame


class RoadRender:
    def __init__(self, screen):
        self.road = Road()
        self.road.create_non_random_road()
        self.cam = Camera(0.0, ConfigMap.Configuration.cam_height, 0.0, ConfigMap.Configuration.fov)
        self.delta = ConfigMap.Configuration.delta
        self.speed = ConfigMap.Configuration.speed
        self.redraw = True
        self.screen = screen
        self.player = Object()
        self.running = True

    def update(self):
        # Automatic movement
        self.redraw = True
        self.cam.z += self.speed
        if self.cam.z >= self.road.get_length() * ConfigMap.Configuration.road_seg_len:
            self.cam.z -= self.road.get_length() * ConfigMap.Configuration.road_seg_len

        if not self.redraw:
            return

        self.screen.fill((6, 123, 191))  # Clear the screen with a color
        start_pos = int(self.cam.z / ConfigMap.Configuration.road_seg_len)
        x = 0.0
        dx = 0.0
        cam_x = self.cam.x
        cam_y = self.cam.y
        cam_z = self.cam.z
        max_y = ConfigMap.Configuration.height
        self.cam.set_y(self.cam.get_y() + self.road.__getitem__(start_pos % self.road.get_length()).get_y())
        for i in range(start_pos + 1, start_pos + ConfigMap.Configuration.draw_distance):
            prev = self.road.__getitem__((i - 1) % self.road.get_length())
            curr = self.road.__getitem__(i % self.road.get_length())

            dx += curr.get_curve()
            x += dx

            if i - 1 >= self.road.get_length():
                self.cam.set_z(self.cam.get_z() - self.road.get_length() * ConfigMap.Configuration.road_seg_len)
            self.cam.set_x(cam_x - (x - dx))
            prev_projection = self.cam.project(prev, self.player, ConfigMap.Configuration.width, ConfigMap.Configuration.height)
            if i >= self.road.get_length():
                self.cam.z -= self.road.get_length() * ConfigMap.Configuration.road_seg_len
            self.cam.x = cam_x - x
            curr_projection = self.cam.project(curr, self.player, ConfigMap.Configuration.width, ConfigMap.Configuration.height)
            if curr_projection[2] <= self.cam.get_depth() or curr_projection[1] >= max_y:
                continue

            max_y = curr_projection[1]

            # Create quads
            grass_quad = Quad()
            rumble_quad = Quad()
            road_quad = Quad()
            road_line_quad = Quad()

            grass_quad.set_xyw_color(0.5 * ConfigMap.Configuration.width, 0.5 * ConfigMap.Configuration.width,
                                     prev_projection[1], curr_projection[1],
                                     ConfigMap.Configuration.width, ConfigMap.Configuration.width,
                                     ((i // 3) % 2) and (100, 168, 0) or (190, 190, 0))
            rumble_quad.set_xyw_color(prev_projection[0], curr_projection[0],
                                      prev_projection[1], curr_projection[1],
                                      1.1 * prev_projection[2], 1.1 * curr_projection[2],
                                      ((i // 9) % 2) and (255, 0, 0) or (255, 255, 255))
            road_quad.set_xyw_color(prev_projection[0], curr_projection[0],
                                    prev_projection[1], curr_projection[1],
                                    prev_projection[2], curr_projection[2],
                                    ((i // 3) % 2) and (100, 100, 100) or (120, 120, 120))
            road_line_quad.set_xyw_color(prev_projection[0], curr_projection[0],
                                         prev_projection[1], curr_projection[1],
                                         0.02 * prev_projection[2], 0.02 * curr_projection[2],
                                         ((i // 6) % 2) and (0, 0, 0) or (255, 255, 255))

            # Draw quads
            grass_quad.draw(self.screen)
            rumble_quad.draw(self.screen)
            road_quad.draw(self.screen)
            road_line_quad.draw(self.screen)

        self.cam.x = cam_x
        self.cam.y = cam_y
        self.cam.z = cam_z
        self.redraw = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    if self.cam.fov < ConfigMap.Configuration.fov_max:
                        self.cam.fov += ConfigMap.Configuration.d_fov
                        self.update_text = True
                elif event.key == pygame.K_f:
                    if self.cam.fov > ConfigMap.Configuration.fov_min:
                        self.cam.fov -= ConfigMap.Configuration.d_fov
                        self.update_text = True
                elif event.key == pygame.K_UP:
                    if self.speed < ConfigMap.Configuration.speed_max:
                        self.speed += ConfigMap.Configuration.d_speed
                        self.update_text = True
                elif event.key == pygame.K_DOWN:
                    if self.speed > ConfigMap.Configuration.speed_min:
                        self.speed -= ConfigMap.Configuration.d_speed
                        self.update_text = True
                elif event.key == pygame.K_RIGHTBRACKET:
                    if self.delta < ConfigMap.Configuration.delta_max:
                        self.delta += ConfigMap.Configuration.d_delta
                        self.update_text = True
                elif event.key == pygame.K_LEFTBRACKET:
                    if self.delta > ConfigMap.Configuration.delta_min:
                        self.delta -= ConfigMap.Configuration.d_delta
                        self.update_text = True
        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
           # self.cam.x -= self.delta
            self.player.x -= 100
            self.redraw = True
        if keys[pygame.K_d]:
            #self.cam.x += self.delta
            self.player.x += 100
            self.redraw = True
        if keys[pygame.K_w]:
            if self.cam.y < ConfigMap.Configuration.cam_height_max:
                self.cam.y += self.delta
            self.redraw = True
        if keys[pygame.K_s]:
            if self.cam.y > ConfigMap.Configuration.cam_height_min:
                self.cam.y -= self.delta
            self.redraw = True
