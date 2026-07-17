# Practice Problem: Calculate income tax for a given income based on these rules:
#
# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax

income = int(input("Podaj przychod: "))

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 0.1
else:
    tax_payable = 0 + (10000 * 0.1)
    tax_payable += (income - 20000) * 0.2

print(f"Musisz zapłacicić {tax_payable} podatku")
