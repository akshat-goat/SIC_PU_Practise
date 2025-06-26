# Employee Name Validation
while True:
    employee_name = input("Enter The Employee Name: ").strip()
    if not employee_name:
        print("Error: Employee Name cannot be empty. Please re-enter.")
    elif not re.fullmatch(r'[a-zA-Z\s]+', employee_name): # Allows spaces in names
        print("Error: Employee Name must contain only alphabets and spaces. Please re-enter.")
    elif len(employee_name) > 50:
        print("Error: Employee Name cannot exceed 50 characters. Please re-enter.")
    else:
        break

# Employee ID Validation
while True:
    employee_id = input("Enter the Employee ID: ").strip()
    if not employee_id:
        print("Error: Employee ID cannot be empty. Please re-enter.")
    elif not employee_id.isalnum():
        print("Error: Employee ID must be alphanumeric. Please re-enter.")
    elif not (5 <= len(employee_id) <= 10):
        print("Error: Employee ID must be between 5 and 10 characters. Please re-enter.")
    else:
        break

# Basic Monthly Salary Validation
while True:
    try:
        base_monthly_salary_str = input("Enter the Basic Monthly Salary: ")
        base_monthly_salary = int(base_monthly_salary_str)
        if base_monthly_salary <= 0:
            print("Error: Basic Monthly Salary must be a positive number. Please re-enter.")
        elif base_monthly_salary > 10000000: # Max ₹1,00,00,000
            print("Error: Basic Monthly Salary cannot exceed ₹1,00,00,000. Please re-enter.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for Basic Monthly Salary.")

# Special Allowances Validation
while True:
    try:
        special_allowances_str = input("Enter the Special Allowances: ")
        special_allowances = int(special_allowances_str)
        if special_allowances < 0:
            print("Error: Special Allowances cannot be negative. Please re-enter.")
        elif special_allowances > 10000000: # Max ₹1,00,00,000
            print("Error: Special Allowances cannot exceed ₹1,00,00,000. Please re-enter.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for Special Allowances.")

# Bonus Percentage Validation
while True:
    try:
        bonus_percentage_str = input("Enter the bonus percentage (0-100): ")
        bonus_percentage = int(bonus_percentage_str)
        if not (0 <= bonus_percentage <= 100):
            print("Error: Bonus Percentage must be between 0 and 100. Please re-enter.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for Bonus Percentage.")

# --- Derived Calculations (with validation) ---
gross_monthly_salary = base_monthly_salary + special_allowances

# Validate Gross Monthly Salary
if gross_monthly_salary <= 0:
    # This scenario should ideally not be reachable if base_monthly_salary is > 0 and special_allowances >= 0
    print("Warning: Gross Monthly Salary is not greater than zero. Review inputs.")

# Calculate initial annual gross salary before its own validation
# Note: bonus_percentage is applied on base_monthly_salary, not gross_monthly_salary for bonus calculation as per original code.
annual_gross_salary = (gross_monthly_salary * 12) + ((bonus_percentage / 100) * base_monthly_salary)

# Validate Annual Gross Salary against "realistic values"
# Assuming "realistic values" means it shouldn't exceed a certain high but reasonable threshold.
# This limit is arbitrary for this example, adjust as needed.
MAX_REALISTIC_ANNUAL_GROSS = 20000000 # Example: 2 Crore INR
if annual_gross_salary > MAX_REALISTIC_ANNUAL_GROSS:
    print(f"Warning: Calculated Annual Gross Salary ({annual_gross_salary:,.2f}) exceeds realistic values (max ₹{MAX_REALISTIC_ANNUAL_GROSS:,.2f}).")
    print("Please check the input values, especially Basic Monthly Salary and Special Allowances.")
