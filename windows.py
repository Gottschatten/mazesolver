from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, hight) -> None:
        self.root = Tk()
        self.root.title = ("Maze Solver")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()

    def close(self) -> None:
        self.running = False

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line, fill_colour) -> None:
       line.draw(self.canvas, fill_colour)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas: Canvas, fill_colour) -> None:
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill = fill_colour, width = 2
        )
        canvas.pack()