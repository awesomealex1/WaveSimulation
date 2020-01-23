import graphics

class my_graphics:
    def graph(points):
        win = graphics.GraphWin("wave simulation", 500, 500)
        for p in points:
            point = graphics.Point(p.coords[0], p.coords[1])
            point.draw(win)
        win.getMouse()
        win.close
