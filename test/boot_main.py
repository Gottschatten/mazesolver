from boot_graphics import Window
from boot_cell import Cell


def main():
    win = Window(800, 600)

    a = Cell(win)
    a.has_left_wall = False
    a.draw(50, 50, 100, 100)

    b = Cell(win)
    b.has_right_wall = False
    b.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    d = Cell(win)
    d.has_top_wall = False
    d.draw(300, 300, 500, 500)

    b.draw_move(a)

    c.draw_move(d, True)

    win.wait_for_close()

if __name__ == "__main__":
    main()
