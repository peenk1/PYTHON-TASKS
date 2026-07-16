# Practice Problem: Iterate through a given list of numbers and print only those numbers which are divisible by 5.

ile_rek = input("Podaj ile rekordow: ")

lista = []
lista2 = []

for i in range(int(ile_rek)):
    lista.append(int(input(f"Podaj {i + 1} liczbe: ")))

for i in lista:
    if i % 5 == 0:
        lista2.append(i)

print("Liczby podzielne przez 5:", lista2)