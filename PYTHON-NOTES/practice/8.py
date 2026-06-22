
# ==========================================================
# 8.py - PYTHON EXCEPTION HANDLING COMPLETE EXAMPLES
# Topics:
# 1. try
# 2. except
# 3. Multiple except
# 4. Exception as e
# 5. else
# 6. finally
# 7. raise
# 8. Custom Exceptions
# 9. Real World Examples
# ==========================================================


# ==========================================================
# BASIC TRY EXCEPT
# ==========================================================

print("\n===== BASIC TRY EXCEPT =====")

try:

    result = 10 / 0

    print(result)

except:

    print("Cannot Divide By Zero")


# ==========================================================
# HANDLE SPECIFIC EXCEPTION
# ==========================================================

print("\n===== SPECIFIC EXCEPTION =====")

try:

    result = 10 / 0

except ZeroDivisionError:

    print("ZeroDivisionError Occurred")


# ==========================================================
# VALUE ERROR
# ==========================================================

print("\n===== VALUE ERROR =====")

try:

    number = int("abc")

except ValueError:

    print("Invalid Integer Value")


# ==========================================================
# INDEX ERROR
# ==========================================================

print("\n===== INDEX ERROR =====")

try:

    numbers = [10, 20, 30]

    print(numbers[10])

except IndexError:

    print("Index Out Of Range")


# ==========================================================
# KEY ERROR
# ==========================================================

print("\n===== KEY ERROR =====")

try:

    student = {
        "name": "Pavan"
    }

    print(student["age"])

except KeyError:

    print("Key Not Found")


# ==========================================================
# FILE NOT FOUND ERROR
# ==========================================================

print("\n===== FILE NOT FOUND =====")

try:

    file = open("unknown.txt")

except FileNotFoundError:

    print("File Not Found")


# ==========================================================
# MULTIPLE EXCEPT BLOCKS
# ==========================================================

print("\n===== MULTIPLE EXCEPT =====")

try:

    num = int(input("Enter Number: "))

    result = 100 / num

    print(result)

except ValueError:

    print("Please Enter Valid Number")

except ZeroDivisionError:

    print("Cannot Divide By Zero")


# ==========================================================
# EXCEPTION AS e
# ==========================================================

print("\n===== EXCEPTION AS e =====")

try:

    result = 10 / 0

except Exception as e:

    print("Error:", e)


# ==========================================================
# ELSE BLOCK
# ==========================================================

print("\n===== ELSE BLOCK =====")

try:

    result = 100 / 5

except ZeroDivisionError:

    print("Error")

else:

    print("Success")
    print("Result =", result)


# ==========================================================
# FINALLY BLOCK
# ==========================================================

print("\n===== FINALLY BLOCK =====")

try:

    result = 10 / 0

except ZeroDivisionError:

    print("Error")

finally:

    print("Always Executes")


# ==========================================================
# TRY EXCEPT ELSE FINALLY
# ==========================================================

print("\n===== FULL STRUCTURE =====")

try:

    result = 100 / 10

except ZeroDivisionError:

    print("Error")

else:

    print("No Error")

finally:

    print("Execution Completed")


# ==========================================================
# FILE HANDLING WITH FINALLY
# ==========================================================

print("\n===== FILE WITH FINALLY =====")

file = None

try:

    file = open("data.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File Not Found")

finally:

    if file:

        file.close()

        print("File Closed")


# ==========================================================
# MANUAL EXCEPTION USING RAISE
# ==========================================================

print("\n===== RAISE EXCEPTION =====")

try:

    age = -10

    if age < 0:

        raise ValueError(
            "Age Cannot Be Negative"
        )

except ValueError as e:

    print(e)


# ==========================================================
# PASSWORD VALIDATION
# ==========================================================

print("\n===== PASSWORD VALIDATION =====")

try:

    password = "123"

    if len(password) < 6:

        raise ValueError(
            "Password Must Be At Least 6 Characters"
        )

except ValueError as e:

    print(e)


# ==========================================================
# SALARY VALIDATION
# ==========================================================

print("\n===== SALARY VALIDATION =====")

try:

    salary = -1000

    if salary < 0:

        raise ValueError(
            "Salary Cannot Be Negative"
        )

except ValueError as e:

    print(e)


# ==========================================================
# CUSTOM EXCEPTION
# ==========================================================

print("\n===== CUSTOM EXCEPTION =====")

class InvalidAgeError(Exception):

    pass


try:

    age = -5

    if age < 0:

        raise InvalidAgeError(
            "Age Cannot Be Negative"
        )

except InvalidAgeError as e:

    print(e)


# ==========================================================
# BANK EXCEPTION
# ==========================================================

print("\n===== BANK EXCEPTION =====")

class InsufficientBalanceError(Exception):

    pass


try:

    balance = 1000

    withdraw = 5000

    if withdraw > balance:

        raise InsufficientBalanceError(
            "Insufficient Balance"
        )

except InsufficientBalanceError as e:

    print(e)


# ==========================================================
# STUDENT MARKS VALIDATION
# ==========================================================

print("\n===== MARKS VALIDATION =====")

class InvalidMarksError(Exception):

    pass


try:

    marks = 150

    if marks < 0 or marks > 100:

        raise InvalidMarksError(
            "Marks Must Be Between 0 and 100"
        )

except InvalidMarksError as e:

    print(e)


# ==========================================================
# ATM EXAMPLE
# ==========================================================

print("\n===== ATM EXAMPLE =====")

try:

    amount = int(input("Enter Amount: "))

    if amount <= 0:

        raise ValueError(
            "Amount Must Be Greater Than Zero"
        )

    print("Withdrawal Successful")

except ValueError as e:

    print(e)

finally:

    print("Transaction Finished")


# ==========================================================
# LOGIN EXAMPLE
# ==========================================================

print("\n===== LOGIN EXAMPLE =====")

try:

    username = "admin"
    password = "1234"

    entered_username = "admin"
    entered_password = "1111"

    if entered_password != password:

        raise ValueError(
            "Invalid Password"
        )

    print("Login Success")

except ValueError as e:

    print(e)


# ==========================================================
# NESTED TRY EXCEPT
# ==========================================================

print("\n===== NESTED TRY =====")

try:

    try:

        result = 10 / 0

    except ZeroDivisionError:

        print("Inner Exception Handled")

except:

    print("Outer Exception")


# ==========================================================
# MULTIPLE EXCEPT IN ONE LINE
# ==========================================================

print("\n===== MULTIPLE ERRORS =====")

try:

    number = int("abc")

except (ValueError, TypeError):

    print("ValueError or TypeError Occurred")


# ==========================================================
# GENERIC EXCEPTION
# ==========================================================

print("\n===== GENERIC EXCEPTION =====")

try:

    result = 10 / 0

except Exception as e:

    print("Caught By Generic Exception")
    print(e)


# ==========================================================
# END
# ==========================================================

print("\nException Handling Examples Completed Successfully!")

