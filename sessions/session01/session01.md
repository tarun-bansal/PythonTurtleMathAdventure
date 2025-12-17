# Session 1: Meet Your Digital Turtle

## 🎯 Learning Objectives
- Install/set up Python with turtle graphics
- Understand coordinate system (0,0 at center)
- Learn basic commands: `forward()`, `backward()`, `left()`, `right()`
- Run your first Python program!
- Connect Scratch movement to Python turtle commands

## 🐢 What is a Digital Turtle?

Imagine you have a little robot turtle that holds a pen. You can tell it:
- "Walk forward 100 steps"
- "Turn left 90 degrees"
- "Walk backward 50 steps"

The turtle draws a line wherever it walks! This is called **turtle graphics**, and it's a fun way to learn programming because you can SEE what your code does immediately.

**Kid-Friendly Analogy**: "The turtle is like a remote-controlled robot that follows your exact instructions. You're the commander, and the turtle is your obedient drawing assistant!"

## 🔧 Setup Checklist (with Parent Help)

✅ **Step 1: Install Python**
- Ask a parent to help you install Python 3 from [python.org](https://python.org)
- Make sure to check "Add Python to PATH" during installation

✅ **Step 2: Install Thonny (Recommended)**
- Thonny is a friendly editor for beginners
- Download from [thonny.org](https://thonny.org)
- It has Python and turtle graphics built in!

✅ **Step 3: Test Your Setup**
Open Thonny and type this in the main window:
```python
import turtle
print("Python is working! 🎉")
```
Click the green Run button. If you see "Python is working! 🎉" then you're ready!


---

⏱️ **20-Minute Break Point**

*Great job! You've set up Python and Thonny. Take a short break if you need one. When you're ready, continue with the next section to learn about coordinates and basic turtle commands.*

---
## 📍 The Coordinate System

Think of your computer screen as a giant grid:
- The center is **(0, 0)** - that's where the turtle starts
- Moving **right** increases the x-coordinate: (100, 0)
- Moving **up** increases the y-coordinate: (0, 100)
- Moving **left** decreases the x-coordinate: (-100, 0)
- Moving **down** decreases the y-coordinate: (0, -100)

**Math Connection**: This is the **coordinate plane** you might have learned in math class! We use (x, y) coordinates to describe positions.

## 🎮 Basic Turtle Commands

| Command | What it does | Scratch Equivalent |
|---------|-------------|-------------------|
| `forward(100)` | Move forward 100 steps | "move 100 steps" block |
| `backward(50)` | Move backward 50 steps | "move -100 steps" block |
| `left(90)` | Turn left 90 degrees | "turn ↺ 90 degrees" block |
| `right(45)` | Turn right 45 degrees | "turn ↻ 45 degrees" block |
| `penup()` | Lift the pen (stop drawing) | "pen up" block |
| `pendown()` | Lower the pen (start drawing) | "pen down" block |

## ✨ Your First Program: Draw a Square!

Let's write a program to draw a square. In Thonny, type this code:

```python
import turtle

# Create our turtle friend
t = turtle.Turtle()

# Draw a square
t.forward(100)  # Move forward 100 steps
t.left(90)      # Turn left 90 degrees
t.forward(100)  # Move forward 100 steps
t.left(90)      # Turn left 90 degrees
t.forward(100)  # Move forward 100 steps
t.left(90)      # Turn left 90 degrees
t.forward(100)  # Move forward 100 steps
t.left(90)      # Turn left 90 degrees

# Keep the window open
turtle.done()
```

**Click the green Run button!** You should see a square appear!


---

⏱️ **20-Minute Break Point**

*Excellent! You've drawn your first square with Python. Take a short break if you need one. When you're ready, continue with the next section to learn about angles and hands-on exercises.*

---
## 🧩 Why 90 Degrees?

A square has 4 sides and 4 corners. Each corner is a **90-degree angle**. That's why we turn 90 degrees after drawing each side!

**Math Connection**: 90° is called a **right angle**. Squares and rectangles have four right angles.

## 🎨 Hands-on Exercises

### Exercise 1: Draw Your Initials
Try to draw the first letter of your name using only `forward()`, `backward()`, `left()`, and `right()` commands.

**Tip**: Use `penup()` and `pendown()` to move without drawing when you need to start a new line.

### Exercise 2: The "Get Lost" Challenge
Write a program that makes the turtle walk in a random path. Can you make it look like the turtle is lost?

```python
import turtle

t = turtle.Turtle()

# Try changing these numbers and see what happens!
t.forward(50)
t.left(30)
t.forward(75)
t.right(45)
t.backward(25)
# Add more commands here...

turtle.done()
```

### Exercise 3: Shape Detective
What shape do you get with this code?
```python
import turtle

t = turtle.Turtle()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
turtle.done()
```
Try to guess before running it! Then modify it to draw different shapes.

## 🧠 Math Connection: Geometry in Action

Turtle graphics is all about **geometry**:
- **Distance**: How far the turtle moves (steps/pixels)
- **Angles**: How much the turtle turns (degrees)
- **Shapes**: Combining straight lines at specific angles

**Challenge**: Can you figure out what angle you need to turn to draw:
- A triangle? (Hint: 3 sides)
- A pentagon? (5 sides)
- A hexagon? (6 sides)

**Formula**: For any polygon with n sides, each turn = 360 ÷ n degrees!


---

⏱️ **20-Minute Break Point**

*Great work! You've explored geometry concepts and hands-on exercises. Take a short break if you need one. When you're ready, continue with the Scratch to Python translation and challenge problems.*

---
## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| Use "move 100 steps" block | `t.forward(100)` |
| Use "turn ↺ 90 degrees" block | `t.left(90)` |
| Use "turn ↻ 45 degrees" block | `t.right(45)` |
| Use "pen up" block | `t.penup()` |
| Use "pen down" block | `t.pendown()` |

## 💡 Pro Tip: Fixing Mistakes

Made a mistake? No problem! Programmers make mistakes all the time. Here's how to fix common issues:

- **"Nothing happens when I run"**: Did you remember `import turtle` at the top?
- **"The window closes too fast"**: Add `turtle.done()` at the end
- **"I want to start over"**: Add `t.clear()` to erase everything

## 📝 Session Checklist

- [ ] Installed Python and Thonny (with parent help)
- [ ] Ran the test program successfully
- [ ] Drew a square with turtle commands
- [ ] Drew the first letter of my name
- [ ] Tried the "Get Lost" challenge
- [ ] Discovered what shape 120-degree turns make

## 🏆 Challenge Problems

**Bronze Challenge**: Draw a rectangle (different length and width)

**Silver Challenge**: Draw a star shape (hint: turn 144 degrees each time)

**Gold Challenge**: Draw your name in block letters using only turtle commands!

## 🔜 Next Time...

In Session 2, we'll learn about **variables** - the programmer's memory boxes! We'll use them to draw shapes of any size without rewriting all our code.

**Remember**: Programming is like learning a new language or musical instrument. It takes practice, but it's super fun once you get the hang of it!

---

*Parent Note: This session is designed in 20-minute chunks (marked with ⏱️ break points). Total session time: 45-60 minutes. Let your child explore and make mistakes - debugging is an important skill! The most important goal is maintaining excitement and curiosity.*