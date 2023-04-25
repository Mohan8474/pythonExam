
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
