gross = float(input('Enter your salary: '))
tax_rate = 0.27

tax = gross * tax_rate
take_home = gross - tax

if gross > 0:
    print('Gross salary:', gross)
    print('Tax amount:', tax)
    print('Take-home pay:', take_home)
else:
    print('Salary must be greater than 0')