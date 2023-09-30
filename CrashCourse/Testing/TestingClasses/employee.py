class Employee:
    """Allow employees to be created"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialises attributes of employee class"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, pay_raise=5000):
        """Gives employee a 5000 raise"""
        self.annual_salary += pay_raise

Alan = Employee("Alan", "Wright", 10000)
Alan.give_raise()
print(Alan)