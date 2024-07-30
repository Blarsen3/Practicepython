class Employee:
    def __init__(self, emp_name, emp_number):
        self.emp_name = emp_name
        self.emp_number = emp_number
    
    def get_emp_name(self):
        return self.emp_name
    
    def get_emp_number(self):
        return self.emp_number
    
    def set_emp_name(self, emp_name):
        self.emp_name = emp_name
    
    def set_emp_number(self, emp_number):
        self.emp_number = emp_number