import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Math Quiz")
screen.bgcolor("lightgrey")

# Create a turtle object
t = turtle.Turtle()
t.hideturtle()
t.penup()

# Define quiz questions and answers
questions = [
    {
        "question": "What is 5 + 3?",
        "choices": ["6", "8", "7", "9"],
        "correct": "8"
    },
    {
        "question": "What is 12 - 4?",
        "choices": ["7", "8", "9", "10"],
        "correct": "8"
    },
    {
        "question": "What is 3 * 3?",
        "choices": ["6", "8", "9", "7"],
        "correct": "9"
    },
    {
        "question": "What is 15 / 3?",
        "choices": ["4", "5", "6", "7"],
        "correct": "5"
    }
]

# Function to display the question and choices
def display_question(question, choices):
    t.clear()
    t.goto(-200, 200)
    t.write(question, font=("Arial", 16, "bold"))
    y = 150
    for i, choice in enumerate(choices):
        t.goto(-200, y)
        t.write(f"{i + 1}. {choice}", font=("Arial", 14, "normal"))
        y -= 30

# Function to handle clicks
def on_click(x, y):
    global current_question
    if -200 < x < 200 and 200 > y > -200:
        # Calculate the choice index based on the y-coordinate
        choice_index = int((200 - y) // 30) - 1
        if 0 <= choice_index < len(questions[current_question]["choices"]):
            answer = questions[current_question]["choices"][choice_index]
            if answer == questions[current_question]["correct"]:
                t.goto(-200, -50)
                t.write("Correct!", font=("Arial", 16, "bold"))
            else:
                t.goto(-200, -50)
                t.write("Wrong! Try Again.", font=("Arial", 16, "bold"))
            screen.update()
            screen.ontimer(next_question, 2000)  # Move to next question after 2 seconds

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        q = questions[current_question]
        display_question(q["question"], q["choices"])
    else:
        t.clear()
        t.goto(-200, 0)
        t.write("Quiz Completed!", font=("Arial", 24, "bold"))

current_question = 0

# Display the first question
display_question(questions[current_question]["question"], questions[current_question]["choices"])

# Set up click event listener
screen.onclick(on_click)

# Keep the window open
turtle.done()