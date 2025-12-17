# Session 5: Conditionals: Program Decision Making

## 🎯 Learning Objectives
- Use `if`, `elif`, and `else` statements
- Understand comparison operators (`>`, `<`, `==`, `!=`)
- Create branching programs that make decisions
- Use random numbers with `random.randint()`
- Connect Scratch "if-then" blocks to Python conditionals

## 🤔 What are Conditionals?

Imagine your program is at a crossroads:
- "If it's raining, bring an umbrella."
- "If you're hungry, eat a snack."
- "If your score is 100, show 'You win!'"

These "if-then" decisions are called **conditionals**. They let programs react differently to different situations.

**Kid-Friendly Analogy**: "Conditionals are like a choose-your-own-adventure book for your program. 'IF you turn left, you find treasure. ELSE IF you go straight, you meet a dragon. ELSE you stay safe at home.'"

## ⚖️ Comparison Operators

Before making decisions, we need to compare things:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `3 < 7` | `True` |
| `>=` | Greater than or equal | `5 >= 5` | `True` |
| `<=` | Less than or equal | `4 <= 4` | `True` |

**Important**: `==` (comparison) is different from `=` (assignment)!
- `x = 5` means "put 5 in the box labeled x"
- `x == 5` means "is what's in the box x equal to 5?"

## 🎮 The `if` Statement

The simplest conditional: "If this is true, do that."

```python
age = 9

if age >= 8:
    print("You're old enough to learn Python!")
```

**Indentation matters!** The code inside the `if` must be indented (usually 4 spaces).

## 🔀 `if-else` Statements

"What if the condition is false? Do something else!"

```python
score = 75

if score >= 80:
    print("Great job! You got an A!")
else:
    print("Good try! Keep practicing!")
```

## 🔀🔀 `if-elif-else` Statements

Multiple possible paths:

```python
grade = 85

if grade >= 90:
    print("A - Excellent!")
elif grade >= 80:
    print("B - Very good!")
elif grade >= 70:
    print("C - Good effort!")
elif grade >= 60:
    print("D - Needs improvement")
else:
    print("F - Let's try again")
```

**Note**: `elif` is short for "else if". Python checks each condition in order until one is true.

## 🎲 Random Numbers with `random.randint()`

To make games interesting, we need randomness:

```python
import random

# Generate random number between 1 and 10
secret_number = random.randint(1, 10)
print(f"Secret number: {secret_number}")

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
random_color = random.choice(colors)
print(f"Random color: {random_color}")
```

---

⏱️ **20-Minute Break Point**

*Great! You've learned the core concepts. Take a short break if you need one. When you're ready, continue with hands-on exercises to practice your new skills.*

---
## 🐢 Exercise 1: Random Walk Turtle

Create a turtle that randomly chooses directions:

```python
import turtle
import random

t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)

# Random walk for 50 steps
for i in range(50):
    # Randomly choose a direction
    direction = random.randint(1, 4)

    if direction == 1:
        t.forward(20)      # Forward
    elif direction == 2:
        t.backward(20)     # Backward
    elif direction == 3:
        t.left(90)         # Turn left
        t.forward(20)
    else:  # direction == 4
        t.right(90)        # Turn right
        t.forward(20)

turtle.done()
```

**Experiment**: Change the number of steps, step size, or add more directions!

## 🧮 Exercise 2: Math Quiz with Feedback

Improve our math quiz with personalized feedback:

```python
import turtle

t = turtle.Turtle()
t.penup()
t.hideturtle()
t.goto(-150, 100)

score = 0

print("=== MATH QUIZ ===")

# Question 1
answer1 = int(input("What is 7 × 8? "))

if answer1 == 56:
    score += 10
    t.write("✅ Correct! 7 × 8 = 56", font=("Arial", 14, "normal"))
    print("Perfect! You know your 7s table!")
else:
    t.write(f"❌ Actually, 7 × 8 = 56 (you said {answer1})", font=("Arial", 14, "normal"))
    print("Remember: 7 × 8 = 56")

# Move down for next question
t.goto(-150, 70)

# Question 2
answer2 = int(input("What is 15 - 9? "))

if answer2 == 6:
    score += 10
    t.write("✅ Correct! 15 - 9 = 6", font=("Arial", 14, "normal"))
    print("Great subtraction skills!")
elif answer2 > 6:
    t.write(f"❌ Too high! 15 - 9 = 6 (you said {answer2})", font=("Arial", 14, "normal"))
    print("Try subtracting a bit more...")
else:  # answer2 < 6
    t.write(f"❌ Too low! 15 - 9 = 6 (you said {answer2})", font=("Arial", 14, "normal"))
    print("Try subtracting a bit less...")

# Show final score
t.goto(-150, 40)
t.write(f"Final score: {score}/20", font=("Arial", 18, "bold"))

if score == 20:
    t.goto(-150, 10)
    t.write("🎉 PERFECT SCORE! 🎉", font=("Arial", 20, "bold"))
elif score >= 10:
    t.goto(-150, 10)
    t.write("Good job! 👍", font=("Arial", 16, "normal"))
else:
    t.goto(-150, 10)
    t.write("Keep practicing! 💪", font=("Arial", 16, "normal"))

turtle.done()
```

## 🎨 Exercise 3: Color-Changing Turtle

Make a turtle that changes color based on position:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")
t.pensize(3)

# Draw a spiral that changes color
for i in range(100):
    # Get current position
    x, y = t.position()

    # Change color based on position
    if x > 0 and y > 0:      # Quadrant I
        t.color("red")
    elif x < 0 and y > 0:    # Quadrant II
        t.color("blue")
    elif x < 0 and y < 0:    # Quadrant III
        t.color("green")
    elif x > 0 and y < 0:    # Quadrant IV
        t.color("purple")
    else:                    # On axes
        t.color("black")

    # Draw
    t.forward(i * 2)
    t.left(91)

turtle.done()
```

**Math Connection**: This uses the **coordinate plane quadrants** you learn in math!

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "If <> then" block | `if condition:` |
| "If <> then, else" block | `if condition: ... else: ...` |
| "Wait until <> " block | `while not condition:` (next session) |
| ">", "<", "=" operators | `>`, `<`, `==` |

---

⏱️ **20-Minute Break Point**

*Great job! You've practiced with hands-on exercises. Take a short break if you need one. When you're ready, continue with the math connection and Scratch translation.*

---
## 🧠 Math Connection: Inequalities and Number Lines

Conditionals are perfect for exploring inequalities:

```python
# Number line game
number = int(input("Enter a number between 1 and 100: "))

if number < 1:
    print("Too small! Must be at least 1")
elif number <= 25:
    print("In the first quarter [1-25]")
elif number <= 50:
    print("In the second quarter [26-50]")
elif number <= 75:
    print("In the third quarter [51-75]")
elif number <= 100:
    print("In the fourth quarter [76-100]")
else:
    print("Too big! Must be at most 100")
```

## 🔧 Logical Operators: `and`, `or`, `not`

Combine conditions:

```python
age = 9
has_permission = True

# Both must be true
if age >= 8 and has_permission:
    print("You can learn Python!")

# Either can be true
if age < 5 or age > 12:
    print("You're outside the typical 5-12 age range")

# Reverse a condition
if not has_permission:
    print("You need permission first")
```

## 💡 Debugging Tips: Conditional Problems

- **"SyntaxError: invalid syntax"**: Check you have `:` at the end of `if`, `elif`, `else`
- **"IndentationError"**: All code inside the conditional must be indented consistently
- **"Nothing happens when condition should be true"**: Check your comparison operator (`==` not `=`)
- **"Both if and else run"**: Impossible! Check your logic - maybe you have separate `if` statements instead of `if-elif-else`

## 📝 Session Checklist

- [ ] Used `if` to make simple decisions
- [ ] Used `if-else` for two choices
- [ ] Used `if-elif-else` for multiple choices
- [ ] Compared numbers with `>`, `<`, `==`, `!=`
- [ ] Generated random numbers with `random.randint()`
- [ ] Created a random walk turtle
- [ ] Made a math quiz with feedback
- [ ] Created a color-changing turtle based on position
- [ ] Used `and`, `or`, `not` to combine conditions
- [ ] Created a number line game

---

⏱️ **20-Minute Break Point**

*Great work! You've learned the key concepts. Take a short break if you need one. When you're ready, try the challenge problems to test your skills!*

---
## 🏆 Challenge Problems

**Bronze Challenge**: Create a guessing game where the computer picks a number 1-10 and the user guesses. Give "too high"/"too low" hints.

**Silver Challenge**: Make a turtle that draws different shapes based on user input: "s" for square, "t" for triangle, "c" for circle.

**Gold Challenge**: Create a "math obstacle course" where the turtle moves through a maze, and at each intersection, you must solve a math problem to choose the correct path.

## 🔜 Next Time...

In Session 6, we'll learn about **functions** - your code toolbox! We'll create reusable pieces of code, build our own commands, and organize programs into neat, manageable parts.

**Remember**: Programs that make decisions feel alive and responsive. The smarter your decisions, the smarter your program!

---

*Parent Note: This session is designed in 20-minute chunks (marked with ⏱️ break points). Total session time: 45-60 minutes. Conditionals introduce logical thinking. Help your child trace through different paths ("What if the number is 5? What if it's 15?"). The concept of Boolean logic (True/False) is foundational to computer science.*