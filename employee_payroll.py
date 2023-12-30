

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_payrate = float(input("Enter hourly pay rate: "))
federal_taxrate = float(input("Enter Federal Tax Withholding rate: "))
state_taxrate = float(input("Enter State Tax Withholding rate: "))

gross_pay = hours_worked * hourly_payrate

federal_withholdings = round(((federal_taxrate * gross_pay) / 100), 2)

state_withholdings = round(((state_taxrate * gross_pay) / 100), 2)

total_deduction = round((federal_withholdings + state_withholdings), 2)

net_pay = round((gross_pay - (federal_withholdings + state_withholdings)), 2)

print("************************************************************")
print("*", employee_name + " Payroll Statement for the month of April *")
print("************************************************************")
print("*Employee Name: " + employee_name)
print("*Hours Worked: " + str(hours_worked)) 
print("*Pay Rate: $" + str(hourly_payrate))
print("*Gross Pay: $" + str(gross_pay))
print("*Deductions:")
print("*Federal Withholdings(20.0%): $" + str(federal_withholdings))
print("*State Withholdings(9.00%): $" + str(state_withholdings))
print("*Total Deduction: $" + str(total_deduction))
print("*Net Pay: $" + str(net_pay))
print("************************************************************")
