# Session 6: Functions: Your Code Toolbox

## 🎯 Learning Objectives
- Define functions with `def`
- Call functions with parameters
- Return values from functions
- Organize code into reusable pieces
- Connect Scratch custom blocks to Python functions

💡 **Session Note**: This session covers many concepts. Take breaks at the ⏱️ markers to avoid overload.

## 🧰 What is a Function?

Imagine you have a magic recipe box. Each recipe card tells you how to make something:
- "How to draw a square"
- "How to calculate area"
- "How to greet someone"

Instead of rewriting the instructions every time, you just say "Use the square recipe!" That's what functions do in programming.

**Kid-Friendly Analogy**: "Functions are like recipes you write once and use whenever you need that dish. Want to draw a square? Use your `draw_square()` recipe!"

## 📝 Defining Functions with `def`

To create a function, use `def` (short for "define"):

```python
def say_hello():
    print("Hello!")
    print("Nice to meet you!")

# Now use it
say_hello()  # Calls the function
say_hello()  # Call it again!
```

**Note**: The function definition doesn't run until you call it with `()`.

## 🎯 Functions with Parameters

Parameters are like recipe ingredients - they make functions flexible:

```python
def draw_square(size):
    """Draws a square of given size"""
    for i in range(4):
        t.forward(size)
        t.left(90)

# Use with different sizes
draw_square(100)  # Big square
draw_square(50)   # Medium square
draw_square(20)   # Small square
```

## 🔄 Functions that Return Values

Some functions calculate something and give you back the result:

```python
def calculate_area(length, width):
    """Calculates area of rectangle"""
    area = length * width
    return area  # Send the result back

# Use the returned value
room_area = calculate_area(10, 12)
print(f"The room area is {room_area} square feet")

# Or use it directly
print(f"A 5x5 square has area {calculate_area(5, 5)}")
```

**Math Connection**: This is exactly like mathematical functions! `f(x) = x²` becomes `def f(x): return x * x`

---

⏱️ **20-Minute Break Point**

*Great! You've learned the core concepts. Take a short break if you need one. When you're ready, continue with hands-on exercises to practice your new skills.*

---
## 🐢 Exercise 1: Shape Drawing Toolkit

Let's build a collection of shape-drawing functions:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

# Function 1: Draw a square
def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

# Function 2: Draw a triangle
def draw_triangle(size):
    for i in range(3):
        t.forward(size)
        t.left(120)  # 360 ÷ 3 = 120

# Function 3: Draw a circle (approximated with polygon)
def draw_circle(radius):
    circumference = 2 * 3.14159 * radius
    sides = 36  # More sides = smoother circle
    side_length = circumference / sides

    for i in range(sides):
        t.forward(side_length)
        t.left(360 / sides)

# Use our functions
draw_square(100)
t.penup()
t.forward(150)
t.pendown()

draw_triangle(100)
t.penup()
t.forward(150)
t.pendown()

draw_circle(50)

turtle.done()
```

**Challenge**: Add functions for pentagon, hexagon, star!

## 🧮 Exercise 2: Math Helper Functions

Create a library of useful math functions:

```python
# Math helper functions
def double(number):
    return number * 2

def square(number):
    return number * number

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Test our functions
print(f"Double 7 is {double(7)}")
print(f"Square of 9 is {square(9)}")
print(f"Is 12 even? {is_even(12)}")
print(f"Is 7 even? {is_even(7)}")
print(f"5! = {factorial(5)}")

# Use in calculations
radius = 5
area = 3.14159 * square(radius)
print(f"Area of circle with radius {radius} is {area}")
```

**Math Connection**: These are mathematical functions come to life! `f(x) = x²` is our `square(x)` function.

## 🎨 Exercise 3: Pattern Generator Functions

Create functions that make complex patterns:

```python
import turtle
import random

t = turtle.Turtle()
t.speed("fastest")

def random_color():
    """Returns a random color name"""
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    return random.choice(colors)

def draw_star(size):
    """Draws a 5-pointed star"""
    for i in range(5):
        t.forward(size)
        t.right(144)  # 180 - (360/5) = 144

def draw_flower(petals, size):
    """Draws a flower with given number of petals"""
    for i in range(petals):
        t.color(random_color())
        # Each petal is like a thin circle
        for j in range(36):  # Half circle
            t.forward(size / 10)
            t.right(5)
        t.left(180)  # Turn around
        for j in range(36):  # Other half
            t.forward(size / 10)
            t.right(5)
        t.left(180)  # Back to start
        t.right(360 / petals)  # Move to next petal position

# Draw a garden of shapes
t.penup()
t.goto(-200, 0)
t.pendown()
draw_star(100)

t.penup()
t.goto(0, 0)
t.pendown()
draw_flower(8, 100)

t.penup()
t.goto(200, 0)
t.pendown()
draw_flower(12, 60)

turtle.done()
```

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "Make a block" button | `def function_name():` |
| Add input to block | `def function_name(parameter):` |
| Use block in code | `function_name()` |
| Custom block with number input | `def function_name(size):` |

## 🏗️ Organizing Code with Functions

Functions help organize big programs:

```python
# BEFORE: Messy code all in one place
# Draw a house
# ... 20 lines of turtle commands ...

# AFTER: Organized with functions
def draw_house(size):
    draw_walls(size)
    draw_roof(size)
    draw_door(size)
    draw_windows(size)

def draw_walls(size):
    # ... code for walls ...

def draw_roof(size):
    # ... code for roof ...

# And so on...
```

## 🔧 Default Parameters

Make functions more flexible with default values:

```python
def draw_polygon(sides=4, size=100):
    """Draws a polygon with given sides and size"""
    angle = 360 / sides
    for i in range(sides):
        t.forward(size)
        t.left(angle)

# Use defaults
draw_polygon()          # Draws square (default)
draw_polygon(5)         # Draws pentagon, size=100
draw_polygon(6, 50)     # Draws hexagon, size=50
```

## 💡 Debugging Tips: Function Problems

- **"NameError: name 'draw_square' is not defined"**: You tried to use a function before defining it. Fix: Define functions before calling them.
- **"TypeError: draw_square() missing 1 required argument"**: You forgot to pass a parameter. Fix: Call with `draw_square(100)`.
- **"IndentationError"**: All code inside the function must be indented.
- **"Nothing happens"**: Did you remember to call the function with `()`?

## 📝 Session Checklist

- [ ] Defined a simple function with `def`
- [ ] Created a function with parameters
- [ ] Created a function that returns a value
- [ ] Built a shape drawing toolkit
- [ ] Created math helper functions
- [ ] Made pattern generator functions
- [ ] Used functions to organize code
- [ ] Used default parameters
- [ ] Called functions multiple times with different arguments

---

⏱️ **20-Minute Break Point**

*Great work! You've learned the key concepts. Take a short break if you need one. When you're ready, try the challenge problems to test your skills!*

---
## 🏆 Challenge Problems

**Bronze Challenge**: Create a `draw_snowflake()` function that draws a 6-armed snowflake using your `draw_star()` or other shape functions.

**Silver Challenge**: Build a `math_quiz()` function that takes a difficulty level (1=easy, 2=medium, 3=hard) and gives appropriate math problems.

**Gold Challenge**: Create a `draw_fractal()` function that draws a simple fractal tree using recursion (a function that calls itself!). Hint: Each branch splits into two smaller branches.

## 🔜 Next Time...

In Session 7, we'll learn about **lists** - the programmer's collection! We'll store multiple items together, work with sequences of data, and create awesome patterns with color palettes and coordinate lists.

**Remember**: Functions are your programming toolbox. The more tools you create, the more powerful you become!

---

*Parent Note: This session is designed in 20-minute chunks (marked with ⏱️ break points). Total session time: 45-60 minutes. Functions introduce abstraction - a key computer science concept. Help your child see functions as "black boxes": you put ingredients in (parameters), get results out (return values), without worrying about how it works inside. This is how real software is built!*