import graphics

class Graph():

    def __init__(self, points):
        self.points = points
        self.graphics_points = [graphics.Point(p.coords[0], p.coords[1]) for p in self.points]
        self.win = graphics.GraphWin("Wave Simulation", 500, 500)
        for p in self.graphics_points:
            p.draw(self.win)
        l = graphics.Line(self.graphics_points[0],self.graphics_points[1])
        l.draw(self.win)


    def update_graph(self, new_points):
        for i in range(0,len(self.graphics_points)):
            self.graphics_points[i].move(new_points[i].coords[0]-self.graphics_points[i].getX(),new_points[i].coords[1]-self.graphics_points[i].getY())
            print(new_points[i].coords[0]-self.points[i].coords[0],new_points[i].coords[1]-self.points[i].coords[1])
        self.points = new_points

    def close_graph(self):
        self.win.close()

'''
def convex_hull(points):

    leftP = points[0]

    for p in points:
        if p.coords[0] < leftP.coords[0]:
            leftP = p

    pointsOnHull = []
    pOnHull = leftP
    pointsOnHull.append(pOnHull)
'''