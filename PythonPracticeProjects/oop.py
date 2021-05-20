# Corey Schafer.  Python OOP Tutorial 1: Classes and Instances
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&ab_channel=CoreySchafer

# Creating a class to fill in later
class EmployeeBadClass:
    pass

emp_1 = EmployeeBadClass()
emp_2 = EmployeeBadClass()
# emp_1 is instance of Employee class
# Employee() is the class - a blueprint for creating instances

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'test.user@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

# The below is a quicker way of doing this - 10 lines instead of 14.
# Would get even more efficient with more instances

class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@company.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return self.first + " " + self.last
        #        return '{} {}'.format(self.first, self.last) #another way of doing it

    def fullname_fail(): #this will fail because there is no self
        return self.first + " " + self.last

    def apply_raise(self):
            #self.pay = int(self.pay * raise_amount) #will error because need to declare variable as class variable
            self.pay = int(self.pay * self.raise_amount)

    # This class method changes a class variable
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        pass

    # This class method creates a shortcuty for creating employee from a string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # This static method
    # Static methods associated with class but don't use class variables
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True # No need for "else" here as return ends the code

emp_3 = Employee('Alan', 'Wright', 70000) # emp_3 is passed in as self
emp_4 = Employee('Lorraine', 'Lisk', 1000000) # emp_4 is passed in as self

print(emp_3.email)
print(emp_4.email)
print(emp_3.fullname())
# print(emp_3.fullname_fail())
# this will fail because emp_3 gets passed as argument automatically but function does not expect it


# THESE TWO BELOW ARE THE SAME THING
print(emp_3.fullname())
# get the emp_3 instance and call the fullname function on it

print(Employee.fullname(emp_3))
# get the fullname function from the employee class and pass it the instance "emp_3" as an argument

print(emp_3.pay)
print(emp_4.pay)
emp_3.apply_raise()
print(emp_3.pay)
print(emp_4.pay)
print(Employee.__dict__)
print(emp_3.__dict__)


print(Employee.raise_amount)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)

# Use class method as alternative constructor to create customer from a string
emp_str_1 = "dave-mendez-99000"
new_emp_1 = Employee.from_string(emp_str_1)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
