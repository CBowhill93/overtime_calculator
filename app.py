## OVERTIME CALCULATOR ##

## greeting & information collection ##
print("""WELCOME TO THE OVERTIME CALCULATOR!
  """)
print("""Please follow the steps below to calculate your weekend overtime...
 """)
yearly_income = int(input("Please enter your annual salary: "))
print(f"""Your annual salary is {yearly_income}
 """)

weekend_hours = int(input("Please enter the total weekend hours worked: "))
print(f"""
You worked {weekend_hours} total hours. """)

## hourly rate calculation ##

def hourly_rate():
    result = float(yearly_income // 2080)
    return float(result)

print(f"""Your hourly rate is: {hourly_rate()} per hour.""")

## overtime amount calculation with tax deduction ##

def overtime():
    payment_amount = hourly_rate() * weekend_hours
    tax_deduction = payment_amount * 0.20
    final_amount = payment_amount - tax_deduction
    return float(final_amount)

## overtime amount result ##

print(f"""
YOUR TOTAL OVERTIME PAYMENT FOR THE INPUTTED HOURS IS: {overtime()}""")