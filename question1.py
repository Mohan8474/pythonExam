"""
1. Temperature Conversion:
Write a Python program that converts temperatures from Celsius to Fahrenheit and vice versa.
The program should prompt the user to enter a temperature and whether they want to convert it
from Celsius to Fahrenheit or from Fahrenheit to Celsius.
The program should then perform the conversion and print the result.
1 celsius = 33.8 Fahrenheit

Sample output:
Enter the temperature: 25
Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: C
25 degrees Celsius is 77.0 degrees Fahrenheit.
"""

def celsiustofarenheit(a):
    conversion = a * 33.8
    return f"{a} degrees Celsius is {conversion} degrees Farenheit"
def farenheittocelsius(a):
    conversion = a / 33.8
    return f"{a} degrees Celsius is {conversion} degrees Farenheit"

def start():
    a = int(input("Enter Temparature: "))
    b = input("Enter 'C' to Convert from Celsius to Farenheit, or 'F' to convert from Farenheit to Celsius: ")
    if b == "C":
        result = celsiustofarenheit(a)
        print(result)
    elif b == "F":
        result = farenheittocelsius(a)
        print(result)
    else:
        print("Invalid Input")

start()