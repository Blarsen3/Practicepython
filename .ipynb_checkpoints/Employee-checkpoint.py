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

class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_number, shift_number, hourly_rate):
        super().__init__(emp_name, emp_number)
        self.shift_number = shift_number
        self.hourly_rate - hourly_rate

    def get_shift_number(self):
        return self.shift_number

    def get_hourly_rate(self):
        return self.hourly_rate

    def set_shift_number(self, shift_number):
        self.shift_number = shift_number

    def set_hourly_rate(self, hourly_rate):
        self.hourly_rate = hourly_rate