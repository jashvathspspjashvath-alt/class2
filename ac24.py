units = float(input('enter the number of units consumed:'))
cost_per_=0
tax = 0
if units < 50:
   cost_per_units=2.98
   tax = 34
elif units < 100:
     cost_per_units == 3.45
     tax = 34
elif units <200:
    cost_per_units= 5.56
    tax = 45
else:
    cost_per_units = 8.45
    tax=56
bill_amount = (units * cost_per_units) + tax
print('\n--- electricity bill ---')
print(f'units comsumed: {units}')
print(f'cost per ccost unit: {cost_per_units}')
print(f'tax{tax}')
print(f'total bill amount: {bill_amount:.2f}')