## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Do is a animal
class Dog(Animal):

    def __init__(self, name):
        ## Animal has a name
        self.name = name

## Cat is a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has a name
        self.name = name

## Person is a object
class Person(object):

    def __init__(self, name):
        ## person has a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is a person
class Employee(Person):

    def __init__(self, name, salary):
        ## run the __init__ method of a parent class reliably
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

## Halibut is a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## mary has a pet called satan
mary.pet = satan

## frank is an employee with 120000 salary
frank = Employee("Frank", 120000)

## frank has a pet called rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a salmon
crouse = Salmon()

## harry is a halibut
harry = Halibut()
