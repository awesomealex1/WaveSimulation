from math import sin,pi,sqrt,floor,ceil
from wave_point import Point
from wave_graphics import Graph
import time
amplitude = 2
period = 0.5
length = 20

width = 200
height = 200

height_of_center = 50
width_of_center = 0

points = []

def displacement(t,x):
    return amplitude*sin(2*pi*(t/period-x/length))

def displacement_to_color(d):
    return d/amplitude*255

def simulate(time_total,time_step,graphics_time_step):
    for i in range(0,floor(time_total/time_step)):
        next(time_step*i)
        time.sleep(graphics_time_step)

def next(time):
    print("NEXT")
    displacements_on_line = [displacement(time,x) for x in range(0,width)] #First calculate the displacement for every pixel on a horizontal line, then use those values for circles intersecting specific pixel
    all_points = []
    for x in range(0,width):
        for y in range(0,height):
            radius = sqrt((x-width_of_center)**2+(y-width_of_center)**2)
            if floor(radius) < len(displacements_on_line):
                all_points.append(Point(x,y,color=[ceil(abs(displacement_to_color(displacements_on_line[floor(radius)]))),0,0]))
    g.update_graph(all_points)

g = Graph(points,width,height)

simulate(10,1,0.5)