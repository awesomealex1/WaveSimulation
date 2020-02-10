from math import sin,pi,sqrt,floor,ceil
from wave_point import Point
import time
import PIL
import image_gif

amplitude = 2
period = 0.5
length = 20

width = 200
height = 200

height_of_center = 50
width_of_center = 0

def displacement(t,x):
    return amplitude*sin(2*pi*(t/period-x/length))

def displacement_to_color(d):
    return d/amplitude*255

def simulate(time_total,time_step,graphics_time_step):
    for i in range(0,floor(time_total/time_step)):
        next(time_step*i,i)
        time.sleep(graphics_time_step)

def next(current_time,n_image):
    displacements_on_line = [displacement(current_time,x) for x in range(0,width)] #First calculate the displacement for every pixel on a horizontal line, then use those values for circles intersecting specific pixel
    points = []

    for x in range(0,width):
        for y in range(0,height):
            radius = sqrt((x-width_of_center)**2+(y-width_of_center)**2)
            if floor(radius) < len(displacements_on_line):
                points.append(Point(x,y,color=[ceil(abs(displacement_to_color(displacements_on_line[floor(radius)]))),0,0]))
            else:
                points.append(Point(x,y,color=[0,0,0]))

    image_gif.write_image("image",points,width,height,n_image)

simulate(1,0.03,0)