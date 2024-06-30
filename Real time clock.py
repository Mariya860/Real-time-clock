import turtle
import time

wn = turtle.Screen()
wn.bgcolor("white")
wn.setup(width=600, height=600)
wn.title("Real time clock")

clock = turtle.Turtle()
clock.speed(0)
clock.pensize(10)

# Function to draw the clock hands
def draw_hand(clock, pos, length, width):
    clock.penup()
    clock.goto(0, 0)
    clock.color("black")
    clock.setheading(90)
    clock.rt(pos)
    clock.pendown()
    clock.pensize(width)
    clock.fd(length)

# Function to draw the watch face
def draw_clock(h, m, s, clock):
    # Draw the clock face
    clock.penup()
    clock.goto(0, 210)
    clock.setheading(180)
    clock.color("black")
    clock.pendown()
    clock.circle(210)

    # Drawing hour markers
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(90)

    for _ in range(12):
        clock.fd(190)
        clock.pendown()
        clock.fd(20)
        clock.penup()
        clock.goto(0, 0)
        clock.rt(30)

    # Drawing the hands
    draw_hand(clock, (h % 12) * 30 + m / 2, 100, 7)  # hour
    draw_hand(clock, m * 6, 150, 3)  # minute
    draw_hand(clock, s * 6, 200, 1)  # second

# Continuous hourly update
def run_clock():
    while True:
        h = int(time.strftime("%I"))
        m = int(time.strftime("%M"))
        s = int(time.strftime("%S"))
        clock.clear()
        draw_clock(h, m, s, clock)
        wn.update()
        time.sleep(1)

# Start running the clock
run_clock()

# To keep the window open
wn.mainloop()


             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
