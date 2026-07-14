# Practice Problem: Display only those characters which are present at an even index number in given string.

word = input("Enter a string: ")

even_chars = word[::2]

for i in even_chars:
    print(i)