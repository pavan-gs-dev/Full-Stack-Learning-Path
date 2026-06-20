
# ==========================================================
# 7.py - PYTHON OOP COMPLETE EXAMPLES
# Topics:
# 1. Class
# 2. Object
# 3. Constructor
# 4. Instance Variables
# 5. Class Variables
# 6. Methods
# 7. Inheritance
# 8. Polymorphism
# 9. Encapsulation
# 10. Abstraction
# 11. Access Modifiers
# ==========================================================


# ==========================================================
# CLASS AND OBJECT
# ==========================================================

class Student:

    pass


student1 = Student()

print(student1)


# ==========================================================
# CLASS ATTRIBUTES
# ==========================================================

class Student:

    name = "Pavan"
    age = 22


student = Student()

print(student.name)
print(student.age)


# ==========================================================
# METHODS
# ==========================================================

class Student:

    def show(self):

        print("Hello Student")


student = Student()

student.show()


# ==========================================================
# CONSTRUCTOR
# ==========================================================

class Student:

    def __init__(self):

        print("Constructor Called")


student = Student()


# ==========================================================
# CONSTRUCTOR WITH PARAMETERS
# ==========================================================

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student = Student("Pavan", 22)

print(student.name)
print(student.age)


# ==========================================================
# MULTIPLE OBJECTS
# ==========================================================

class Student:

    def __init__(self, name):

        self.name = name


s1 = Student("Pavan")
s2 = Student("Rahul")
s3 = Student("Arjun")

print(s1.name)
print(s2.name)
print(s3.name)


# ==========================================================
# INSTANCE VARIABLES
# ==========================================================

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


employee = Employee("Pavan", 50000)

print(employee.name)
print(employee.salary)


# ==========================================================
# CLASS VARIABLES
# ==========================================================

class Student:

    college = "ABC College"

    def __init__(self, name):

        self.name = name


s1 = Student("Pavan")
s2 = Student("Rahul")

print(Student.college)

print(s1.college)
print(s2.college)


# ==========================================================
# OBJECT METHODS
# ==========================================================

class Student:

    def __init__(self, name):

        self.name = name

    def show(self):

        print("Student Name:", self.name)


student = Student("Pavan")

student.show()


# ==========================================================
# INHERITANCE
# ==========================================================

class Animal:

    def eat(self):

        print("Animal is Eating")


class Dog(Animal):

    pass


dog = Dog()

dog.eat()


# ==========================================================
# MULTILEVEL INHERITANCE
# ==========================================================

class Animal:

    def eat(self):

        print("Eating")


class Dog(Animal):

    def bark(self):

        print("Barking")


class Puppy(Dog):

    def cry(self):

        print("Crying")


puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.cry()


# ==========================================================
# METHOD OVERRIDING
# ==========================================================

class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Dog Barks")


dog = Dog()

dog.sound()


# ==========================================================
# POLYMORPHISM
# ==========================================================

class Dog:

    def sound(self):

        print("Bark")


class Cat:

    def sound(self):

        print("Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ==========================================================
# ENCAPSULATION
# ==========================================================

class BankAccount:

    def __init__(self):

        self.balance = 10000

    def show_balance(self):

        print("Balance:", self.balance)


account = BankAccount()

account.show_balance()


# ==========================================================
# PROTECTED VARIABLE
# ==========================================================

class Employee:

    def __init__(self):

        self._salary = 50000


employee = Employee()

print(employee._salary)


# ==========================================================
# PRIVATE VARIABLE
# ==========================================================

class Employee:

    def __init__(self):

        self.__salary = 50000

    def show_salary(self):

        print(self.__salary)


employee = Employee()

employee.show_salary()


# ==========================================================
# PRIVATE METHOD
# ==========================================================

class Test:

    def __private_method(self):

        print("Private Method")

    def show(self):

        self.__private_method()


obj = Test()

obj.show()


# ==========================================================
# GETTER METHOD
# ==========================================================

class Student:

    def __init__(self):

        self.__marks = 95

    def get_marks(self):

        return self.__marks


student = Student()

print(student.get_marks())


# ==========================================================
# SETTER METHOD
# ==========================================================

class Student:

    def __init__(self):

        self.__marks = 0

    def set_marks(self, marks):

        self.__marks = marks

    def get_marks(self):

        return self.__marks


student = Student()

student.set_marks(90)

print(student.get_marks())


# ==========================================================
# ABSTRACTION
# ==========================================================

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass


class Car(Vehicle):

    def start(self):

        print("Car Started")


car = Car()

car.start()


# ==========================================================
# MULTIPLE INHERITANCE
# ==========================================================

class Father:

    def skill1(self):

        print("Driving")


class Mother:

    def skill2(self):

        print("Cooking")


class Child(Father, Mother):

    pass


child = Child()

child.skill1()
child.skill2()


# ==========================================================
# STATIC METHOD
# ==========================================================

class Calculator:

    @staticmethod
    def add(a, b):

        return a + b


print(Calculator.add(10, 20))


# ==========================================================
# CLASS METHOD
# ==========================================================

class School:

    school_name = "ABC School"

    @classmethod
    def get_school(cls):

        return cls.school_name


print(School.get_school())


# ==========================================================
# OBJECT COUNT EXAMPLE
# ==========================================================

class Student:

    count = 0

    def __init__(self):

        Student.count += 1


s1 = Student()
s2 = Student()
s3 = Student()

print(Student.count)


# ==========================================================
# REAL WORLD EXAMPLE
# ==========================================================

class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def display(self):

        print("Product:", self.name)
        print("Price:", self.price)


product1 = Product("Laptop", 50000)

product1.display()


# ==========================================================
# END
# ==========================================================

print("\nPython OOP Examples Completed Successfully!")
