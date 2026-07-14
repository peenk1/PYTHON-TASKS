# Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

text = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Total number of vowels in the given sentence: {count}")

