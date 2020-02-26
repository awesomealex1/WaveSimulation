from math import sin,pi,sqrt,floor,ceil
from wave_point import Point
import time
import PIL
import image_gif
import os

#Wave specific properties
amplitudes = [2,2]
perdiods = [0.5,0.5]
lengths = [20,20]

n_waves = len(amplitudes)
max_amplitude = 0
for a in amplitudes:
    max_amplitude += a

#Image and GIF properties
width = 200
height = 200

#Location of wave centers
height_of_centers = [199,0]
width_of_centers = [199,0]

def displacement(t,x,amplitude,period,length):  #Returns displacement for point that has a distance x from the center at time t
    return amplitude*sin(2*pi*(t/period-x/length))

def displacement_to_color(d):   #Returns a color depending on displacement (negative displacemet gets same color as positive displacement)
    return [ceil(abs(d/max_amplitude*255)),0,0]

def simulate(time_total,time_step):  #Simulate the wave
    for i in range(0,floor(time_total/time_step)):
        next(time_step*i,i)

def next(current_time,n_image):
    points = [] #List with all the points/pixels that will be in the gif

    for x in range(0,width):
        for y in range(0,height):
            d = 0
            #Go through loop to add wave displacemnts together for all waves at x,y
            for w in range(0,n_waves):
                distance = sqrt((x-width_of_centers[w])**2+(y-height_of_centers[w])**2)
                d += displacement(current_time,distance,amplitudes[w],perdiods[w],lengths[w])
            points.append(Point(displacement_to_color(d)))

    image_gif.write_image(points,width,height,n_image)  #Write an image that will be turned into a gif later on

simulate(1,0.03)  #Start the creation of the gif