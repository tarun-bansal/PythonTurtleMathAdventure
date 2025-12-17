# Session 8: Math Operations & Problem Solving

## 🎯 Learning Objectives
- Use advanced math operators (`//`, `%`, `**`)
- Import and use functions from the `math` module
- Solve programming puzzles and challenges
- Debug complex programs
- Apply mathematical thinking to programming problems

💡 **Session Note**: This session covers many concepts. Take breaks at the ⏱️ markers to avoid overload.

## 🧮 Advanced Math Operators

Python has special math operators beyond `+`, `-`, `*`, `/`:

### Integer Division (`//`)
Divides and chops off the decimal part (rounds down):

```python
print(10 // 3)   # 3 (not 3.333...)
print(17 // 5)   # 3
print(9 // 2)    # 4
```

**Kid-Friendly Analogy**: "`//` is like sharing cookies: If you have 10 cookies and 3 friends, each gets 3 whole cookies (and 1 is left over)."

### Modulus (`%`)
Gives the remainder after division:

```python
print(10 % 3)    # 1 (10 ÷ 3 = 3 remainder 1)
print(17 % 5)    # 2 (17 ÷ 5 = 3 remainder 2)
print(9 % 2)     # 1 (9 ÷ 2 = 4 remainder 1)
```

**Kid-Friendly Analogy**: "`%` is the leftover cookie after sharing. If 10 cookies shared among 3 friends, each gets 3 cookies, and 1 cookie is left over."

### Exponentiation (`**`)
Raises to a power:

```python
print(2 ** 3)    # 8 (2³ = 2 × 2 × 2)
print(5 ** 2)    # 25 (5² = 5 × 5)
print(10 ** 0)   # 1 (any number⁰ = 1)
```

## 📊 The `math` Module

Python has a built-in `math` module with more advanced functions:

```python
import math

# Common math functions
print(math.sqrt(25))      # 5.0 (square root)
print(math.pow(2, 3))     # 8.0 (2³)
print(math.pi)            # 3.141592653589793
print(math.floor(3.7))    # 3 (round down)
print(math.ceil(3.2))     # 4 (round up)
print(math.fabs(-5))      # 5.0 (absolute value)
```

---

⏱️ **20-Minute Break Point**

*Great! You've learned the core concepts. Take a short break if you need one. When you're ready, continue with hands-on exercises to practice your new skills.*

---
## 🐢 Exercise 1: Prime Number Visualizer

Create a visual representation of prime numbers:

```python
import turtle
import math

t = turtle.Turtle()
t.speed("fastest")
t.penup()

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Draw prime numbers in a grid
size = 20  # Size of each square
count = 0

for num in range(1, 101):  # Check numbers 1-100
    # Calculate grid position
    row = count // 10  # Which row (0-9)
    col = count % 10   # Which column (0-9)

    # Move to position
    x = col * size - 150
    y = 150 - row * size
    t.goto(x, y)

    # Draw square
    if is_prime(num):
        t.color("red")
        t.fillcolor("lightcoral")
    else:
        t.color("blue")
        t.fillcolor("lightblue")

    t.begin_fill()
    for _ in range(4):
        t.forward(size - 2)  # Slightly smaller than grid cell
        t.right(90)
    t.end_fill()

    # Write the number
    t.penup()
    t.goto(x + size/2, y - size/2 - 5)
    t.color("black")
    t.write(str(num), align="center", font=("Arial", 8, "normal"))
    t.penup()

    count += 1

t.hideturtle()
turtle.done()
```

**Math Connection**: This visualizes the **Sieve of Eratosthenes** - an ancient algorithm for finding primes!

## 🔢 Exercise 2: Fibonacci Spiral

Draw the famous Fibonacci spiral using the golden ratio:

```python
import turtle
import math

t = turtle.Turtle()
t.speed("slowest")
t.pensize(2)

# Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
fib = [1, 1]
for i in range(8):  # Generate more numbers
    fib.append(fib[-1] + fib[-2])

print(f"Fibonacci numbers: {fib}")

# Draw squares and arcs
x, y = 0, 0
angle = 0

for i, num in enumerate(fib):
    # Draw square
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.color("black", "lightyellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(num * 5)  # Scale for visibility
        t.left(90)
    t.end_fill()

    # Draw quarter circle (arc)
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.color("red")
    t.circle(num * 5, 90)  # 90 degree arc

    # Update position for next square
    if i % 4 == 0:      # Right side
        x += num * 5
    elif i % 4 == 1:    # Top side
        y += num * 5
    elif i % 4 == 2:    # Left side
        x -= num * 5
    elif i % 4 == 3:    # Bottom side
        y -= num * 5

    angle -= 90  # Turn for next square

t.hideturtle()
turtle.done()
```

**Math Connection**: The Fibonacci sequence appears in nature (pinecones, sunflowers) and approximates the golden ratio (φ ≈ 1.618).

## 📈 Exercise 3: Times Table Visualization

Create an interactive times table visualization:

```python
import turtle
import math

t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()

def draw_times_table(factor, points=200):
    """Draw a times table pattern for given factor"""
    t.clear()
    t.penup()

    # Draw points around a circle
    for i in range(points):
        angle = 2 * math.pi * i / points  # Angle in radians

        # Calculate position on circle
        x1 = 200 * math.cos(angle)
        y1 = 200 * math.sin(angle)

        # Calculate connected point (i × factor)
        j = (i * factor) % points
        angle2 = 2 * math.pi * j / points
        x2 = 200 * math.cos(angle2)
        y2 = 200 * math.sin(angle2)

        # Draw line connecting the points
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

# Interactive loop
print("Times Table Visualizer")
print("Enter a number (2-100) or 'q' to quit")

while True:
    user_input = input("Enter factor: ")

    if user_input.lower() == 'q':
        break

    try:
        factor = int(user_input)
        if 2 <= factor <= 100:
            draw_times_table(factor)
        else:
            print("Please enter 2-100")
    except ValueError:
        print("Please enter a number")

turtle.done()
```

**Experiment**: Try factors like 2, 3, 5, 7, 11, 13. Prime numbers create beautiful symmetric patterns!

## 🧩 Programming Puzzles

### Puzzle 1: FizzBuzz
A classic programming interview question!

```python
# Print numbers 1-100, but:
# - If divisible by 3, print "Fizz"
# - If divisible by 5, print "Buzz"
# - If divisible by both, print "FizzBuzz"

for i in range(1, 101):
    if i % 15 == 0:  # Divisible by 3 AND 5
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

### Puzzle 2: Collatz Conjecture
A famous unsolved math problem!

```python
def collatz(n):
    """Apply Collatz rules: if even ÷2, if odd ×3+1"""
    steps = 0
    while n != 1:
        if n % 2 == 0:  # Even
            n = n // 2
        else:           # Odd
            n = n * 3 + 1
        steps += 1
        print(f"Step {steps}: {n}")
    return steps

# Try different starting numbers
print(f"Steps for 6: {collatz(6)}")
print(f"Steps for 27: {collatz(27)}")  # Takes 111 steps!
```

## 🎯 Math Module Deep Dive

Explore more `math` functions:

```python
import math

# Trigonometry (angles in radians)
print(math.sin(math.pi/2))   # 1.0 (sin 90°)
print(math.cos(math.pi))     # -1.0 (cos 180°)
print(math.tan(math.pi/4))   # 1.0 (tan 45°)

# Logarithms
print(math.log(100))         # Natural log of 100
print(math.log10(100))       # Base-10 log (2.0)

# Degrees/radians conversion
print(math.degrees(math.pi)) # 180.0
print(math.radians(90))      # 1.5707... (π/2)

# Constants
print(math.e)                # 2.718... (Euler's number)
print(math.tau)              # 6.283... (2π)
```

## 💡 Debugging Tips: Math Problems

- **"ZeroDivisionError"**: Divided by zero. Fix: Check denominator before dividing.
- **"ValueError: math domain error"**: Tried `math.sqrt(-1)`. Fix: Check input is non-negative.
- **"Floating point precision issues"**: `0.1 + 0.2 != 0.3` due to binary representation. Fix: Use `round()` or compare with tolerance.
- **"Integer overflow"**: Python handles big integers automatically! Try `2 ** 1000` - it works!

## 📝 Session Checklist

- [ ] Used integer division (`//`) and modulus (`%`)
- [ ] Used exponentiation (`**`)
- [ ] Imported and used the `math` module
- [ ] Created a prime number visualizer
- [ ] Drew a Fibonacci spiral
- [ ] Made an interactive times table visualization
- [ ] Solved the FizzBuzz puzzle
- [ ] Explored the Collatz conjecture
- [ ] Used trigonometry and logarithms
- [ ] Handled math-related errors

---

⏱️ **20-Minute Break Point**

*Great work! You've learned the key concepts. Take a short break if you need one. When you're ready, try the challenge problems to test your skills!*

---
## 🏆 Challenge Problems

**Bronze Challenge**: Create a program that converts between decimal, binary, and hexadecimal numbers using division and modulus.

**Silver Challenge**: Write a program that approximates π using the Monte Carlo method (random points in a square/circle).

**Gold Challenge**: Create a "graphing calculator" that plots any mathematical function the user enters (like y = x² or y = sin(x)).

## 🔜 Next Time...

In Session 9, we'll learn about **animation** - bringing drawings to life! We'll create moving patterns, bouncing balls, and interactive animations that respond to user input.

**Remember**: Mathematics is the language of programming. The better you understand math, the more powerful your programs become!

---

*Parent Note: This session is designed in 20-minute chunks (marked with ⏱️ break points). Total session time: 45-60 minutes. This session connects advanced math concepts to programming. The modulo operator (`%`) is particularly important in computer science (hashing, cryptography, cyclic patterns). Encourage mathematical thinking as problem-solving.*