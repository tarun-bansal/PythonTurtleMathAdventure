# Python Turtle Cheatsheet

## 🐢 Basic Turtle Commands

### Setup
```python
import turtle                  # Import turtle module
t = turtle.Turtle()           # Create a turtle
screen = turtle.Screen()      # Create screen object
turtle.done()                 # Keep window open
```

### Movement
```python
t.forward(100)    # Move forward 100 steps
t.backward(50)    # Move backward 50 steps
t.left(90)        # Turn left 90 degrees
t.right(45)       # Turn right 45 degrees
t.goto(100, 100)  # Go to coordinates (x, y)
t.home()          # Return to (0,0), face east
```

### Drawing Control
```python
t.penup()         # Lift pen (stop drawing)
t.pendown()       # Lower pen (start drawing)
t.pensize(5)      # Set pen thickness
t.speed(0)        # 0=fastest, 1=slowest, 10=fast
t.clear()         # Clear drawing
t.reset()         # Clear and reset turtle
```

### Appearance
```python
t.color("red")            # Set pen color
t.color("red", "blue")    # Pen color, fill color
t.begin_fill()            # Start filled shape
t.end_fill()              # End filled shape
t.fillcolor("yellow")     # Set fill color
t.pencolor("green")       # Set pen color only
```

### Shapes and Stamps
```python
t.circle(50)              # Draw circle radius 50
t.dot(20, "red")          # Draw dot diameter 20
t.stamp()                 # Leave turtle imprint
t.shape("turtle")         # Change shape
t.shapesize(2, 2)         # Stretch shape (width, length)
```

## 📊 Python Basics

### Variables
```python
name = "Alex"             # String variable
age = 9                   # Integer variable
score = 95.5              # Float variable
is_learning = True        # Boolean variable
```

### Math Operators
```python
5 + 3      # Addition: 8
10 - 4     # Subtraction: 6
6 * 7      # Multiplication: 42
15 / 3     # Division: 5.0 (float)
15 // 4    # Integer division: 3
15 % 4     # Modulus (remainder): 3
2 ** 3     # Exponentiation: 8 (2³)
```

### Comparison Operators
```python
5 == 5     # Equal: True
5 != 3     # Not equal: True
10 > 5     # Greater than: True
3 < 7      # Less than: True
5 >= 5     # Greater than or equal: True
4 <= 4     # Less than or equal: True
```

### Logical Operators
```python
True and False    # AND: False (both must be True)
True or False     # OR: True (at least one True)
not True          # NOT: False (reverses)
```

## 🔄 Loops

### For Loops
```python
# Repeat 5 times
for i in range(5):
    print(i)          # Prints 0,1,2,3,4

# With start and end
for i in range(1, 6):
    print(i)          # Prints 1,2,3,4,5

# With step
for i in range(0, 10, 2):
    print(i)          # Prints 0,2,4,6,8
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1        # Don't forget to update!
```

## ⚖️ Conditionals

### If Statements
```python
if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Keep trying")
```

## 📦 Lists

### Creating Lists
```python
colors = ["red", "green", "blue"]     # String list
numbers = [1, 2, 3, 4, 5]             # Number list
mixed = [1, "hello", True]            # Mixed list
empty = []                            # Empty list
```

### List Operations
```python
colors.append("yellow")       # Add to end
colors.insert(1, "orange")    # Insert at position 1
colors.remove("red")          # Remove "red"
colors.pop(2)                 # Remove item at index 2
len(colors)                   # Get length: 4
"green" in colors             # Check if exists: True
```

### Accessing Lists
```python
colors[0]           # First item: "red"
colors[-1]          # Last item: "blue"
colors[1:3]         # Slice: ["green", "blue"]
colors[:2]          # First 2 items
colors[2:]          # From index 2 to end
```

## 🧰 Functions

### Defining Functions
```python
def say_hello(name):
    """Greets a person"""
    print(f"Hello, {name}!")

say_hello("Alex")   # Call the function
```

### Functions with Return
```python
def add_numbers(a, b):
    """Adds two numbers"""
    return a + b

result = add_numbers(5, 3)   # result = 8
```

### Default Parameters
```python
def draw_square(size=100):
    """Draws square with optional size"""
    for i in range(4):
        t.forward(size)
        t.left(90)
```

## 🎮 User Input

### Getting Input
```python
name = input("What's your name? ")      # String input
age = int(input("How old are you? "))   # Convert to int
```

### Simple Error Handling
```python
try:
    number = int(input("Enter a number: "))
    print(f"Twice your number is {number * 2}")
except ValueError:
    print("That's not a valid number!")
```

## 🎲 Random Numbers

### Random Module
```python
import random

random.randint(1, 10)      # Random integer 1-10
random.choice(["a", "b", "c"])  # Random choice from list
random.random()            # Random float 0.0-1.0
```

## 📐 Math Module

### Useful Math Functions
```python
import math

math.sqrt(25)          # Square root: 5.0
math.pow(2, 3)         # 2³ = 8.0
math.pi                # π ≈ 3.14159
math.floor(3.7)        # Round down: 3
math.ceil(3.2)         # Round up: 4
abs(-5)                # Absolute value: 5
```

## 🕒 Time Module

### Timing and Delays
```python
import time

time.sleep(1)          # Pause for 1 second
time.sleep(0.5)        # Pause for 0.5 seconds
```

## 🎨 Animation Basics

### Smooth Animation
```python
import turtle
import time

screen = turtle.Screen()
screen.tracer(0)       # Turn off auto-update

# Animation loop
for frame in range(100):
    t.clear()          # Clear previous frame
    # Draw something...
    screen.update()    # Update screen
    time.sleep(0.05)   # Control speed
```

## 🔧 Common Patterns

### Drawing a Polygon
```python
def draw_polygon(sides, size):
    """Draws any regular polygon"""
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)
```

### Grid Pattern
```python
for x in range(5):        # 5 columns
    for y in range(5):    # 5 rows
        t.penup()
        t.goto(x * 50, y * 50)
        t.pendown()
        t.dot(10)
```

### Spiral Pattern
```python
for i in range(100):
    t.forward(i * 2)      # Increasing step
    t.left(91)            # Not 90° for spiral
```

## 🐛 Debugging Tips

### Print Debugging
```python
print(f"DEBUG: x = {x}, y = {y}")  # See variable values
```

### Check Types
```python
type(variable)            # See what type it is
```

### Test Small Parts
```python
# Comment out sections with #
# t.forward(100)  # Temporarily disable
```

## 📝 Good Practices

### Naming Conventions
```python
player_score = 100       # Use underscores, descriptive
circle_radius = 50       # Not: cr or x
is_game_over = False     # Boolean: start with "is_"
```

### Comments
```python
# Single line comment
def calculate_area(length, width):
    """Multi-line docstring explains function"""
    return length * width
```

### Organization
```python
# Import statements first
import turtle
import random

# Then functions
def setup():
    # Setup code here

# Main program at bottom
if __name__ == "__main__":
    setup()
    # Main code here
```

## 🎯 Scratch to Python Quick Reference

| Scratch Block | Python Equivalent |
|---------------|------------------|
| move 10 steps | `t.forward(10)` |
| turn ↺ 15 degrees | `t.left(15)` |
| turn ↻ 15 degrees | `t.right(15)` |
| go to x:0 y:0 | `t.goto(0, 0)` |
| pen down | `t.pendown()` |
| pen up | `t.penup()` |
| set pen color to | `t.color("red")` |
| repeat 10 | `for i in range(10):` |
| forever | `while True:` |
| if then | `if condition:` |
| if then else | `if condition: ... else: ...` |
| ask and wait | `input("Question? ")` |
| set variable to | `score = 100` |
| change variable by | `score = score + 10` |
| make a list | `colors = []` |
| add to list | `colors.append("red")` |
| item of list | `colors[0]` |
| length of list | `len(colors)` |
| make a block | `def my_function():` |

## 💡 Pro Tips

1. **Start small**: Get something working, then add features
2. **Test often**: Run code after every small change
3. **Read errors**: Error messages tell you what's wrong
4. **Take breaks**: Fresh eyes see mistakes
5. **Have fun**: Programming is creative play!

---

*Keep this cheatsheet handy while working through the sessions. It's normal to look things up - even professional programmers do!*