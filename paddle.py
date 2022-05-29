from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def top(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)










