from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_parts = []

    def create_snake(self):
        turtle_1 = Turtle(shape="square")
        turtle_1.penup()
        turtle_1.color("white")

        turtle_2 = Turtle(shape="square")
        turtle_2.color("white")
        turtle_2.penup()
        turtle_2.setposition(y=0, x=-20)

        turtle_3 = Turtle(shape="square")
        turtle_3.color("white")
        turtle_3.penup()
        turtle_3.setposition(y=0, x=-40)

        self.snake_parts.append(turtle_1)
        self.snake_parts.append(turtle_2)
        self.snake_parts.append(turtle_3)

    def move_snake(self):
        for part in range(len(self.snake_parts) - 1, 0, -1):
            x = self.snake_parts[part - 1].xcor()
            y = self.snake_parts[part - 1].ycor()
            self.snake_parts[part].setposition(x=x, y=y)

        self.snake_parts[0].forward(MOVING_DISTANCE)

    def up(self=None):
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def down(self=None):
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def left(self=None):
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    def right(self=None):
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)

    def add_one_segment(self, position):
        snake_next_part = Turtle()
        snake_next_part.color("white")
        snake_next_part.penup()
        snake_next_part.shape("square")
        self.snake_parts.append(snake_next_part)
        snake_next_part.setposition(position)

    def extend(self):
        self.add_one_segment(self.snake_parts[-1].position())

    def reset_game(self):
        for segment in self.snake_parts:
            segment.setposition(x=1000, y=1000)
        self.snake_parts.clear()
        self.create_snake()

