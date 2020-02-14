from math import sin,pi,sqrt,floor,ceil
from wave_point import Point
import time
import PIL
import image_gif
import os

#Location of gif and images
path = os.path

#Wave specific properties
amplitude = 2
period = 0.5
length = 20

#Image and GIF properties
width = 200
height = 200

#Location of wave center
height_of_center = 50
width_of_center = 0

def displacement(t,x):  #Returns displacement for point that has a distance x from the center at time t
    return amplitude*sin(2*pi*(t/period-x/length))

def displacement_to_color(d):   #Returns a color depending on displacement (negative displacemet gets same color as positive displacement)
    return [ceil(abs(d/amplitude*255)),0,0]

def simulate(time_total,time_step):  #Simulate the wave
    for i in range(0,floor(time_total/time_step)):
        next(time_step*i,i)

def next(current_time,n_image):
    displacements_on_line = [displacement(current_time,x) for x in range(0,width)] #First calculate the displacement for every pixel on a horizontal line, then use those values for circles intersecting specific pixel
    points = [] #List with all the points/pixels that will be in the gif

    for x in range(0,width):
        for y in range(0,height):
            distance = sqrt((x-width_of_center)**2+(y-width_of_center)**2)    #Calculate the distance from the center of the wave for the specific point
            
            #Assign a color depending on distance from center and then add point to points list. If the distance is so big, that its not in the displacements list, set the points color to black
            if floor(distance) < len(displacements_on_line):
                points.append(Point(displacement_to_color(displacements_on_line[floor(distance)])))
            else:
                points.append(Point([0,0,0]))

    image_gif.write_image(points,width,height,n_image)  #Write an image that will be turned into a gif later on



simulate(1,0.03)  #Start the creation of the gif