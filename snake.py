from turtle import Turtle, Screen
position = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for t_turtles in position:
            self.grow_snake(t_turtles)

    def grow_snake(self, t_turtles):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(t_turtles)
        self.all_turtles.append(new_turtle)

    def reset(self):
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]

    def extent(self):
        self.grow_snake(self.all_turtles[-1].position())


    def move(self):
        for conjuto in range(len(self.all_turtles) - 1, 0, -1):
                new_x = self.all_turtles[conjuto - 1].xcor()
                new_y = self.all_turtles[conjuto - 1].ycor()
                self.all_turtles[conjuto].goto(new_x, new_y)
        self.head.forward(20)

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
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)



