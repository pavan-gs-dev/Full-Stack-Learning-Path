
# ==========================================================
# 9.py - MODULES, PACKAGES, IMPORTS, PIP, VENV
# Complete Examples
# ==========================================================


# ==========================================================
# IMPORT MODULE
# ==========================================================

import math

print("\n===== MATH MODULE =====")

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.pi)


# ==========================================================
# FROM IMPORT
# ==========================================================

from math import sqrt

print("\n===== FROM IMPORT =====")

print(sqrt(49))


# ==========================================================
# IMPORT MULTIPLE FUNCTIONS
# ==========================================================

from math import sqrt, pi

print("\n===== MULTIPLE IMPORT =====")

print(sqrt(64))
print(pi)


# ==========================================================
# ALIAS
# ==========================================================

import math as m

print("\n===== ALIAS =====")

print(m.sqrt(81))


# ==========================================================
# RANDOM MODULE
# ==========================================================

import random

print("\n===== RANDOM MODULE =====")

print(random.randint(1, 10))

print(random.choice([
    "Apple",
    "Banana",
    "Mango"
]))


# ==========================================================
# DATETIME MODULE
# ==========================================================

import datetime

print("\n===== DATETIME MODULE =====")

current_date = datetime.datetime.now()

print(current_date)


# ==========================================================
# OS MODULE
# ==========================================================

import os

print("\n===== OS MODULE =====")

print("Current Folder:")
print(os.getcwd())


# ==========================================================
# SYSTEM INFORMATION
# ==========================================================

import sys

print("\n===== SYS MODULE =====")

print(sys.version)


# ==========================================================
# JSON MODULE
# ==========================================================

import json

print("\n===== JSON MODULE =====")

student = {

    "name": "Pavan",
    "age": 22
}

json_data = json.dumps(student)

print(json_data)


# ==========================================================
# JSON STRING TO DICTIONARY
# ==========================================================

print("\n===== JSON LOADS =====")

json_string = '''

{
    "city":"Bangalore",
    "state":"Karnataka"
}

'''

python_object = json.loads(
    json_string
)

print(python_object)


# ==========================================================
# SAVE JSON FILE
# ==========================================================

print("\n===== JSON FILE WRITE =====")

data = {

    "name": "Pavan",
    "skills": [
        "Python",
        "SQL"
    ]
}

with open(

    "student.json",

    "w"

) as file:

    json.dump(
        data,
        file,
        indent=4
    )

print("student.json Created")


# ==========================================================
# READ JSON FILE
# ==========================================================

print("\n===== JSON FILE READ =====")

with open(

    "student.json",

    "r"

) as file:

    json_data = json.load(file)

print(json_data)


# ==========================================================
# USER DEFINED FUNCTIONS
# ==========================================================

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


print("\n===== USER FUNCTIONS =====")

print(add(10, 20))
print(subtract(50, 20))


# ==========================================================
# __name__
# ==========================================================

print("\n===== __name__ =====")

print(__name__)


# ==========================================================
# MAIN BLOCK
# ==========================================================

if __name__ == "__main__":

    print(
        "This File Is Running Directly"
    )


# ==========================================================
# EXAMPLE OF USER DEFINED MODULE
# ==========================================================

print("\n===== MODULE EXAMPLE =====")

print("""

Create calculator.py

--------------------------------

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

--------------------------------

Create main.py

import calculator

print(
    calculator.add(10,20)
)

--------------------------------

Output:
30

""")


# ==========================================================
# PACKAGE EXAMPLE
# ==========================================================

print("\n===== PACKAGE EXAMPLE =====")

print("""

Project Structure

project/

│
├── main.py
│
└── utilities/
    │
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py

Import:

from utilities.math_utils import add

""")


# ==========================================================
# REQUIREMENTS.TXT EXAMPLE
# ==========================================================

print("\n===== REQUIREMENTS.TXT =====")

requirements = """

requests==2.31.0
numpy==2.0.0
pandas==2.2.0

"""

print(requirements)


# ==========================================================
# PIP COMMANDS
# ==========================================================

print("\n===== PIP COMMANDS =====")

print("pip install requests")
print("pip install numpy")
print("pip install pandas")

print("pip list")
print("pip show requests")
print("pip uninstall requests")


# ==========================================================
# VIRTUAL ENVIRONMENT COMMANDS
# ==========================================================

print("\n===== VIRTUAL ENVIRONMENT =====")

print("""

Create Environment

python -m venv myenv

----------------------

Activate (Windows)

myenv\\Scripts\\activate

----------------------

Deactivate

deactivate

""")


# ==========================================================
# DIRECTORY LISTING
# ==========================================================

print("\n===== FILES IN CURRENT DIRECTORY =====")

for item in os.listdir():

    print(item)


# ==========================================================
# PATH EXISTS
# ==========================================================

print("\n===== PATH EXISTS =====")

print(
    os.path.exists(
        "student.json"
    )
)


# ==========================================================
# FILE SIZE
# ==========================================================

print("\n===== FILE SIZE =====")

if os.path.exists("student.json"):

    print(
        os.path.getsize(
            "student.json"
        ),
        "bytes"
    )


# ==========================================================
# RANDOM PASSWORD GENERATOR
# ==========================================================

print("\n===== RANDOM PASSWORD =====")

characters = (
    "abcdefghijklmnopqrstuvwxyz"
    "123456789"
)

password = ""

for i in range(8):

    password += random.choice(
        characters
    )

print(password)


# ==========================================================
# END
# ==========================================================

print(
    "\nModules & Packages Examples Completed Successfully!"
)

