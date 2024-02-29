from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = ("Maze Solver")
        self.__canvas = Canvas(self.__root, bg ="green", height=height, width = width)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def draw_line(self, line, fill_colour="black") -> None:
       line.draw(self.__canvas, fill_colour)

    def close(self) -> None:
        self.__running = False


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, point_1: Point, point_2: Point) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas, fill_colour) -> None:
        canvas.create_line(
            self.point_1.x, self.point_1.y, 
            self.point_2.x, self.point_2.y, 
            fill = fill_colour, width = 2
        )
        canvas.pack()
