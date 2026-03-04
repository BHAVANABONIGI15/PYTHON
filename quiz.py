# Python Quiz Program

questions = [
    {
        "question": "1. What is the output of print(3 + 2 * 2)?",
        "options": ["a) 10", "b) 7", "c) 8", "d) 12"],
        "answer": "b"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) define", "c) def", "d) function"],
        "answer": "c"
    },
    {
        "question": "3. What data type is 'Hello'?",
        "options": ["a) Integer", "b) String", "c) Boolean", "d) List"],
        "answer": "b"
    },
    {
        "question": "4. What will the code print if x = 5 and x > 3?",
        "options": ["a) No", "b) Yes", "c) 5", "d) Error"],
        "answer": "b"
    },
    {
        "question": "5. Which symbol is used for comments in Python?",
        "options": ["a) //", "b) <!-- -->", "c) #", "d) **"],
        "answer": "c"
    },
    {
        "question": "6. What is the output of len('Python')?",
        "options": ["a) 5", "b) 6", "c) 7", "d) Error"],
        "answer": "b"
    },
    {
        "question": "7. Which brackets create a list in Python?",
        "options": ["a) ( )", "b) { }", "c) [ ]", "d) < >"],
        "answer": "c"
    },
    {
        "question": "8. What does range(3) print in a loop?",
        "options": ["a) 1 2 3", "b) 0 1 2", "c) 0 1 2 3", "d) 1 2"],
        "answer": "b"
    },
    {
        "question": "9. Which function takes user input?",
        "options": ["a) scan()", "b) input()", "c) read()", "d) get()"],
        "answer": "b"
    },
    {
        "question": "10. Python is a ______ programming language.",
        "options": ["a) Case-insensitive", "b) Case-sensitive", "c) Only uppercase", "d) Only lowercase"],
        "answer": "b"
    }
]

score = 0

print("Welcome to the Python Quiz!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (a/b/c/d): ").lower()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is '{q['answer']}'.\n")

print(f"Quiz finished! Your final score is {score}/{len(questions)}")

