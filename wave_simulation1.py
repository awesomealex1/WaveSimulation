from wave_point import Point
from wave_graphics import Graph
import time

def next(prev_points,time_passed):
    new_points = prev_points
    for p in new_points:
        x,y = p.coords[0], p.coords[1]
        new_x,new_y = x + p.vel[0]*time_passed, y + p.vel[1]*time_passed
        p.coords = [new_x,new_y]
    return new_points

def iterate(start_points,n_iterations,time_between,graph_time_between,graph):
    points = start_points
    for i in range(0,n_iterations):
        points = next(points,time_between)
        time.sleep(graph_time_between)
        graph.update_graph(points)
    return points

def print_points(points):
    for p in points:
        print("X:",p.coords[0],"Y:",p.coords[1],"XV:",p.vel[0],"YV:",p.vel[1])



points = [Point(0,0,1,0),Point(0,10,1,0),Point(0,20,1,0),Point(0,30,1,0)]

g = Graph(points)

points = iterate(points,10,10,1,g)

g.close_graph()