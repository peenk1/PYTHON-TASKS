# Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

number = 121

if str(number) == str(number)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")