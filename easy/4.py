# Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

text = (input("Enter a string: "))
n = int(input("Enter the index number up to which you want to remove characters: "))

def remove_chars(text, n):
    return text[n:]

print(remove_chars(text, n))