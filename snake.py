from turtle import Turtle # class import

DISTANCE = 20
up = 90
down = 270
left = 180
right = 0

STARTING_SEGMENTS = 3
START = (0,0)

class Snake:
    '''Create a three segment snake'''
    # Snake constructor
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]


    def create_snake(self):
        for i in range(STARTING_SEGMENTS): # create 3 snake (turtle) objects
            self.create_snake_piece(START)
            print('snake piece')
        # create an attribute that contains the list items
        self.mylist = self.segment_list


    def create_snake_piece(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(position)
        # snake_segment.setposition(position)
        self.segment_list.append(snake_segment)  # segment list is full of snake objects


    def move(self):
        my_length = len(self.mylist)
        # iterate through segment as element 2->1
        for i in range(my_length-1, 0, -1):  # generate numbers beginning at second to last element
            x_cord = self.mylist[i-1].xcor()  # get the x coord of the second to last element
            y_cord = self.mylist[i-1].ycor() # e.g., y cord of segement # 2 in list (index 1)
            # move block i to position of previous block
            self.segment_list[i].goto(x_cord, y_cord)
            # move the head or the first block forward --> the others will follow
        self.head.forward(DISTANCE)


    def extend(self):
        '''create a new snake segment and send it to a specific position based on tail location'''
        #print(f'snake start length: {len(self.segment_list)}')
        coords = self.segment_list[-1].position() # tail position of snake
        #print(f'tail coords: {coords}')
        self.create_snake_piece(coords)
        self.segment_list[-1].color('red')
        #print(f'snake length: {len(self.segment_list)}')


    def snake_position(self):
        self.position_list = []
        for segment in self.segment_list[1:]: # all elements except the head
            x = segment.pos()
            # print(f'turtle distance: {self.distance(x)}')
            #print(f'snake position: {segment.pos()}') # unbelievably, this works and returns a tuple (x,y)
            self.position_list.append(segment.pos())
            #print(f'position list: {self.position_list}')
            #print(f'head position: {self.head.pos()}')
            if self.head.pos() == x:
                print("Snake, you hit yoself")


    def up(self):
        if self.head.heading() != down:
            # allow snake to go down
            self.head.seth(up)

    def down(self):
        if self.head.heading() != up:
            self.head.seth(down)

    def right(self):
        if self.head.heading() != left:
            self.head.seth(right)

    def left(self):
        if self.head.heading() != right:
            self.head.seth(left)

    def clear_snake(self):
        for seg in self.segment_list:
            seg.goto(-800, -800)
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]
