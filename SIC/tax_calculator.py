#level 1

#input pt1 
employee_name = input("Enter The Employee Name : ")
employee_id = input("Enter the Employeee ID :")
base_monthly_salary = int(input("Ente the Basic Monthly Salary :"))
special_allowances = int(input("Enter the Speacial Allowances"))
bonus_percentage = int(input("Enter the bonus percentage: "))
gross_monthly_salary = base_monthly_salary + special_allowances
annual_gross_salary = (gross_monthly_salary * 12) + (bonus_percentage / 100) * base_monthly_salary
'''
#output lvl1
print("The Employee name is ",employee_name)
print("THe Employee ID : ",employee_id)
print("The Gross monthly Salary is : ",gross_monthly_salary)
print("The gross Annual Salary is : ",annual_gross_salary)
'''
#level 2
#calculation of taxable income
taxable_income = annual_gross_salary - 50000

#print("Gross salary =",annual_gross_salary)
#print("Standard deduction =  ₹50000")
#print("Taxable income is :",taxable_income)

#level 3
if annual_gross_salary >= 0 and annual_gross_salary <= 300000:
    tax = 0
elif annual_gross_salary <= 600000:
    tax = 5
elif annual_gross_salary <= 900000:
    tax = 10
elif annual_gross_salary <= 1200000:
    tax = 15
elif annual_gross_salary <= 1500000:
    tax =20
else :
    tax = 30

if taxable_income <= 700000:
    tax = 0
    tax = tax + 4
    print ("You're eligible for 100 % rebate ")
else :
    tax = tax + 4

total_tax = (tax/100) * taxable_income
#print("The Tax payable is : ", total_tax)

#level 4

net_salary = annual_gross_salary - total_tax
'''
print("Annual Gross Salary :",annual_gross_salary)
print("Total Payable tax =",total_tax)
print("Net Salary :",net_salary)
'''

#level 5
print("---- Employee Details ----")
print("Name :",employee_name)
print("Employee ID: ",employee_id)
print("Gross monthly Salary : ",gross_monthly_salary)
print("Annual Gross Salary: ",annual_gross_salary)
print("Taxable Income",taxable_income)
print("Tax Payable : ",total_tax)
print("Annual net Salary :",net_salary)



