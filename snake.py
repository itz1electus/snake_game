from turtle import Turtle
SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for idx in SNAKE_POSITION:
            self.add_segment(idx)

    def add_segment(self, idx):
        snake = Turtle(shape="square")
        snake.color("green")
        snake.penup()
        snake.setposition(idx)
        self.full_snake.append(snake)

    def reset(self):
        for segment in self.full_snake:
            segment.goto(1000, 1000)
        self.full_snake.clear()
        self.create_snake()
        self.head = self.full_snake[0]

    def extend(self):
        self.add_segment(self.full_snake[-1].position())

    def move(self):
        for segment_num in range(len(self.full_snake) - 1, 0, -1):
            new_x_cor = self.full_snake[segment_num - 1].xcor()
            new_y_cor = self.full_snake[segment_num - 1].ycor()
            self.full_snake[segment_num].goto(new_x_cor, new_y_cor)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
