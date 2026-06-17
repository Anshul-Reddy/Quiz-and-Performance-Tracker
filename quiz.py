

def view_attempts():
    print("\n=====PREVIOUS ATTEMPTS=====")

    with open("results.txt","r") as file:
        data = file.read()
    print(data)

print("=====QUIZ SYSTEM=====")
name = input("Enter your name: ")
print("Welcome!",name)
score = 0
print("\nChoose SUbject: ")
print("1. Python")
print("2. DBMS")
print("3. AI")

choice = input("Enter your Choice: ")
print("You Selected: ",choice)

quiz_data = {
    "Python": [
        {
            "question":"What is Python?",
            "options": ["Programming Language","Database","Operating System","Browser"],
            "answer": 1,
            "topic":"Basics"
            
        },

        {
            "question":"Which keyword is used to create a function?",
            "options": ["func","define","def","function"],
            "answer": 3,
            "topic":"Functions"
        },

        {
            "question":"Which symbol is used for comments in Python?",
            "options": ["//","#","/*","--"],
            "answer": 2,
            "topic":"Basics"
        }
    ],

    "DBMS":[
        {
            "question":"What does DBMS stand for?",
            "options": ["Database Management System","Data Base Main System","Database Memory System","None"],
            "answer": 1,
            "topic":"Basics"
        },

        {
            "question":"Which key uniquely identifies a record in a table?",
            "options": ["Foreign Key","Primary Key","Candidate Key","Composite Key"],
            "answer": 2,
            "topic":"Keys"
        },

        {
            "question":"Which SQL command is used to retrieve data from a table?",
            "options": ["GET","FETCH","SELECT","DISPLAY"],
            "answer":3,
            "topic":"SQL"
        }
    ],

    "AI":[
        {
            "question":"What does AI stand for?",
            "options": ["Automated Intelligence","Artificial Intelligence","Automated Internet","Artificial Internet"],
            "answer":2,
            "topic":"Basics"
        },

        {
            "topic": "Applications",
            "question": "Which of the following is an application of AI?",
            "options": ["Face Recognition","Keyboard","Monitor","Printer"],
            "answer": 1
        },

        {
            "topic":"Machine Learning",
            "question":"Machine Learning is a subset of?",
            "options": ["DBMS","Operating System","Artificial Intelligence","Computer Network"],
            "answer":3
        }
    ]
} 

weak_topics = []
if choice == "1":
    selected_questions = quiz_data["Python"]
    subject = "Python"

elif choice == "2":
    selected_questions = quiz_data["DBMS"]
    subject = "DBMS"

else:
    selected_questions = quiz_data["AI"]
    subject = "AI"

for q in selected_questions:
    print("\n" + q["question"])
    for i,option in enumerate(q["options"], start = 1):
        print(f"{i}. {option}")

    user_answer = int(input("Enter your answer: "))

    if user_answer == q["answer"]:
        print("✅ CORRECT!!")
        score += 1
    else:
        print("❌ WRONG!")
        weak_topics.append(q["topic"])

print("\n=====QUIZ FINISHED=====")
print("Your Score:",score, "/", len(selected_questions))

percentage = (score / len(selected_questions))*100
print("Percentage: ",percentage, "%")

if percentage >= 40:
    print("PASS")
else:
    print("FAIL")

print("\nWeak Areas: ")
if len(weak_topics) == 0:
    print("No weak areas detected.Excellent Performance! 🎉")
else:
    for topic in weak_topics:
        print("-",topic)

with open("results.txt","a") as file:
    file.write(f"{name} | {subject} | Score: {score}/{len(selected_questions)} | Percentage: {percentage:.2f}%\n")
view_attempts()