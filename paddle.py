from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.speed('fastest')
        self.goto(coords)
        self.turtlesize(1, 5)
        self.setheading(90)

    def up(self):
        self.forward(20)
        # print(self.xcor(), self.ycor())

    def down(self):
        self.backward(20)
        # print(self.xcor(), self.ycor())

