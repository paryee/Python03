# Input

Charge = int(input("Enter the charge of food "))
tip = (0.18*int(Charge))
Sale_tax = (0.07*int(Charge))
Grand_total = (int(Charge) + int(tip) + int(Sale_tax))

# Output

print("tip = $" + str(tip))
print("Sale tax = $" + str(Sale_tax))
print("Grand total = $" + str(Grand_total))
