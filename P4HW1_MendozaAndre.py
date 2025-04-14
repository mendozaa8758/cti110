# Andre Mendoza
# P4HW1
# 4/13/25
# Create a scoring system for tests

# Ask how many scores need to be entered
num_scores = int(input("How many scores would you like to enter? "))

# Create a list to store valid scores
student_scores = []

# Loop to collect the scores
for i in range(num_scores):
    score = int(input(f"Enter score #{i+1}: "))

    # Check if the score is valid (between 0 and 100)
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        score = int(input(f"Re-enter score #{i+1}: "))

    # Add the valid score to the list
    student_scores.append(score)

print('------------Results------------')
# Display the lowest score
lowest_score = min(student_scores)
print("\nLowest score:", lowest_score)

# Create a new list with the lowest score removed
modified_scores = student_scores.copy()
modified_scores.remove(lowest_score)
print("Modified List:", modified_scores)

# Calculate average of the modified list
average_score = sum(modified_scores) / len(modified_scores)
print("Average score:", round(average_score, 2))

# Find letter grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
print('------------------------')
