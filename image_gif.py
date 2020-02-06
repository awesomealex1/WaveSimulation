from PIL import Image

def write_image(name,pixels,width,height):
    new_pixels = []
    count = 0
    for i in range(0,height):
        arr = []
        for j in range(0,height):
            arr.append(new_pixels[count].color)
            count++
        new_pixels.append(arr)
    print(new_pixels)
    img = Image.fromarray(new_pixels)
    img.save(name)