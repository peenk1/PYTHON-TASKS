# Practice Problem: Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

new_fruit = input("Enter a new fruit to add to the list: ")

fruits.append(new_fruit)

fruits.remove(fruits[1])

print(fruits)