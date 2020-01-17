from wave_point import Point

def next(prev_points,time_passed):
    new_points = []
    for p in prev_points:
        x,y = p.coords[0], p.coords[1]
        new_x,new_y = x + p.vel[0]*time_passed, y + p.vel[1]*time_passed
        p.coords = [new_x,new_y]
        