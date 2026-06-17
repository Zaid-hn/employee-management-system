class Company:
    def __init__(self) -> None:
        self._departments = {} #type: ignore

    def create_department(self):
        
    #   -------Department Data---------

        dept_name = input('Enter Department Name: ')

        department = Department(dept_name= dept_name)

    #   -----------Add Department------------
        if dept_name not in self._departments: #type: ignore
            self._departments[dept_name] = department #type: ignore
            print(self._departments) #type: ignore
        else:
            print('Department already exists..')

    def check_dept(self): #type: ignore
        dept_name = input('Department Name: ')
        return self._departments.get(dept_name) #type: ignore 

    def add_employees(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return

        department.add_employee() #type: ignore

    def remove_employee(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return

        department.remove_employee() #type: ignore

    def update_employee(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return

        department.update_employee() #type: ignore 

    def transfer_employee(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return

        employee = department.find_employee() #type: ignore

        if employee is None:
            print('Employee not found')
            return

        print('Transfer to', end=' ')
        transfer_dept = self.check_dept() #type: ignore

        if transfer_dept is None:
            print('Department not found')
            return

        department.employees.remove(employee) #type: ignore
        transfer_dept.employees.append(employee) #type: ignore

        employee.dept_name = transfer_dept.dept_name #type: ignore

    def search_employee(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return

        department.search_employee() #type: ignore

    def show_employees(self):
        department = self.check_dept() #type: ignore

        if department is None:
            print('Department not found')
            return


        department.show_employees() #type: ignore

class Department:
    def __init__(self, dept_name: str) -> None:
        self.dept_name = dept_name
        self.employees = []

    def __repr__(self) -> str:
        return self.dept_name

    def add_employee(self):

    #   -----Employee Data-------
        
        employee_name = input('Enter Employee Name: ')
        employee_id = input('Enter Employee Id: ')
        experience = input('Enter Work Experience: ')
        desig_post = input('Enter Post: ')

    #   ---------Employee Post------------

        employee = Employee(employee_name= employee_name, employee_id= employee_id, experience= experience, post= desig_post, salary= '0')

    # ------Add Employee------

        self.employees.append(employee) #type: ignore

    def find_employee(self): #type: ignore
        employee_id = input('Enter Employee Id: ')
        for employee in self.employees: #type: ignore
            if employee.employee_id == employee_id: #type: ignore

                return employee #type: ignore

    def remove_employee(self):
        employee = self.find_employee() #type: ignore

        if employee is None:
            print('Employee not found')
            return

        self.employees.remove(employee) #type: ignore

    def update_employee(self):
        employee = self.find_employee() #type: ignore

        if employee is None:
            print('Employee not found')
            return

        update_input = input('What would you like to update: ') #type: ignore
        for key in employee.__dict__: #type: ignore
            if update_input == key:
                setattr(employee, key, input(f'Enter New {key}: ')) #type: ignore
                if key == 'post':
                    employee.cal_salary() #type: ignore

    def display_employee_details(self, employee): #type: ignore
        print(f'{employee.employee_name.center(15)} |', #type: ignore
                  f'{employee.employee_id.center(10)} |', #type: ignore
                  f'{(str(employee.experience) + ' years').center(10)} |', #type: ignore
                  f'{employee.post.center(10)} |', #type: ignore 
                  f'{str(employee.salary).center(10)}') #type: ignore

    def search_employee(self):
        employee = self.find_employee() #type: ignore

        if employee is None:
            print('Employee not found')
            return

        print(f'{'Name'.center(15)} | {'ID'.center(10)} | {'Experience'.center(10)} | {'Post'.center(10)} | {'Salary'.center(10)}')
        self.display_employee_details(employee= employee) #type: ignore

    def show_employees(self):
        print(f'{'Name'.center(15)} | {'ID'.center(10)} | {'Experience'.center(10)} | {'Post'.center(10)} | {'Salary'.center(10)}')
        for employee in self.employees: #type: ignore
            self.display_employee_details(employee= employee) #type: ignore

class Employee:
    positions = {'Worker': 80000, 'Customer Service': 40000, 'Manager': 200000}
    
    def __init__(self, employee_name: str, employee_id: str, experience: str, post: str, salary: str) -> None:
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.experience = experience
        self.post = post
        self.salary = salary
        self.cal_salary()

    def cal_salary(self):
        self.salary = str(Employee.positions[self.post])

    def __str__(self) -> str:
        return self.employee_name
    
    def __repr__(self) -> str:
        return self.employee_name

