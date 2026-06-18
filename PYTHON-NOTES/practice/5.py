students = [
    ("Pavan", 22),
    ("Rahul", 20),
    ("Arjun", 25)
]

students.sort(key=lambda x: x[1])
# students.sort(key=lambda student: student[1])

print(students)

def get_age(x):
    return x[1]

students.sort(key=get_age)
print(students)


# =========================

# ==========================================================
# 5.py - PYTHON FUNCTIONS COMPLETE EXAMPLES
# Topics:
# 1. Function Creation
# 2. Function Calling
# 3. Parameters
# 4. Arguments
# 5. Return Values
# 6. Default Arguments
# 7. Keyword Arguments
# 8. *args
# 9. **kwargs
# 10. Local Variables
# 11. Global Variables
# 12. Lambda Functions
# ==========================================================


# ==========================================================
# SIMPLE FUNCTION
# ==========================================================

def greet():
    print("Hello Python")


greet()


# ==========================================================
# FUNCTION WITH ONE PARAMETER
# ==========================================================

def welcome(name):
    print("Welcome", name)


welcome("Pavan")


# ==========================================================
# FUNCTION WITH MULTIPLE PARAMETERS
# ==========================================================

def student(name, age, city):
    print("Name :", name)
    print("Age  :", age)
    print("City :", city)


student("Pavan", 22, "Bangalore")


# ==========================================================
# ADDITION FUNCTION
# ==========================================================

def add(a, b):
    print("Addition =", a + b)


add(10, 20)


# ==========================================================
# SUBTRACTION FUNCTION
# ==========================================================

def subtract(a, b):
    print("Subtraction =", a - b)


subtract(50, 20)


# ==========================================================
# MULTIPLICATION FUNCTION
# ==========================================================

def multiply(a, b):
    print("Multiplication =", a * b)


multiply(10, 5)


# ==========================================================
# DIVISION FUNCTION
# ==========================================================

def divide(a, b):
    print("Division =", a / b)


divide(100, 5)


# ==========================================================
# FUNCTION WITH RETURN VALUE
# ==========================================================

def add_numbers(a, b):
    return a + b


result = add_numbers(100, 200)

print("Result =", result)


# ==========================================================
# RETURN MULTIPLE VALUES
# ==========================================================

def calculate(a, b):

    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(20, 10)

print(result)


# ==========================================================
# RETURNING STRING
# ==========================================================

def get_name():
    return "Pavan"


name = get_name()

print(name)


# ==========================================================
# FUNCTION WITH DEFAULT ARGUMENT
# ==========================================================

def greet_user(name="Guest"):
    print("Hello", name)


greet_user()

greet_user("Pavan")


# ==========================================================
# MULTIPLE DEFAULT ARGUMENTS
# ==========================================================

def employee(name="Unknown", salary=0):
    print(name, salary)


employee()

employee("Pavan", 50000)


# ==========================================================
# KEYWORD ARGUMENTS
# ==========================================================

def person(name, age, city):
    print(name, age, city)


person(
    age=22,
    city="Bangalore",
    name="Pavan"
)


# ==========================================================
# POSITIONAL ARGUMENTS
# ==========================================================

def display(a, b, c):
    print(a, b, c)


display(10, 20, 30)


# ==========================================================
# *ARGS
# ==========================================================

def total(*numbers):

    print("Numbers:", numbers)

    print("Sum:", sum(numbers))


total(10, 20, 30)

total(1, 2, 3, 4, 5)


# ==========================================================
# *ARGS LOOPING
# ==========================================================

def show_numbers(*data):

    for item in data:

        print(item)


show_numbers(10, 20, 30, 40, 50)


# ==========================================================
# **KWARGS
# ==========================================================

def student_info(**details):

    print(details)


student_info(
    name="Pavan",
    age=22,
    city="Bangalore"
)


# ==========================================================
# **KWARGS LOOPING
# ==========================================================

def employee_info(**data):

    for key, value in data.items():

        print(key, ":", value)


employee_info(
    name="Pavan",
    age=22,
    salary=50000
)


# ==========================================================
# LOCAL VARIABLE
# ==========================================================

def local_example():

    x = 100

    print("Local Variable =", x)


local_example()


# ==========================================================
# GLOBAL VARIABLE
# ==========================================================

x = 500


def global_example():

    print("Global Variable =", x)


global_example()


# ==========================================================
# GLOBAL KEYWORD
# ==========================================================

count = 0


def increase():

    global count

    count += 1


increase()

print(count)


# ==========================================================
# FUNCTION INSIDE FUNCTION
# ==========================================================

def outer():

    print("Outer Function")

    def inner():

        print("Inner Function")

    inner()


outer()


# ==========================================================
# CHECK EVEN NUMBER
# ==========================================================

def is_even(number):

    if number % 2 == 0:
        return True

    return False


print(is_even(10))

print(is_even(11))


# ==========================================================
# CHECK ODD NUMBER
# ==========================================================

def is_odd(number):

    return number % 2 != 0


print(is_odd(11))


# ==========================================================
# FACTORIAL USING FUNCTION
# ==========================================================

def factorial(number):

    result = 1

    for i in range(1, number + 1):

        result *= i

    return result


print(factorial(5))


# ==========================================================
# SUM OF LIST
# ==========================================================

def list_sum(numbers):

    total = 0

    for num in numbers:

        total += num

    return total


print(list_sum([10, 20, 30, 40]))


# ==========================================================
# MAX VALUE
# ==========================================================

def find_max(numbers):

    return max(numbers)


print(find_max([10, 50, 100, 30]))


# ==========================================================
# LAMBDA FUNCTION BASIC
# ==========================================================

square = lambda x: x * x

print(square(5))


# ==========================================================
# LAMBDA WITH TWO ARGUMENTS
# ==========================================================

add = lambda a, b: a + b

print(add(10, 20))


# ==========================================================
# LAMBDA WITH THREE ARGUMENTS
# ==========================================================

multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))


# ==========================================================
# LAMBDA INSIDE SORT
# ==========================================================

students = [

    ("Pavan", 22),
    ("Rahul", 18),
    ("Arjun", 25)

]

students.sort(
    key=lambda student: student[1]
)

print(students)


# ==========================================================
# LAMBDA WITH FILTER
# ==========================================================

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(

    filter(
        lambda x: x % 2 == 0,
        numbers
    )

)

print(even_numbers)


# ==========================================================
# LAMBDA WITH MAP
# ==========================================================

numbers = [1, 2, 3, 4, 5]

squares = list(

    map(
        lambda x: x * x,
        numbers
    )

)

print(squares)


# ==========================================================
# RECURSION
# Function Calling Itself
# ==========================================================

def recursive_count(number):

    if number == 0:
        return

    print(number)

    recursive_count(number - 1)


recursive_count(5)


# ==========================================================
# RECURSIVE FACTORIAL
# ==========================================================

def recursive_factorial(number):

    if number == 1:
        return 1

    return number * recursive_factorial(number - 1)


print(recursive_factorial(5))


# ==========================================================
# FUNCTION RETURNING DICTIONARY
# ==========================================================

def get_student():

    return {
        "name": "Pavan",
        "age": 22
    }


print(get_student())


# ==========================================================
# FUNCTION RETURNING LIST
# ==========================================================

def get_numbers():

    return [10, 20, 30, 40]


print(get_numbers())


# ==========================================================
# END
# ==========================================================

print("\nPython Functions Examples Completed Successfully!")

