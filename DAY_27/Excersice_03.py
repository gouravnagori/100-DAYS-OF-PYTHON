# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

# KBC (Kaun Banega Crorepati) Quiz Game

# List of questions
questions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    
    ["Which language is used for AI and ML most commonly?", 
     "Python", "Java", "C", "PHP", 1],
    
    ["Who is the founder of Microsoft?", 
     "Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg", 3],
    
    ["Which planet is known as the Red Planet?", 
     "Earth", "Mars", "Jupiter", "Venus", 2],
    
    ["What is 5 + 7 ?", 
     "10", "11", "12", "13", 3]
]

# Prize money for each question
money = [1000, 5000, 10000, 50000, 100000]

total_money = 0

print("Welcome to KBC Game\n")

# Loop through all questions
for i in range(len(questions)):
    
    question = questions[i]
    
    print(f"Question for Rs. {money[i]}")
    print(question[0])   # Question
    
    # Display options
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    
    # Take user answer
    answer = int(input("Enter your answer (1-4): "))
    
    # Check answer
    if answer == question[5]:
        print("Correct Answer!\n")
        total_money = money[i]
        
    else:
        print("Wrong Answer!")
        print(f"The correct answer was option {question[5]}")
        break

# Final winning amount
print(f"\nYou are taking home Rs. {total_money}")
