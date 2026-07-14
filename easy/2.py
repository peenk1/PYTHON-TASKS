# Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

previous_num = 0

for i in range (10):
    suma = previous_num + i
    print (f"Previous number: {previous_num}, Current number: {i}, Sum: {suma}")
    previous_num = i