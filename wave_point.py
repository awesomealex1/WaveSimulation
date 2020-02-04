class Point:

    def __init__(self,x,y,vel_x=0,vel_y=0,color=[0,0,0]):
        self.coords = [x,y]
        self.x = x
        self.y = y
        self.vel = [vel_x,vel_y]
        self.color = color