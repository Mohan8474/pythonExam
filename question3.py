"""

Write a Python program that calculates the factorial of a given integer.
The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less
than or equal to n.
For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.

The program should prompt the user to enter a non-negative integer, and then calculate its factorial.
The program should handle invalid input gracefully by displaying an error message and asking
the user to enter a valid input.

Sample Output:
Enter a non-negative integer: 5
The factorial of 5 is 120.
"""
def fact(a):
    factorial = 0
    if a == 0:
        return factorial
    elif a == 1:
        factorial = 1
        return factorial
    else:
        factorial = a * fact(a-1)
        return factorial

def start():
    a = int(input("Enter a Non Negative Number: "))
    while a <0:
        print("Invalid Input ")
        a = int(input("Enter a Non Negative Number: "))
    result = fact(a)
    print(result)

start()
