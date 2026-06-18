import json
from typing import Callable

class Company:
    def __init__(self) -> None:
        self._departments: dict[str, Department] = {}
        self._employees: dict[str, Employee] = {}
        self.methods: dict[str, Callable[[], None] ] = {'1': self.create_department, 
               '2': self.add_employees,
               '3': self.remove_employee,
               '4': self.update_employee,
               '5': self.transfer_employee,
               '6': self.search_employee,
               '7': self.show_employees,
               '8': self.show_departments,
               '9': self.employee_count,
               '10': self.save_file,
               '11': self.load_file,
               '12': self.display_menu}
        self.display_menu()

        user_input = 'a'
        while user_input != '0':
            user_input = input('> ')
            self.menu(user_input= user_input)

    def create_department(self) -> None:
        
    #   -------Department Data---------
        dept_name = input('Enter Department Name: ')

        if dept_name.strip() and not dept_name.isnumeric():
            department = Department(dept_name= dept_name)
     
        #   -----------Add Department------------
            if dept_name not in self._departments:
                self._departments[dept_name] = department
            else:
                print('Department already exists..')

        else:
            print()
            print('- Department name cannot be empty or numeric')
            print()

    def show_departments(self) -> None:
        print()
        print('Deparments: ')
        for department in self._departments:
            print(f'- {department}')
        print()

    def check_dept(self) -> 'Department | None':
        dept_name = input('Department Name: ')
        return self._departments.get(dept_name)

    def add_employees(self) -> None:
        department = self.check_dept()

        if department is None:
            print('Department not found')
            return

        employee_id = input('Enter Employee ID: ')

        if employee_id in self._employees:
            print('Employee ID already exists...')
            return

        employee = department.add_employee(employee_id)
        self._employees[employee_id] = employee

    def remove_employee(self) -> None:
        department = self.check_dept()

        if department is None:
            print('Department not found')
            return
    
        employee_id = department.remove_employee()

        if employee_id is None:
            print('Employee not found')
            return

        del self._employees[employee_id]

    def update_employee(self) -> None:
        department = self.check_dept()

        if department is None:
            print('Department not found')
            return

        department.update_employee()

    def transfer_employee(self) -> None:
        department = self.check_dept()

        if department is None:
            print('Department not found')
            return

        employee_id = input('Enter Employee ID: ')
        employee = department.find_employee(employee_id)

        if employee is None:
            print('Employee not found')
            return

        print('Transfer to', end=' ')
        transfer_dept = self.check_dept()

        if transfer_dept is None:
            print('Department not found')
            return

        del department.employees[employee_id]
        transfer_dept.employees[employee_id] = employee

        employee.department = transfer_dept.dept_name

    def search_employee(self) -> None:
        employee_id = input('Enter Employee ID: ')
        employee = self._employees.get(employee_id)

        if employee is None:
            print('Employee not found')
            return

        print(f'{'Name'.center(15)} | {'ID'.center(10)} | {'Department'.center(15)} | {'Experience'.center(15)} | {'Post'.center(15)} | {'Salary'.center(10)}')
        self.display_employee_details(employee= employee)

    def display_employee_details(self, employee: 'Employee') -> None:
        print(f'{employee.employee_name.center(15)} |',
                    f'{employee.employee_id.center(10)} |',
                    f'{employee.department.center(15)} |',
                    f'{(str(employee.experience) + ' years').center(15)} |',
                    f'{employee.post.center(15)} |', 
                    f'{str(employee.salary).center(10)}')

    def show_employees(self) -> None:
        print(f'{'Name'.center(15)} | {'ID'.center(10)} | {'Department'.center(15)} | {'Experience'.center(15)} | {'Post'.center(15)} | {'Salary'.center(10)}')
        print('-'* 100)
        for employee in self._employees.values():
            self.display_employee_details(employee= employee)

    def employee_count(self) -> None:
        total_count = 0
        print('Employee count: ')
        print()
        for dept_name, department in self._departments.items():
            print(f'- {dept_name}: {len(department.employees)} employees')
            total_count += len(department.employees)
        
        print()
        print(f'Total employee count: {total_count}')

    def display_menu(self) -> None:
        print()
        print('========== EMPLOYEE MANAGEMENT ==========')
        for index, method in self.methods.items():
            print(index + '.', ' '.join((method.__name__).split('_')).title())
        print('0. Exit')
        print('=========================================')
        print()

    def menu(self, user_input: str) -> None:
        if user_input in self.methods:
            method = self.methods[user_input]
            print()
            print('*'*100)
            method()
            print('*'*100)
            print()
        elif user_input == '0':
            print()
            print('Program stopped')
            print()
        else:
            print()
            print('Invalid option..')
            print()

    def store_obj(self, obj: object) -> dict[str, object]:
        return vars(obj)

    def save_file(self) -> None:
        file_name = input('File name: ')
        with open(f'{file_name}', 'w') as f:
            json.dump(self._employees, f, default= self.store_obj)
        
        print()
        print(f'- Successfully saved {len(self._employees)} employees')

    def load_file(self) -> None:
        file_name = input('File Name: ')
        try:
            with open(f'{file_name}', 'r') as f:
                employee_dict = json.load(f)
                self._departments.clear()
                self._employees.clear()
                for employee_id, employee_details in employee_dict.items():
                    employee = Employee(**employee_details)
                    self._employees[employee_id] = employee
                    if employee.department not in self._departments:
                        self._departments[employee.department] = Department(dept_name= employee.department)
                    
                    department = self._departments[employee.department]
                    

                    department.employees[employee.employee_id] = employee

            print()
            print(f'- Successfully loaded {len(self._employees)} employees')

        except FileNotFoundError:
            print('File not found')
        except Exception as e:
            print(f'{type(e).__name__}: {e}')

class Department:
    def __init__(self, dept_name: str) -> None:
        self.dept_name = dept_name
        self.positions = {'Worker': 80000, 'Customer Service': 40000, 'Manager': 200000}
        self.employees: dict[str, Employee] = {}

    def __repr__(self) -> str:
        return self.dept_name

    def add_employee(self, employee_id: str) -> 'Employee':

    #   -----Employee Data-------

        while True:
            employee_name = input('Enter Employee Name: ')

            if employee_name.replace(' ', '').isalpha():
                break
        
            print()
            print('- Employee name cannot be empty or numeric....')
            print()

        experience = None
        while not isinstance(experience, int):
            try:
                experience = int(input('Enter Work Experience: '))
            except ValueError:
                print()
                print('Experience must be numeric..')
                print()

        desig_post = input('Enter Post: ')

        while desig_post not in self.positions:
            print()
            print('Available positions: ')
            for position in self.positions:
                print(f'- {position}')
            print()
            desig_post = input('Enter Post: ')

    #   ---------Employee Post------------

        employee = Employee(employee_name= employee_name, employee_id= employee_id, department= self.dept_name, experience= experience, post= desig_post, salary= 0)
        self.assign_salary(employee= employee, post= desig_post)
   
    # ------Add Employee------
        
        self.employees[employee.employee_id] = employee

        return employee

    def assign_salary(self, employee: 'Employee', post: str) -> None:
        employee.salary = self.positions[post]

    def find_employee(self, employee_id: str) -> 'Employee | None':
        return self.employees.get(employee_id)

    def remove_employee(self) -> str | None:
        employee_id = input('Enter Employee ID: ')
        employee = self.find_employee(employee_id= employee_id)

        if employee is None:
            print('Employee not found')
            return

        del self.employees[employee.employee_id]

        return employee_id

    def update_employee(self) -> None:
        employee_id = input('Enter Employee ID: ')
        employee = self.find_employee(employee_id= employee_id)
        employee_info = {
            '1': 'employee_name',
            '2': 'experience',
            '3': 'post',
            '4': 'salary'
        }

        if employee is None:
            print('Employee not found')
            return

        print("Available fields:")
        for key, attr in employee_info.items():
            print(f"- {key}. {(' '.join((attr).split('_'))).title()}")

        update_input = input('What would you like to update: ')
        for key, info in employee_info.items():
            if update_input == key:
                data = getattr(employee, info)
                new_info = None
                while True:
                    print()
                    print('- Press enter to exit')
                    print()
                    new_info = input(f'Enter New {(' '.join((info).split('_'))).title()}: ')

                    if new_info == str(data):
                        print()
                        print(f'- Cannot enter same {(' '.join((info).split('_'))).title()}')
                        continue
                    elif new_info == '':
                        break

                    if info == 'post':
                        if new_info in self.positions:
                            setattr(employee, info, new_info)
                            self.assign_salary(employee= employee, post= new_info)
                            break
                        else:
                            print()
                            print('Position not available')
                            print()
                            print('Available positions: ')
                            for position in self.positions:
                                print(f'- {position}')
                            print()
                    else:
                        new_info = int(new_info) if isinstance(data, int) and new_info.isnumeric() else new_info
                        if type(new_info) == type(data):
                            setattr(employee, info, new_info)
                            break
                        else:
                            print()
                            print('Wrong data type assigned...')
                            print(f'Data type -> {type(data)}')
                            print()

    def show_employee_count(self) -> None:
        print(len(self.employees))

class Employee:
    
    def __init__(self, employee_name: str, employee_id: str, department: str, experience: int, post: str, salary: int) -> None:
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.department = department
        self.experience = experience
        self.post = post
        self.salary = salary

    def __str__(self) -> str:
        return self.employee_name
    
    def __repr__(self) -> str:
        return self.employee_name

def main() -> None:
    Company()

if __name__ == '__main__':
    main()