gross = float(input('Enter your salary: '))
hours = float(input('Enter the number of hours worked: '))
tax_rate = float(input('Enter the tax rate (as a decimal): '))
gross_pay = gross * hours
tax_amount = gross_pay * tax_rate
take_home_pay = gross_pay - tax_amount
if gross_pay > 0:
    print("total pay:",take_home_pay)
    print("bi-weekly pay:", take_home_pay *2)
if gross_pay <= 0:
    print("total pay must be greater than 0")