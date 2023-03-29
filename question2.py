"""Write a Python program that calculates a student's grade based on their scores in three different tests.
The program should prompt the user to enter their scores for each test, and then calculate their average score.
The program should then assign a letter grade based on the following grading scale:

A: average score >= 90
B: 80 <= average score < 90
C: 70 <= average score < 80
D: 60 <= average score < 70
F: average score < 60
The program should print the average score and letter grade.

Output:
Enter score for test 1: 85
Enter score for test 2: 92
Enter score for test 3: 88
Average score: 88.33
Letter grade: B
"""

def studentgrade(a,b,c):
    average = (a+b+c)/3
    if average >= 90:
        Grade = "A"
    elif average < 90 and average >= 80:
        Grade = "B"
    elif average < 80 and average >= 70:
        Grade = "C"
    elif average < 70 and average >= 60:
        Grade = "D"
    else:
        Grade = "F"
    return f"Average score is : {average} \nLetter Grade : {Grade}"

def start():
    a = int(input("Enter Score for Test 1: "))
    b = int(input("Enter Score for Test 2: "))
    c = int(input("Enter Score for Test 3: "))
    result = studentgrade(a,b,c)
    print(result)

start()