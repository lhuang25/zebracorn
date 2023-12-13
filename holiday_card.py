import random
from graphics import *

def draw_santa(win):
    # body
    body = Circle(Point(200, 300), 60)
    body.setFill("red")
    body.draw(win)
    # face
    face = Circle(Point(200, 240), 40)
    face.setFill("light yellow")
    face.draw(win)
    # eyes
    left_eye = Circle(Point(185, 245), 5)
    right_eye = Circle(Point(215, 245), 5)
    left_eye.setFill("black")
    right_eye.setFill("black")
    left_eye.draw(win)
    right_eye.draw(win)
    # hat
    hat_bottom = Rectangle(Point(160, 200), Point(240, 230))
    hat_top = Polygon(Point(160, 200), Point(240, 200), Point(200, 160))
    hat_bottom.setFill("red")
    hat_top.setFill("red")
    hat_bottom.draw(win)
    hat_top.draw(win)
    # mouth
    mouth = Line(Point(185, 270), Point(215, 270))
    mouth.setWidth(3)
    mouth.draw(win)
    
    #cookie
    cookie = Circle(Point(260, 320), 20)
    cookie.setFill("tan")
    cookie.draw(win)
    #chocolate chips
    chip1 = Circle(Point(265, 310), 2)
    chip1.setFill("brown")
    chip1.draw(win)
    chip2 = Circle(Point(250, 325), 2)
    chip2.setFill("brown")
    chip2.draw(win)
    chip3 = Circle(Point(270, 330), 2)
    chip3.setFill("brown")
    chip3.draw(win)
    
    # hand
    hand = Line(Point(200, 285), Point(260, 320))
    hand.setWidth(3)
    hand.draw(win)
    


def draw_text(win):
    text = Text(Point(200, 50), "HAPPY HOLIDAYS!")
    text.setSize(30)
    text.setStyle("bold")
    text.setFace("times roman")
    text.setTextColor("darkblue")
    text.draw(win)

def draw_snowflakes(win):
    for _ in range(30):
        x = random.randint(0, win.getWidth())
        y = random.randint(0, win.getHeight())
        snowflake = Text(Point(x, y), "❄️")
        snowflake.setSize(20)
        snowflake.draw(win)

def main():
    win = GraphWin("Santa Claus Greeting Card", 400, 400)
    win.setBackground("darkgreen")
    draw_santa(win)
    draw_snowflakes(win)
    draw_text(win)

if __name__ == "__main__":
    main()
