# Session 7: Lists: The Programmer's Collection

## 🎯 Learning Objectives
- Create and manipulate lists
- Access elements with indices (starting at 0!)
- Loop through lists with `for` loops
- Use lists with turtle graphics
- Connect Scratch lists to Python lists

## 📦 What is a List?

Imagine you have a numbered row of lockers:
- Locker 0: Red crayon
- Locker 1: Blue crayon
- Locker 2: Green crayon
- Locker 3: Yellow crayon

This collection of items in order is called a **list**. Lists let you store multiple things together and access them by their position.

**Kid-Friendly Analogy**: "Lists are like a numbered line of lockers where you can store multiple items. Want your blue crayon? Get it from locker 1!"

## 📝 Creating Lists

Lists are created with square brackets `[]`:

```python
# List of numbers
test_scores = [95, 87, 92, 78, 100]

# List of strings
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# List of mixed types (less common)
mixed = [42, "hello", 3.14, True]

# Empty list
shopping_list = []
```

## 🔢 Accessing List Elements

Use the position number (called an **index**) to get items:

```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

print(colors[0])   # "red" - FIRST item at index 0
print(colors[1])   # "orange"
print(colors[2])   # "yellow"
print(colors[3])   # "green"
print(colors[4])   # "blue"
print(colors[5])   # "purple" - LAST item at index 5
```

**Important**: List indices start at 0, not 1! This is a fundamental computer science concept.

## 🔄 Looping Through Lists

Use `for` loops to process all items in a list:

```python
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Method 1: Loop through items directly
for color in colors:
    print(f"I like {color}")

# Method 2: Loop through indices
for i in range(len(colors)):
    print(f"Color {i} is {colors[i]}")
```

## 📊 List Operations

Lists have many useful operations:

```python
numbers = [10, 20, 30]

# Add to end
numbers.append(40)        # [10, 20, 30, 40]

# Insert at position
numbers.insert(1, 15)     # [10, 15, 20, 30, 40]

# Remove item
numbers.remove(20)        # [10, 15, 30, 40]

# Get length
count = len(numbers)      # 4

# Check if item exists
if 30 in numbers:
    print("30 is in the list!")

# Find position
position = numbers.index(30)  # 2
```

## 🐢 Exercise 1: Rainbow Turtle

Use a color list to create rainbow drawings:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")
t.pensize(5)

# Color palette
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw rainbow circles
radius = 20
for color in rainbow:
    t.color(color)
    t.circle(radius)
    radius += 20  # Each circle bigger
    t.penup()
    t.forward(10)  # Move right a bit
    t.pendown()

turtle.done()
```

**Challenge**: Make a rainbow spiral by changing colors as you draw!

## 📐 Exercise 2: Polygon Side Lengths

Store polygon side lengths in a list:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

# Different polygons with their side lengths
polygons = [
    [100, 100, 100, 100],           # Square
    [100, 100, 100],               # Triangle
    [100, 100, 100, 100, 100],     # Pentagon
    [100, 100, 100, 100, 100, 100] # Hexagon
]

# Draw each polygon
x_position = -300
for sides in polygons:
    t.penup()
    t.goto(x_position, 0)
    t.pendown()

    # Draw this polygon
    for side_length in sides:
        t.forward(side_length)
        t.left(360 / len(sides))  # Turn angle based on number of sides

    # Move right for next polygon
    x_position += 200

turtle.done()
```

## 🎮 Exercise 3: Connect the Dots Game

Create a game from coordinate lists:

```python
import turtle

t = turtle.Turtle()
t.speed("slow")
t.pensize(3)
t.hideturtle()

# List of (x, y) coordinates
points = [
    (-100, 100),   # Top-left
    (100, 100),    # Top-right
    (100, -100),   # Bottom-right
    (-100, -100),  # Bottom-left
    (-100, 100)    # Back to start
]

# Draw the points
t.penup()
for (x, y) in points:
    t.goto(x, y)
    t.dot(10, "red")  # Draw red dot
    t.write(f"({x}, {y})", font=("Arial", 10, "normal"))

# Connect the dots
t.penup()
t.goto(points[0])  # Go to first point
t.pendown()
t.color("blue")

for (x, y) in points:
    t.goto(x, y)

turtle.done()
```

**Challenge**: Create your own shape by changing the coordinates!

## 🧮 Math Connection: Statistics with Lists

Lists are perfect for math calculations:

```python
# Calculate statistics
grades = [95, 87, 92, 78, 100, 88, 91]

# Sum
total = sum(grades)
print(f"Total: {total}")

# Average
average = total / len(grades)
print(f"Average: {average:.1f}")  # .1f means 1 decimal place

# Minimum and maximum
lowest = min(grades)
highest = max(grades)
print(f"Range: {lowest} to {highest}")

# Sort
sorted_grades = sorted(grades)
print(f"Sorted: {sorted_grades}")
```

## 🔄 List Slicing

Get parts of a list using slicing:

```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(numbers[2:5])    # [30, 40, 50] - indices 2,3,4
print(numbers[:3])     # [10, 20, 30] - first 3
print(numbers[7:])     # [80, 90, 100] - from index 7 to end
print(numbers[::2])    # [10, 30, 50, 70, 90] - every 2nd item
print(numbers[::-1])   # [100, 90, ..., 10] - reversed!
```

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "Make a list" button | `my_list = []` |
| "Add thing to list" block | `my_list.append(thing)` |
| "Delete 1 of list" block | `my_list.pop(1)` |
| "Item 1 of list" block | `my_list[0]` (remember: 0-indexed!) |
| "Length of list" block | `len(my_list)` |

## 💡 Debugging Tips: List Problems

- **"IndexError: list index out of range"**: You tried to access `list[10]` but list only has 5 items. Fix: Check `len(list)` first.
- **"TypeError: 'list' object is not callable"**: You used `list()` as a variable name, then tried to call it. Fix: Don't use `list` as a variable name.
- **"Nothing changes when I modify list in loop"**: If modifying while looping, make a copy: `for item in list.copy():`
- **"List seems empty"**: Did you `append()` or just create empty list?

## 📝 Session Checklist

- [ ] Created lists of numbers and strings
- [ ] Accessed list elements by index (starting at 0)
- [ ] Looped through lists with `for` loops
- [ ] Used list operations: `append()`, `insert()`, `remove()`, `len()`
- [ ] Created rainbow turtle drawings
- [ ] Stored polygon side lengths in lists
- [ ] Made a connect-the-dots game
- [ ] Calculated statistics (sum, average, min, max)
- [ ] Used list slicing
- [ ] Checked if items exist with `in`

## 🏆 Challenge Problems

**Bronze Challenge**: Create a program that stores 5 friend names in a list, then prints a greeting for each friend.

**Silver Challenge**: Make a "math facts practice" program that stores problems and answers in lists, then quizzes the user.

**Gold Challenge**: Create a "graph plotter" that takes a list of y-values and draws a line graph using turtle. Bonus: Plot mathematical functions like y = x²!

## 🔜 Next Time...

In Session 8, we'll explore **advanced math operations** and problem solving! We'll learn about integer division, remainders, exponents, and the math module. Get ready for some serious math-programming fusion!

**Remember**: Lists are your programming toolbox for collections. The more organized your data, the more powerful your programs!

---

*Parent Note: The concept of 0-based indexing is critical in computer science. Help your child visualize indices as "positions from the start" rather than "which item". Lists introduce data structures - a fundamental CS concept.*