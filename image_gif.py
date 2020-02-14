from PIL import Image
import numpy as np
import imageio
import os

def write_image(pixels,width,height,n_image):
    new_pixels = [] #Create pixel array which will store [r,g,b] colors
    count = 0
    for i in range(0,height):
        arr = []
        for j in range(0,height):
            arr.append(pixels[count].color)
            count += 1
        new_pixels.append(arr)
    img = Image.fromarray(np.array(new_pixels, dtype=np.uint8))
    img.save("Images/img"+str(n_image)+".png")
    if n_image == 32:
        write_gif(33)

def write_gif(n_images):
    png_dir = "Images"
    images = []
    for i in range(0,n_images):
        file_path = os.path.join(png_dir, "img"+str(i)+".png")
        images.append(imageio.imread(file_path))
    imageio.mimsave('Images/wave.gif', images)