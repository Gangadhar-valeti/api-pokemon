questions = [
    "1. What is the capital of India?",
    "2. How many elements are in the periodic table?",
    "3. How many bones are in the human body?",
    "4. Which of the following is an object-oriented language?",
    "5. Which language is a high-level language?",
    "6. How many states are there in India?"
]

options = [
    ("A. Mumbai", "B. Chennai", "C. Delhi", "D. Kerala"),
    ("A. 117", "B. 118", "C. 119", "D. 110"),
    ("A. 206", "B. 207", "C. 208", "D. 209"),
    ("A. R", "B. C", "C. Java", "D. Python"),
    ("A. Python", "B. R", "C. CSS", "D. JavaScript"),
    ("A. 23", "B. 47", "C. 26", "D. 29")
]

score = 0
answers = ["C", "B", "A", "C", "A", "D"]
guesses = []

for questions_num in range(len(questions)):
    print("-----------------------------------")
    print(questions[questions_num])
    for option in options[questions_num]:
        print(option)
    
    guess = input("Enter the options (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[questions_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is {answers[questions_num]}.")

print(f"Your total score is {score} out of {len(questions)}.")
