# Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

a = int(input("Enter a number "))
factorial = 1

for i in range(1, a+1):
    factorial = factorial * i



print(f"Factorial to this number is: {factorial}")
