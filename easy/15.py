#Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.

x = int(input("Podaj ile rekordow: "))

for num in range(1, x+1):
    for i in range(num):
        print(num, end=" ")
    print()


