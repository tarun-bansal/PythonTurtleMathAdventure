# Session 3: User Input: Talking to Your Program

## 🎯 Learning Objectives
- Use `input()` to get data from the user
- Convert strings to integers with `int()`
- Create interactive drawings and games
- Handle errors when users type unexpected things
- Connect Scratch "ask and wait" to Python `input()`

## 🗣️ What is User Input?

Imagine your program is having a conversation with the person using it:
- Program: "What's your name?"
- User: "Alex"
- Program: "Hello, Alex! How old are you?"
- User: "9"
- Program: "Wow, 9 is a great age!"

This back-and-forth is called **user input**. It makes programs interactive and personal!

**Kid-Friendly Analogy**: "`input()` is like your program asking a question and waiting patiently for an answer. It's a conversation between human and computer!"

## 📝 The `input()` Function

The `input()` function:
1. Shows a message (optional)
2. Waits for the user to type something
3. Pressing Enter sends the answer back to your program

```python
# Simple input
name = input("What's your name? ")
print(f"Hello, {name}!")

# Input without a message
age = input()  # Just waits quietly
print(f"You typed: {age}")
```

## 🔢 Two Types of Input: Text vs Numbers

When you use `input()`, everything comes in as **text** (a string), even if you type numbers!

```python
# This creates TEXT, not a number
user_input = input("Enter a number: ")
# If you type "10", user_input is the TEXT "10", not the NUMBER 10
```

**Problem**: You can't do math with text "10"!

**Solution**: Convert text to numbers using `int()` (for whole numbers) or `float()` (for decimals):

```python
# Convert text to integer
text_number = input("Enter a number: ")
real_number = int(text_number)  # Convert "10" to 10
double = real_number * 2        # Now we can do math!
```

## 🐢 Interactive Turtle Graphics

Let's make turtle drawings that respond to user input!

### Example 1: Personalized Drawing
```python
import turtle

t = turtle.Turtle()

# Ask for the user's name
name = input("What's your name? ")

# Draw a personalized message
t.penup()
t.goto(-100, 0)
t.write(f"Hello, {name}!", font=("Arial", 24, "normal"))

# Ask for a size
size_text = input("How big should the square be? ")
size = int(size_text)  # Convert to number

# Draw a square of that size
t.penup()
t.goto(-size/2, -100)  # Center the square
t.pendown()

for i in range(4):
    t.forward(size)
    t.left(90)

turtle.done()
```

## 🧮 Exercise 1: Shape Generator

Create a program that asks for shape details and draws them:

```python
import turtle

t = turtle.Turtle()

# Ask questions
sides = int(input("How many sides? (3-10): "))
length = int(input("Side length? (10-200): "))
color = input("What color? (red/blue/green): ")

# Set up turtle
t.color(color)
t.pensize(3)

# Calculate angle
angle = 360 / sides

# Draw the shape
for i in range(sides):
    t.forward(length)
    t.left(angle)

turtle.done()
```

**Try this**: Make a triangle with side length 150, a pentagon with side length 80, etc.!

## 🎮 Exercise 2: Math Quiz Game

Let's make an interactive math quiz:

```python
import turtle

t = turtle.Turtle()
t.penup()
t.goto(-150, 100)
t.hideturtle()  # Hide the turtle, we only need text

score = 0

# Question 1
t.write("Question 1: What is 5 + 3?", font=("Arial", 16, "normal"))
answer1 = int(input("Your answer: "))

if answer1 == 8:
    score = score + 10
    t.goto(-150, 80)
    t.write("Correct! +10 points", font=("Arial", 16, "normal"))
else:
    t.goto(-150, 80)
    t.write(f"Wrong! The answer is 8", font=("Arial", 16, "normal"))

# Question 2
t.goto(-150, 40)
t.write("Question 2: What is 12 - 4?", font=("Arial", 16, "normal"))
answer2 = int(input("Your answer: "))

if answer2 == 8:
    score = score + 10
    t.goto(-150, 20)
    t.write("Correct! +10 points", font=("Arial", 16, "normal"))
else:
    t.goto(-150, 20)
    t.write(f"Wrong! The answer is 8", font=("Arial", 16, "normal"))

# Show final score
t.goto(-150, -20)
t.write(f"Final score: {score}/20", font=("Arial", 20, "bold"))

turtle.done()
```

**Challenge**: Add more questions! Make a multiplication question or division question.

## 🎨 Exercise 3: Interactive Pattern Generator

Create a program that makes custom patterns:

```python
import turtle

t = turtle.Turtle()
t.speed("fastest")

# Get pattern settings
repeat = int(input("How many repeats? (10-50): "))
step = int(input("Step size? (5-20): "))
angle = int(input("Turn angle? (1-179): "))

# Draw the pattern
for i in range(repeat):
    t.forward(step * i)  # Step gets bigger each time
    t.left(angle)

turtle.done()
```

**Experiment**: Try angle = 144 (makes a star), angle = 90 (makes a square spiral), angle = 121 (makes cool organic patterns).

## ⚠️ Handling Errors: When Users Type Weird Things

What if someone types "banana" when asked for a number? The program crashes! Let's make it more robust:

```python
# Simple error handling
try:
    number = int(input("Enter a number: "))
    print(f"Twice your number is {number * 2}")
except:
    print("That's not a valid number! Please enter digits like 10 or 5.")
```

**Kid-Friendly Analogy**: "The `try` block is like saying 'Let's try to do this...' and the `except` block is like 'If something goes wrong, do this instead.'"

## 🧠 Math Connection: Interactive Word Problems

Remember word problems in math? Now you can CREATE them!

```python
# Interactive word problem creator
print("Let's solve a word problem!")
print("Samantha has some apples. She gets 5 more. Now she has 12 apples.")

answer = int(input("How many apples did Samantha start with? "))

if answer == 7:
    print("Correct! 7 + 5 = 12")
else:
    print(f"Not quite. If she ended with 12 after getting 5 more, she started with 12 - 5 = 7")
```

**Challenge**: Create your own word problem about cookies, toys, or anything you like!

## 🎯 Scratch to Python Translation

| In Scratch you would... | In Python you write... |
|-------------------------|------------------------|
| "Ask 'What's your name?' and wait" block | `name = input("What's your name? ")` |
| "Answer" variable | Whatever you save the input to: `name = input(...)` |
| Use answer in "say" block | `print(f"Hello, {name}!")` |

## 💡 Debugging Tips: Input Problems

- **"ValueError: invalid literal for int()"**: User typed something that's not a number. Fix: Use `try`/`except` or check with `.isdigit()`.
- **"The program ends too fast"**: Add `input("Press Enter to exit...")` at the end.
- **"The input shows after the turtle window"**: Turtle graphics and text input sometimes don't mix well in some editors. Try running in Thonny's shell.

## 📝 Session Checklist

- [ ] Used `input()` to ask for text
- [ ] Used `input()` to ask for numbers
- [ ] Converted string input to integer with `int()`
- [ ] Created an interactive drawing
- [ ] Made a math quiz game
- [ ] Built a pattern generator
- [ ] Used `try`/`except` to handle errors
- [ ] Created an interactive word problem

## 🏆 Challenge Problems

**Bronze Challenge**: Make a program that asks for a favorite color and draws a square in that color.

**Silver Challenge**: Create a "mad libs" style story that asks for nouns, verbs, adjectives and creates a silly story.

**Gold Challenge**: Build a fully interactive drawing program that asks for shape type (square, triangle, circle), size, color, position, and draws it.

## 🔜 Next Time...

In Session 4, we'll learn about **loops** - the programmer's superpower for repeating things! We'll draw complex patterns, make multiplication tables, and create amazing geometric art without writing the same code over and over.

**Remember**: Interactive programs are like conversations. The better questions you ask, the more fun the conversation becomes!

---

*Parent Note: This session introduces real interactivity. Help your child think about good questions to ask users. Error handling (`try`/`except`) is advanced but introduced gently - focus on the concept of "what if someone types something unexpected?"*