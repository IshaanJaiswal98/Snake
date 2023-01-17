from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            seg = Turtle()
            seg.shape("square")
            seg.color("white")
            seg.penup()
            seg.goto(i)
            self.segment.append(seg)

    def create_new_body(self):
        seg = Turtle()
        seg.shape("square")
        seg.color("white")
        seg.penup()
        seg.goto(self.segment[-1].xcor(),self.segment[-1].ycor())
        self.segment.append(seg)




    def move(self):
        for val in range(len(self.segment)-1,0,-1):
            pos_x = self.segment[val-1].xcor()
            pos_y = self.segment[val-1].ycor()
            self.segment[val].goto(pos_x,pos_y)
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







