import graphics
import image_gif

class Graph():

    def __init__(self, points, width, height):
        self.win = graphics.GraphWin("Wave Simulation", width, height, autoflush=False)
        self.width = width
        self.height = height

    def update_graph(self, points,n_image):
        image_gif.write_image("image",points,self.width,self.height,n_image)