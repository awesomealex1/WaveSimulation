import graphics

class my_graphics:
    def makewin():          # Makes Window
        global win 
        win = graphics.GraphWin("Wave Simulation", 500, 500)

    def array(points):      # Draws array of points
        for p in points:
            point = graphics.Point(p.coords[0], p.coords[1])
            point.draw(win)

    def point(point):       # Draws single point
            p = graphics.Point(point.coords[0], point.coords[1])
            p.draw(win)

    def point_xy(x, y):     # Draws single point given only x, y
        p = graphics.Point(x, y)
        p.draw(win)

    def closewin():         # Closes Window
        win.getMouse()
        win.close
    