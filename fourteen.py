# Function to print salary slip for given employee number
def print_salary_slip(emp_no):
    with open('salary_details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(',')
            if int(fields[0]) == emp_no:
                print("Salary Slip for Employee Number:", fields[0])
                print("Name:", fields[1])
                print("Department Number:", fields[2])
                basic = int(fields[3])
                da = int(fields[4])
                hra = int(fields[5])
                conveyance = int(fields[6])
                gross = basic + da + hra + conveyance
                print("Basic Salary:", basic)
                print("DA:", da)
                print("HRA:", hra)
                print("Conveyance:", conveyance)
                print("Gross Salary:", gross)
                break
        else:
            print("Employee not found")

# Function to print employee list for given department number
def print_employee_list(dept_no):
    with open('salary_details.txt', 'r') as f:
        lines = f.readlines()
        print("Employees in Department Number:", dept_no)
        for line in lines:
            fields = line.split(',')
            if int(fields[2]) == dept_no:
                print("Employee Number:", fields[0])
                print("Name:", fields[1])
                print("Basic Salary:", fields[3])
                print()
        else:
            print("No employees found in department")

# Main function
if __name__ == '__main__':
    print_salary_slip(101)
    print()
    print_employee_list(102)
