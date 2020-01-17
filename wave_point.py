class Point:
    coords = []
    vel = []

    def __init__(self,x,y,vel_x,vel_y):
        self.coords = [x,y]
        self.vel = [vel_x,vel_y]