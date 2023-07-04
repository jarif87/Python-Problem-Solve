principal = float(input('Enter principal amount: '))
rate = float(input('Enter the interest rate: '))
time = float(input('Enter time (in years): '))
number = float(input('Enter the number of times that interest is compounded per year: '))

x = number * time
# calculate total amount
amount = principal * (1 + rate / number) ** x

# calculate compound interest

ci=amount-principal

print('Compound interest = %.2f' %ci)
print('Total amount = %.2f' %amount)
