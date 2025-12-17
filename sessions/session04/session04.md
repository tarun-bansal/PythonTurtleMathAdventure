# Session 4: Loops: The Programmer's Superpower

## 🎯 Learning Objectives
- Understand `for` loops with `range()`
- Draw repetitive patterns efficiently
- Use nested loops for complex patterns
- Compare with Scratch "repeat" blocks
- Create multiplication tables and geometric art

## 🔁 What is a Loop?

Imagine you need to tell your turtle:
"Walk forward 100 steps, turn left 90 degrees"
and you need to say this **4 times** to make a square.

Without loops, you'd write:
```python
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
t.forward(100); t.left(90)
```

With loops, you write:
```python
for i in range(4):
    t.forward(100)
    t.left(90)
```

**Kid-Friendly Analogy**: "Loops are like telling your turtle, 'Do this dance move 4 times' instead of saying the same thing 4 times. It's a programming superpower for repetition!"

## 📊 The `for` Loop with `range()`

The `for` loop repeats code a specific number of times:

```python
# Repeat 5 times
for i in range(5):
    print(f"This is repetition number {i}")
    # i will be 0, 1, 2, 3, 4
```

**Important**: `range(5)` gives numbers 0, 1, 2, 3, 4 (5 numbers total, starting at 0).

If you want 1, 2, 3, 4, 5:
```python
for i in range(1, 6):  # From 1 up to (but not including) 6
    print(i)
```

## 🐢 Turtle Graphics with Loops

### Example 1: Draw Any Polygon
```python
import turtle

t = turtle.Turtle()

sides = 8          # Try changing this!
length = 50
angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()
```

**Math Connection**: The angle formula `360 / sides` works for ANY regular polygon!

### Example 2: Concentric Circles
```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

for radius in range(10, 101, 10):  # 10, 20, 30, ..., 100
    t.circle(radius)

turtle.done()
```

## 🎨 Exercise 1: Multiplication Table Patterns

Let's visualize multiplication tables with turtle graphics!

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")
t.penup()

# Draw multiplication table for 7
table_of = 7

for i in range(1, 13):  # 1 through 12
    result = table_of * i

    # Move to position
    t.goto(i * 30 - 200, 100)  # X position based on i

    # Write the multiplication fact
    t.write(f"{table_of} × {i} = {result}", font=("Arial", 12, "normal"))

    # Draw a rectangle whose height represents the result
    t.goto(i * 30 - 200, 0)
    t.pendown()
    t.forward(20)  # Width
    t.right(90)
    t.forward(result * 2)  # Height scaled
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(result * 2)
    t.right(90)
    t.penup()

turtle.done()
```

**Try this**: Change `table_of` to 3, 5, 8, etc. Watch the pattern of heights!

## 🌟 Exercise 2: Geometric Mandala

Create beautiful symmetric patterns using nested loops:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw 6 circles around a center point
for i in range(6):
    t.color(colors[i])

    # Draw a circle
    t.circle(50)

    # Turn to next position
    t.left(60)  # 360 / 6 = 60 degrees

turtle.done()
```

**Challenge**: Add another loop inside to draw multiple circles at each position!

## 🌀 Exercise 3: Spiral Patterns

Loops can create amazing spirals by changing something each time:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

# Simple spiral
for i in range(100):
    t.forward(i * 2)  # Get longer each time
    t.left(91)        # Not 90° makes it spiral

turtle.done()
```

**Experiment**: Try different angles: 89°, 91°, 121°, 144°. Each creates a different spiral pattern!

## 🔄 Nested Loops: Loops Inside Loops

When you put one loop inside another, magic happens:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

# Draw a grid of dots
for x in range(5):      # 5 rows
    for y in range(5):  # 5 columns
        # Calculate position
        pos_x = x * 50 - 100
        pos_y = y * 50 - 100

        # Move to position and draw dot
        t.penup()
        t.goto(pos_x, pos_y)
        t.pendown()
        t.dot(20)

turtle.done()
```

**Kid-Friendly Analogy**: "Nested loops are like saying 'For every row, draw all the columns.' It's like planting a garden: for each row, plant seeds in every spot."

## 🧮 Math Connection: Patterns and Sequences

Loops are perfect for exploring mathematical patterns:

### Number Patterns
```python
# Print triangular numbers: 1, 3, 6, 10, 15...
total = 0
for i in range(1, 11):
    total = total + i
    print(f"Triangular number {i} is {total}")
```

### Fibonacci Sequence
```python
# Fibonacci: 1, 1, 2, 3, 5, 8, 13...
a = 1
b = 1
print(a)
print(b)

for i in range(10):
    c = a + b
    print(c)
    a = b
    b = c
```

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "Repeat 10" block | `for i in range(10):` |
| "Forever" block | `while True:` (we'll learn this later) |
| "Repeat until" block | `while condition:` (later) |
| Use "counter" variable | `for i in range(10):` (i is the counter) |

## 🔧 Loop Control: `break` and `continue`

Sometimes you want to stop early or skip an iteration:

```python
# Stop when we reach 5
for i in range(10):
    if i == 5:
        break  # Exit the loop completely
    print(i)

# Skip even numbers
for i in range(10):
    if i % 2 == 0:  # If i is even
        continue    # Skip to next iteration
    print(i)        # Only prints odd numbers
```

## 💡 Debugging Tips: Loop Problems

- **"Infinite loop"**: The program never stops. Fix: Make sure your loop condition eventually becomes false.
- **"Off by one error"**: `range(5)` gives 0-4, not 1-5. Fix: Use `range(1, 6)` for 1-5.
- **"Indentation error"**: Python cares about indentation! All code inside the loop must be indented exactly the same amount.

## 📝 Session Checklist

- [ ] Used `for i in range(5):` to repeat code
- [ ] Drew a polygon using a loop
- [ ] Created concentric circles
- [ ] Visualized multiplication tables
- [ ] Made a geometric mandala
- [ ] Created spiral patterns
- [ ] Used nested loops for a grid
- [ ] Explored number patterns with loops
- [ ] Used `break` to exit a loop early
- [ ] Used `continue` to skip iterations

## 🏆 Challenge Problems

**Bronze Challenge**: Create a program that draws 10 squares, each larger than the last.

**Silver Challenge**: Make a times table visualizer that shows ALL tables from 1-10 in a grid.

**Gold Challenge**: Create a "spirograph" program that uses nested loops to draw intricate circular patterns. Hint: One loop for circles, another for positions around a circle.

## 🔜 Next Time...

In Session 5, we'll learn about **conditionals** (if/else statements) - how to make programs that make decisions! We'll create guessing games, quizzes with feedback, and turtles that change behavior based on conditions.

**Remember**: Loops give you the superpower of repetition. With great power comes great responsibility (and awesome drawings)!

---

*Parent Note: Loops are a fundamental programming concept. Help your child visualize what's happening in each iteration. Use physical objects (marching toys, counting beads) to demonstrate repetition. The concept of starting at 0 (`range(5)` = 0-4) is important in computer science.*