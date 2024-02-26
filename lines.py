class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        

class Line:
    def __init__(self, point_1, point_2) -> None:
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas, fill_colour) -> None:
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill = fill_colour, width = 2
        )
        canvas.pack()