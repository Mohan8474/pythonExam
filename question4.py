"""

Write a Python program that prompts the user to enter a size for a hexagon,
and then prints a hexagon of that size using asterisks(*).
The program should handle invalid input gracefully by displaying an error message and asking the user to enter a valid input.

Example Output:
Enter a size for the hexagon: 4

   *
  * *
 * * *
* * * *
* * * *
 * * *
  * *
   *
"""

a = int(input("Enter Number: "))
for i in range(a+1):
    for j in range(i):
        print(" *", end=" ")
    print()
for i in range(a,0,-1):
    for j in range(i):
        print(" *", end=" ")
    print()

