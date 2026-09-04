gross = float(input('Enter your salary: '))
hours = float(input('Enter the number of hours worked: '))
tax_rate = float(input('Enter the tax rate (as a decimal): '))
gross_pay = gross * hours
tax_amount = gross_pay * tax_rate
take_home_pay = gross_pay - tax_amount
if gross_pay > 0:
    print("total pay:",take_home_pay)
    print("bi-weekly pay:", take_home_pay *2)
    print("monthly pay:", take_home_pay * 4)
    print("yearly pay:", take_home_pay * 52)
if gross_pay <= 0:
    print("total pay must be greater than 0")