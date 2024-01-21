

class Configuration:
    width = 800
    height = 600
    road_width = 2500.0
    road_seg_len = 250.0
    cam_height = 1800.0
    cam_height_min = 700.0
    cam_height_max = 5000.0
    fov = 100.0
    fov_min = 80.0
    fov_max = 120.0
    d_fov = 5.0
    delta = road_seg_len
    delta_min = 0.25 * road_seg_len
    delta_max = 2.0 * road_seg_len
    d_delta = 5.0
    speed = road_seg_len
    speed_min = 0.5 * road_seg_len
    speed_max = 2.0 * road_seg_len
    d_speed = 5.0
    draw_distance = 100
    draw_distance_min = 200
    draw_distance_max = 50
    fps = 100
    road_segments_min = 3
    road_segments_max = 10
    enter_length_min = 30
    enter_length_max = 100
    hold_length_min = 150
    hold_length_max = 500
    leave_length_min = 30
    leave_length_max = 100
    curve_min = -10.0
    curve_max = 10.0
    hill_min = -60.0
    hill_max = 60.0

    @staticmethod
    def load_config(filename):
        pass

