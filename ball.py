from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.setheading(45)
        self.penup()
        self.speed('slow')

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    # def check_for_bounce(self):
    #     if self.ycor() >= 290:
        # TODO get heading and change directions




