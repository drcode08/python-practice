
## AND - If both are true then it returns True

# Check the salary range between 1000 and 50000

x = int(input("Enter your salary: "))

if x > 0 and x < 50000:
    print("Salary is between 0 and 50000:", x)
else:
    print("Salary is not between 0 and 50000:", x)


## OR - If any one is true then it returns True
# Check age and sal of an employee

age = int(input("Enter Age: "))
sal = int(input("Enter employee salary: "))

if age > 30 or sal > 1000:
    print(f"Employee is eligible to hire with age={age} and sal ={sal}")
else:
    print(f"Employee is not eligible to Hire with age={age} and sal={sal}")



## NOT - it inverts the results

company = 'IBM'

if not(company == 'IBM'):
    print("I'm working in ", company)
else:
    print("I'm not working in ", company)
