# Session 2: Variables: The Programmer's Memory Box

## 🎯 Learning Objectives
- Create and use variables to store numbers and words
- Understand `=` as assignment (putting something IN the box)
- Use variables in turtle commands
- Do basic arithmetic in Python
- Connect Scratch variables to Python variables

## 📦 What is a Variable?

Imagine you have a magic box with a label on it. You can:
1. Put something in the box (like the number 100)
2. Look inside later to see what's there
3. Change what's in the box whenever you want

In programming, these magic boxes are called **variables**. The label is the **variable name**, and what's inside is the **value**.

**Kid-Friendly Analogy**: "Variables are like labeled boxes where you store numbers or words to use later. Want to remember your score in a game? Put it in a box called `score`!"

## 🏷️ Naming Your Variables

Variable names should be:
- **Descriptive**: `side_length` is better than `x`
- **Lowercase with underscores**: `my_score` not `MyScore`
- **No spaces**: Use underscores instead
- **Not Python keywords**: Don't use words like `print` or `if`

Good names: `player_score`, `circle_radius`, `angle_size`
Bad names: `a`, `b`, `c` (too vague!), `my variable` (has space)

## 🔤 Two Types of Variables (for now)

1. **Number variables**: Store integers (whole numbers) or decimals
   ```python
   score = 100
   pi = 3.14159
   ```

2. **String variables**: Store text (letters, words, sentences)
   ```python
   player_name = "Alex"
   greeting = "Hello, turtle friend!"
   ```

**Math Connection**: In algebra, you use letters like `x` and `y` to represent unknown numbers. Programming variables are similar, but we can store any value, not just numbers!

## 📝 Creating and Using Variables

### Example 1: Storing a Number
```python
# Create a variable called "steps" and put 50 in it
steps = 50

# Now use it with turtle
import turtle
t = turtle.Turtle()
t.forward(steps)  # The turtle moves 50 steps!
```

### Example 2: Changing a Variable
```python
size = 100
t.forward(size)  # Move 100 steps

size = 50        # Change what's in the box
t.forward(size)  # Now move 50 steps
```

**Important**: `=` means "put this value in this box", NOT "these are equal" like in math!

## 🧮 Math with Variables

You can do math with variables just like with numbers:

```python
# Basic arithmetic
a = 10
b = 5

sum = a + b          # 10 + 5 = 15
difference = a - b   # 10 - 5 = 5
product = a * b      # 10 × 5 = 50
quotient = a / b     # 10 ÷ 5 = 2.0

# You can even update a variable using itself!
score = 0
score = score + 10   # score is now 10
score = score + 5    # score is now 15
```

## 🐢 Turtle Graphics with Variables

Variables make turtle graphics more flexible! Instead of writing:
```python
t.forward(100)
t.left(90)
t.forward(100)
```

You can write:
```python
side = 100
angle = 90

t.forward(side)
t.left(angle)
t.forward(side)
```

Now you can change the shape just by changing the variables!

## ✨ Hands-on Exercise: Scalable Shapes

Let's create a program that draws shapes of any size using variables:

```python
import turtle

t = turtle.Turtle()

# Variables control the shape
side_length = 150
turn_angle = 90

# Draw a square using variables
t.forward(side_length)
t.left(turn_angle)
t.forward(side_length)
t.left(turn_angle)
t.forward(side_length)
t.left(turn_angle)
t.forward(side_length)
t.left(turn_angle)

turtle.done()
```

**Try this**: Change `side_length` to 75 or 200. Change `turn_angle` to 60 or 120. What shapes do you get?

## 🎮 Exercise 1: The Growing Spiral

Create a spiral that grows bigger with each turn:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

step = 10  # Starting step size

for i in range(20):  # We'll learn about loops next time!
    t.forward(step)
    t.left(90)
    step = step + 5  # Make the next step bigger

turtle.done()
```

**Challenge**: Can you make it turn a different angle? Try 89 degrees instead of 90!

## 📐 Exercise 2: Perfect Polygon Calculator

Remember from Session 1: For an n-sided polygon, each turn = 360 ÷ n degrees.

Let's write a program that calculates this automatically:

```python
import turtle

t = turtle.Turtle()

# Variables
num_sides = 6        # Try changing this: 3=triangle, 5=pentagon, 8=octagon
side_length = 100

# Calculate the turn angle
angle = 360 / num_sides

# Draw the polygon
for i in range(num_sides):
    t.forward(side_length)
    t.left(angle)

turtle.done()
```

**Math Connection**: This is **division in action**! We're using the formula we discovered last session.

## 🔢 Exercise 3: Math Challenge Game

Create a simple math game that uses variables:

```python
import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, 100)  # Move to starting position

# Game variables
score = 0
question_number = 1

# Ask math questions (we'll make this interactive next session!)
answer1 = 5 + 3   # 8
answer2 = 12 - 4  # 8
answer3 = 2 * 4   # 8

# Display the score
t.write(f"Score: {score}", font=("Arial", 16, "normal"))

turtle.done()
```

## 🧠 Math Connection: Algebra Comes Alive!

Variables in programming are exactly like variables in algebra:
- In algebra: `x + 5 = 12`, solve for `x`
- In programming: `x = 12 - 5`, Python calculates `x = 7`

But programming variables are MORE powerful:
- They can store text: `name = "Emma"`
- They can change: `score = score + 10`
- They can control graphics: `t.forward(step_size)`

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "Make a variable" button | `score = 0` |
| "Set score to 100" block | `score = 100` |
| "Change score by 10" block | `score = score + 10` |
| Use variable in "move steps" block | `t.forward(steps)` |

## 💡 Debugging Tips: Variable Problems

- **"NameError: name 'score' is not defined"**: You tried to use a variable before creating it. Fix: Add `score = 0` at the beginning.
- **"SyntaxError: can't assign to literal"**: You wrote something like `10 = x`. Fix: Variables must be on the left: `x = 10`.
- **"TypeError: must be str, not int"**: You mixed text and numbers. Fix: Use `str()` to convert: `print("Score: " + str(score))`

## 📝 Session Checklist

- [ ] Created a variable to store a number
- [ ] Created a variable to store text
- [ ] Used variables in turtle commands
- [ ] Did math with variables (+, -, *, /)
- [ ] Changed a variable's value
- [ ] Drew a scalable shape using variables
- [ ] Created a growing spiral
- [ ] Made a polygon calculator

## 🏆 Challenge Problems

**Bronze Challenge**: Create a program that draws three squares of different sizes using the same `side_length` variable (change it between squares).

**Silver Challenge**: Make a "scoreboard" that shows a player's name and score using turtle's `write()` function.

**Gold Challenge**: Create a program that draws a house with variables for `wall_size`, `roof_height`, and `door_width`. Change one variable to make a bigger or smaller house!

## 🔜 Next Time...

In Session 3, we'll learn about **user input** - how to make programs that ask questions and respond to answers! We'll create interactive math quizzes and games.

**Remember**: Variables are your programming memory. The more you use them, the more powerful your programs become!

---

*Parent Note: This session introduces foundational programming concepts. The equal sign (`=`) as assignment is different from math equality - emphasize this distinction. Encourage experimentation with different values.*