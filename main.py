from windows import Window, Point, Line

def main():
    a = Point(4, 6)
    b = Point(80, 50)
    c = Point(100, 500)
    d = Point(600, 300)
    ab = Line(a,b)
    ac = Line(a,c)
    ad = Line(a,d)
    bc = Line(b,c)
    bd = Line(b,d)
    cd = Line(c,d)


    win = Window(800, 600)
    win.draw_line(ab, "black")
    win.draw_line(ac, "black")
    win.draw_line(ad, "green")
    win.draw_line(bd, "yellow")
    win.draw_line(cd, "red")

    win.wait_for_close()

if __name__ == "__main__":
    main()