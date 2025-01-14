from sys import exit

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    result = x / y
    print(f"{x} / {y} is {result}")
except ValueError:
    print("Error: input is not a valid integer")
    exit(1)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    exit(1)