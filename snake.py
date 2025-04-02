from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
class Snake:
    def __init__(self,):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.control()
    def create_snake(self):
        for position in STARTING_POSITIONS :
            self.adding_snake(position)
            
    def adding_snake(self, position):
        new_snake =  Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.adding_snake((self.segments[-1]).position())

    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def control(self):
        screen = Screen()
        def turn_right():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)
        def turn_left():
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)
        def turn_up():
            if self.head.heading() != DOWN:
                self.head.setheading(UP)
        def turn_down():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        screen.listen()
        screen.onkey(turn_right, "Right")
        screen.onkey(turn_right, "d")
        screen.onkey(turn_left, "Left")
        screen.onkey(turn_left, "a")
        screen.onkey(turn_up, "Up")
        screen.onkey(turn_up, "w")
        screen.onkey(turn_down, "Down")
        screen.onkey(turn_down, "s")