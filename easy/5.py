# Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f"Before swapping: a = {a}, b = {b}")

a, b=b, a

print(f"After swapping: a = {a}, b = {b}")