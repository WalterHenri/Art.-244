from Road import Road
from Camera import Camera
from Quad import Quad
from Object import Object
import ConfigMap
import pygame


class RoadRender:
    def __init__(self, screen, player):
        self.road = Road()
        self.road.create_non_random_road()
        self.cam = Camera(0.0, ConfigMap.Configuration.cam_height, 0.0, ConfigMap.Configuration.fov)
        self.delta = ConfigMap.Configuration.delta
        self.speed = ConfigMap.Configuration.speed
        self.redraw = True
        self.screen = screen
        self.player = player
        self.running = True
        self.font_min = pygame.font.Font(None, 32)
        self.font_max = pygame.font.Font(None, 64)


    def update(self):
        # Automatic movement
        self.redraw = True
        self.cam.z += self.player.motorcycle.speed
        if self.cam.z >= self.road.get_length() * ConfigMap.Configuration.road_seg_len:
            self.road.lap += 1
            if self.road.lap < self.road.n_laps:
                self.cam.z -= self.road.get_length() * ConfigMap.Configuration.road_seg_len
            else:
                self.running = False
                self.road.on_win(self.player)

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
        last_seg = self.road.__getitem__((start_pos + ConfigMap.Configuration.draw_distance-1)  % self.road.get_length())
        max_z = last_seg.get_z()

        projections = []

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


            projections.append((prev_projection, curr_projection))

        for i in reversed(range(start_pos + 1, start_pos + ConfigMap.Configuration.draw_distance)):

            index = i - (start_pos+1)
            z_ind = i % self.road.get_length()
            prev_projection = projections[index][1]
            curr_projection = projections[index][0]


            #
            # if curr_projection[2] <= self.cam.get_depth() or curr_projection[1] >= max_y:
            #     continue
            #
            #
            # max_y = curr_projection[1]



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




            # # Draw quads
            if not curr_projection[2] <= self.cam.get_depth():
                grass_quad.draw(self.screen)
                rumble_quad.draw(self.screen)
                road_quad.draw(self.screen)
                road_line_quad.draw(self.screen)

            for obj_index in self.road.en_index[z_ind]:
                en = self.road.enhancements[obj_index]
                if self.cam.z + ConfigMap.Configuration.draw_distance < en.z - 800:
                    if en.z > max_z:
                        continue

                    project = [0, 0, 0]

                    project[0] = curr_projection[0] + en.x * (curr_projection[2]/ConfigMap.Configuration.road_width)
                    project[1] = curr_projection[1]
                    project[2] = (curr_projection[2]/ConfigMap.Configuration.road_width)

                    en.draw(self.screen, project[0], project[1], project[2])

        # for en in reversed(self.road.enhancements):
        #     if self.cam.z + ConfigMap.Configuration.draw_distance < en.z - 800:
        #         if en.z > max_z:
        #             continue
        #
        #         project = self.cam.project_en(en, self.player, ConfigMap.Configuration.width, ConfigMap.Configuration.height)
        #         en.draw(self.screen, project[0], project[1], project[2])


        self.draw_informations()
        self.cam.x = cam_x
        self.cam.y = cam_y
        self.cam.z = cam_z
        self.redraw = False


    def draw_informations(self):
        red = (255, 0, 0)
        yellow = (255, 255, 0)
        white = (255, 255, 255)

        speed_x = self.screen.get_width() / 1.2
        speed_y = self.screen.get_height() / 8

        speed_text = self.font_max.render(str(int(self.player.motorcycle.speed)), True, red)
        rect_speed = speed_text.get_rect()
        rect_speed.center = (speed_x, speed_y)

        # Render the text
        speed_text_desc = self.font_min.render('KM/H', True, yellow)
        rect_speed_text = speed_text_desc.get_rect()
        rect_speed_text.center = (speed_x + rect_speed_text.width * 1.2, speed_y)

        self.screen.blit(speed_text_desc, rect_speed_text)
        self.screen.blit(speed_text, rect_speed)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.x -= 100
            self.redraw = True
        if keys[pygame.K_d]:
            self.player.x += 100
            self.redraw = True

