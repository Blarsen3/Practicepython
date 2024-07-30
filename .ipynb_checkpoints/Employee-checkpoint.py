
class Employee:
    def __init__(self, name='', number=''):
        self._name = name
        self._number = number

    # Accessor methods
    def get_name(self):
        return self._name

    def get_number(self):
        return self._number

    # Mutator methods
    def set_name(self, name):
        self._name = name

    def set_number(self, number):
        self._number = number

class ProductionWorker(Employee):
    def __init__(self, name='', number='', shift=1, hourly_pay_rate=0.0):
        super().__init__(name, number)
        self._shift = shift
        self._hourly_pay_rate = hourly_pay_rate

    # Accessor methods
    def get_shift(self):
        return self._shift

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    # Mutator methods
    def set_shift(self, shift):
        if shift in [1, 2]:
            self._shift = shift
        else:
            print("Invalid shift number. Please enter 1 for day shift or 2 for night shift.")

    def set_hourly_pay_rate(self, hourly_pay_rate):
        if hourly_pay_rate >= 0:
            self._hourly_pay_rate = hourly_pay_rate
        else:
            print("Hourly pay rate cannot be negative.")
