# Session 11: Game Design: Math Challenges

## 🎯 Learning Objectives
- Combine all programming concepts into a complete game
- Handle user interaction and game state
- Create scoring systems and game logic
- Implement game loops and levels
- Design engaging math-based games

## 🎮 What Makes a Good Game?

A good game needs:
1. **Clear goal**: What players try to achieve
2. **Rules**: How players can achieve it
3. **Feedback**: How players know how they're doing
4. **Challenge**: Not too easy, not too hard
5. **Fun!**: Enjoyable to play

**Kid-Friendly Analogy**: "Game design is like being both the rule-maker and player. You create the playground, then get to play in it!"

## 🔄 The Game Loop

Most games follow this pattern:
```python
initialize_game()

while game_not_over():
    handle_input()
    update_game_state()
    draw_everything()
    check_win_conditions()

show_final_score()
```

---

⏱️ **20-Minute Break Point**

*Great! You've learned the core concepts. Take a short break if you need one. When you're ready, continue with hands-on exercises to practice your new skills.*

---
## 🧮 Exercise 1: Math Fact Practice Game

Create a game that helps practice math facts with increasing difficulty:

```python
import turtle
import random
import time

# Setup
screen = turtle.Screen()
screen.setup(600, 400)
screen.tracer(0)

# Game variables
score = 0
level = 1
lives = 3
current_problem = None
answer = ""
game_over = False

# Create turtles for display
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(-250, 150)

problem_turtle = turtle.Turtle()
problem_turtle.hideturtle()
problem_turtle.penup()
problem_turtle.goto(0, 50)

input_turtle = turtle.Turtle()
input_turtle.hideturtle()
input_turtle.penup()
input_turtle.goto(0, -50)

feedback_turtle = turtle.Turtle()
feedback_turtle.hideturtle()
feedback_turtle.penup()
feedback_turtle.goto(0, -100)

lives_turtle = turtle.Turtle()
lives_turtle.hideturtle()
lives_turtle.penup()
lives_turtle.goto(200, 150)

def generate_problem(level):
    """Generate math problem based on level"""
    if level == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "+"
        correct = a + b
    elif level == 2:
        a = random.randint(10, 50)
        b = random.randint(1, 10)
        op = "-"
        correct = a - b
    else:  # level >= 3
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "×"
        correct = a * b

    problem = f"{a} {op} {b} = ?"
    return problem, correct

def update_display():
    """Update all game displays"""
    score_turtle.clear()
    score_turtle.write(f"Score: {score}\nLevel: {level}",
                      font=("Arial", 16, "normal"))

    lives_turtle.clear()
    lives_turtle.write(f"Lives: {'♥' * lives}",
                      font=("Arial", 16, "normal"))

    problem_turtle.clear()
    if current_problem:
        problem_turtle.write(current_problem[0],
                           font=("Arial", 24, "bold"))

    input_turtle.clear()
    input_turtle.write(f"Your answer: {answer}",
                      font=("Arial", 18, "normal"))

    screen.update()

def check_answer():
    """Check if answer is correct"""
    global score, level, lives, current_problem, answer

    if not current_problem or not answer:
        return

    try:
        user_answer = int(answer)
        _, correct_answer = current_problem

        if user_answer == correct_answer:
            # Correct!
            score += 10 * level
            feedback_turtle.clear()
            feedback_turtle.color("green")
            feedback_turtle.write("Correct! +10 points",
                                font=("Arial", 16, "normal"))

            # Level up every 50 points
            if score >= level * 50:
                level += 1
                feedback_turtle.clear()
                feedback_turtle.color("blue")
                feedback_turtle.write(f"Level up! Now level {level}",
                                    font=("Arial", 16, "normal"))
        else:
            # Wrong!
            lives -= 1
            feedback_turtle.clear()
            feedback_turtle.color("red")
            feedback_turtle.write(f"Wrong! Correct answer: {correct_answer}",
                                font=("Arial", 16, "normal"))

        # Generate new problem
        current_problem = generate_problem(level)
        answer = ""

    except ValueError:
        feedback_turtle.clear()
        feedback_turtle.color("orange")
        feedback_turtle.write("Please enter a number!",
                            font=("Arial", 16, "normal"))

    screen.update()

# Keyboard input handling
def key_press(key):
    """Handle keyboard input"""
    global answer, game_over

    if game_over:
        return

    if key == "Return":  # Enter key
        check_answer()
    elif key == "BackSpace":  # Backspace
        answer = answer[:-1]
    elif key in "0123456789":
        answer += key

    update_display()

# Set up keyboard input
screen.listen()
for key in "0123456789":
    screen.onkey(lambda k=key: key_press(k), key)
screen.onkey(lambda: key_press("Return"), "Return")
screen.onkey(lambda: key_press("BackSpace"), "BackSpace")

# Start game
current_problem = generate_problem(level)
update_display()

# Game loop
while not game_over:
    if lives <= 0:
        game_over = True
        problem_turtle.clear()
        input_turtle.clear()
        feedback_turtle.clear()
        problem_turtle.write("GAME OVER", font=("Arial", 36, "bold"), align="center")
        score_turtle.goto(0, -50)
        score_turtle.write(f"Final Score: {score}",
                          font=("Arial", 24, "normal"), align="center")
        break

    time.sleep(0.05)  # Small delay to prevent CPU overuse

screen.update()
turtle.done()
```

## 🎯 Exercise 2: Shape Matching Game

Create a visual game where players match shapes:

```python
import turtle
import random
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.tracer(0)

class ShapeGame:
    def __init__(self):
        self.score = 0
        self.time_left = 60
        self.shapes = []
        self.target_shape = None
        self.create_shapes()

    def create_shapes(self):
        """Create random shapes on screen"""
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        shape_types = ["square", "triangle", "circle", "pentagon"]

        for _ in range(8):
            shape = turtle.Turtle()
            shape.hideturtle()
            shape.penup()

            # Random properties
            shape_type = random.choice(shape_types)
            color = random.choice(colors)
            size = random.randint(30, 60)
            x = random.randint(-350, 350)
            y = random.randint(-250, 250)

            # Store shape info
            shape.info = {
                "type": shape_type,
                "color": color,
                "size": size,
                "x": x,
                "y": y
            }

            # Draw shape
            shape.goto(x, y)
            shape.color(color)

            if shape_type == "square":
                self.draw_square(shape, size)
            elif shape_type == "triangle":
                self.draw_triangle(shape, size)
            elif shape_type == "circle":
                self.draw_circle(shape, size)
            elif shape_type == "pentagon":
                self.draw_pentagon(shape, size)

            self.shapes.append(shape)

        # Choose target shape
        self.choose_target()

    def draw_square(self, t, size):
        t.pendown()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.penup()

    def draw_triangle(self, t, size):
        t.pendown()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.penup()

    def draw_circle(self, t, size):
        t.pendown()
        t.circle(size)
        t.penup()

    def draw_pentagon(self, t, size):
        t.pendown()
        for _ in range(5):
            t.forward(size)
            t.left(72)
        t.penup()

    def choose_target(self):
        """Choose a random shape as target"""
        target = random.choice(self.shapes)
        self.target_shape = target

        # Display target description
        target_display = turtle.Turtle()
        target_display.hideturtle()
        target_display.penup()
        target_display.goto(0, 250)
        target_display.write(
            f"Find the {target.info['color']} {target.info['type']}",
            font=("Arial", 20, "bold"), align="center"
        )
        self.target_display = target_display

    def check_click(self, x, y):
        """Check if clicked shape matches target"""
        for shape in self.shapes:
            info = shape.info
            # Simple collision detection
            if (abs(x - info['x']) < info['size'] and
                abs(y - info['y']) < info['size']):

                if shape == self.target_shape:
                    self.score += 10
                    feedback = "Correct! +10 points"
                    # Create new shapes
                    self.clear_shapes()
                    self.create_shapes()
                else:
                    self.score -= 5
                    feedback = f"Wrong! That's a {info['color']} {info['type']}"

                # Show feedback
                fb = turtle.Turtle()
                fb.hideturtle()
                fb.penup()
                fb.goto(0, -280)
                fb.write(feedback, font=("Arial", 16, "normal"), align="center")
                screen.ontimer(fb.clear, 1000)  # Clear after 1 second

                self.update_score()
                break

    def clear_shapes(self):
        """Clear all shapes"""
        for shape in self.shapes:
            shape.clear()
        self.shapes = []
        self.target_display.clear()

    def update_score(self):
        """Update score display"""
        score_turtle = turtle.Turtle()
        score_turtle.hideturtle()
        score_turtle.penup()
        score_turtle.goto(-350, 250)
        score_turtle.write(f"Score: {self.score}  Time: {self.time_left}",
                          font=("Arial", 16, "normal"))

    def game_tick(self):
        """Update game timer"""
        self.time_left -= 1
        if self.time_left <= 0:
            self.game_over()
        else:
            screen.ontimer(self.game_tick, 1000)  # Call every second

    def game_over(self):
        """End game"""
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0, 0)
        game_over.write(f"Time's up! Final Score: {self.score}",
                       font=("Arial", 24, "bold"), align="center")

# Create and start game
game = ShapeGame()
game.update_score()
screen.onclick(game.check_click)
game.game_tick()

screen.update()
turtle.done()
```

## 🎮 Game Design Principles

### 1. Progressive Difficulty
Start easy, get harder:
```python
def get_difficulty(level):
    if level == 1:
        return {"min": 1, "max": 10, "operations": ["+"]}
    elif level == 2:
        return {"min": 10, "max": 50, "operations": ["+", "-"]}
    else:
        return {"min": 1, "max": 12, "operations": ["+", "-", "×"]}
```

### 2. Feedback Systems
Tell players how they're doing:
- Visual feedback (colors, animations)
- Audio feedback (beeps, though we can't do sound easily in turtle)
- Score updates
- Progress indicators

### 3. Reward Structures
- Points for correct answers
- Bonus points for speed
- Level advancement
- Unlockable features

## 💡 Debugging Tips: Game Problems

- **"Game runs too fast/slow"**: Adjust `time.sleep()` or frame rate
- **"Input not working"**: Check `screen.listen()` and `screen.onkey()` calls
- **"Collision detection inaccurate"**: Use simpler detection or adjust bounds
- **"Memory leak"**: Clear old turtles properly to avoid slowing down

## 📝 Session Checklist

- [ ] Designed a complete game with goals and rules
- [ ] Implemented a game loop
- [ ] Created a math fact practice game
- [ ] Made a shape matching game
- [ ] Implemented scoring and levels
- [ ] Added user interaction (keyboard/mouse)
- [ ] Provided player feedback
- [ ] Implemented progressive difficulty
- [ ] Created game over conditions
- [ ] Debugged game mechanics

---

⏱️ **20-Minute Break Point**

*Great work! You've learned the key concepts. Take a short break if you need one. When you're ready, try the challenge problems to test your skills!*

---
## 🏆 Challenge Problems

**Bronze Challenge**: Create a "number line" game where players place numbers in correct positions on a number line.

**Silver Challenge**: Make a "math maze" where players solve math problems to open doors and navigate through rooms.

**Gold Challenge**: Create a complete "math adventure" game with multiple levels, power-ups, enemies (that require math to defeat), and a boss battle!

## 🔜 Next Time...

In our final Session 12, you'll create your **Math Art Gallery** - a final project that combines everything you've learned! You'll plan, design, and build your own creative math-programming masterpiece to showcase your skills.

**Remember**: Games are the perfect way to apply programming skills. They combine logic, creativity, and fun - just like programming itself!

---

*Parent Note: This session is designed in 20-minute chunks (marked with ⏱️ break points). Total session time: 45-60 minutes. Game design synthesizes all programming concepts. Help your child think about game mechanics, fairness, and engagement. This is software engineering in miniature - planning, implementing, testing, and refining a complete system.*