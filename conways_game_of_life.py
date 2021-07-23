# Recreation of Conway's Game of Life
# Discord: Avstin#7762
# GitHub: @4vstin
# July 18, 2021 to July 20, 2021

# Controls:
# Arrow keys to choose starting conditions
# 'Z' to turn on or off a cell when setting starting conditions
# Space to start the simulation
# 'X' to toggle on and off color coding the cells
# 'D' to increase the delay between generations by 0.5 seconds

# Info:
# Language: Python
# Version: python 3.8
# IDE: Visual Studio Code

# Imports
import turtle, math, time
        
# Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
CELLS_X_AMT = 50
CELLS_Y_AMT = 50
CELL_WIDTH = 20 #SCREEN_WIDTH/CELLS_X_AMT
CELL_HEIGHT = 20 #SCREEN_HEIGHT/CELLS_Y_AMT
TOTAL_CELL_AMT = CELLS_X_AMT*CELLS_Y_AMT
running = False
selected = 0
colors = False
delay = 0

# Lists
cells = list()
neighbor_ids = [-51, -50, -49, 1, 51, 50, 49, -1]

# Classes
class Cell(turtle.Turtle):
    # Initalize
    def __init__(self, state, id, neighbors_alive):
        turtle.Turtle.__init__(self)
        self.state = state
        self.id = id
        self.neighbors_alive = neighbors_alive
        self.shapesize(CELL_WIDTH/20, CELL_HEIGHT/20)
        self.shape("square")
        self.penup()
        x_formula = (-(SCREEN_WIDTH/2) + ((id % CELLS_X_AMT) * CELL_WIDTH)) + 10
        y_formula = (500 - ((math.floor(id / CELLS_X_AMT)) * CELL_HEIGHT)) - 10
        self.setx(x_formula)
        self.sety(y_formula)
        self.x1 = x_formula 
        self.x2 = x_formula + 10
        self.y1 = y_formula 
        self.y2 = y_formula - 10

        if self.state == "dead":
            self.color("black")
        else:
            self.color("white")

    def check_neighbors(self):
        for i in neighbor_ids:
            override_list(self.id + i, TOTAL_CELL_AMT)

            if cells[override + (self.id + i)].state == "alive":
                self.neighbors_alive += 1

# Functions
def override_list(normal, total):
    global override
    override = 0

    if normal < 0:
        override = (total - abs(normal)) - (normal)
    elif normal >= total:
        override = ((normal) - total) - (normal)

def set_ids():
    for i in range(TOTAL_CELL_AMT):
        cells.append(Cell("dead", i, 0))

def change_state():
    if cells[selected].state == "dead":
        cells[selected].state = "alive"
    else:
        cells[selected].state = "dead"

def start():
    global running
    running = True

def right():
    global selected
    selected += 1
    
    if selected > 2499:
        selected = 0

def left():
    global selected
    selected -= 1

    if selected < 0:
        selected += TOTAL_CELL_AMT

def up():
    global selected
    override_list(selected - CELLS_X_AMT, TOTAL_CELL_AMT)

    selected += CELLS_X_AMT + override - 100

def down():
    global selected
    override_list(selected + CELLS_X_AMT, TOTAL_CELL_AMT)

    selected += CELLS_X_AMT + override

def select_color():
    global selected
    for i in cells:
            if selected == i.id:
                i.color("grey")
            else:
                if i.state == "dead":
                    i.color("black")
                else:
                    i.color("white")

def toggle_colors():
    global colors
    if colors:
        colors = False
    else:
        colors = True

def increase_delay():
    global delay
    delay += 0.1
    if delay > 2:
        delay = 0
    print("Changed the delay to {}.".format(math.ceil(delay)))

# Window
window = turtle.Screen()
window.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
window.bgcolor("white")
window.title("Conway's Game of Life")
window.tracer(0)

# Setup Cells
set_ids()

# Key presses
window.listen()
window.onkeypress(change_state, "z")
window.onkeypress(start, "space")
window.onkeypress(right, "Right")
window.onkeypress(left, "Left")
window.onkeypress(down, "Down")
window.onkeypress(up, "Up")
window.onkeypress(toggle_colors, "x")
window.onkeypress(increase_delay, "d")

while True:

    # Change color
    select_color()

    if running:
        selected = None
        select_color()

        break

    # Update the screen
    window.update()

# Running
while True:

        # Find neighbors before checking
        for i in cells:
            i.check_neighbors()
        
        # Run the next generation
        for i in cells:

            # Change state
            if i.state == "alive" and i.neighbors_alive < 2:
                i.state = "dead"
                i.color("black")

            elif i.state == "alive" and i.neighbors_alive > 3:
                i.state = "dead"
                i.color("black")

            elif i.state == "dead" and i.neighbors_alive == 3:
                i.state = "alive"
                i.color("white")
            
            elif i.state == "alive" and i.neighbors_alive == 2 or i.state == "alive" and i.neighbors_alive == 3:
                i.color("white")

            # Adds more colors
            if colors and i.state == "alive":
                if i.neighbors_alive == 2:
                    i.color("blue")
                else:
                    i.color("red")

            # Reset
            i.neighbors_alive = 0
        
        # Wait the delay
        time.sleep(delay)

        # Update the screen
        window.update()