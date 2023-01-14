grade=input("enter the grade of employee")
salary=int(input("Enter the salary of the employee"))
if grade=='A':
    if salary < 10000:
        bonus=salary*0.07
    else:
        bonus = salary * 0.05
    print(bonus)
    salary = salary + bonus
    print(salary)
elif grade=='B':
    if salary < 10000:
        bonus=salary*0.12
    else:
        bonus = salary * 0.1
    print("bonus:",bonus)
    salary = salary + bonus
    print("total to bepaid:",salary)
else:
    print(salary)
