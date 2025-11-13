# Objective:
# Learn how to compare values using Python’s comparison operators and interpret Boolean (True/False) results.

# Comparison operators:
# == means equal to
# != means not equal to
# > means greater than
# < means less than
# >= means greater than or equal to
# <= means less than or equal to

# = is assignment (it stores a value)
# == is comparison (it checks if values are equal)

# Example setup:
a = 3
b = 4

# Compare two values and print the results
print(a == b)   # False, because 3 is not equal to 4
print(a != b)   # True, because 3 is not equal to 4
print(a > b)    # False, because 3 is not greater than 4
print(a < b)    # True, because 3 is less than 4
print(a >= b)   # False, because 3 is not greater than or equal to 4
print(a <= b)   # True, because 3 is less than or equal to 4


# Predict the output of the following comparisons:
print(10 > 5)          # True, because 10 is greater than 5
print(7 == 2 * 3 + 1)  # True, because 2*3+1 equals 7
print(8 != 8)          # False, because both sides are equal
print(4 <= 2 + 2)      # True, because 4 is equal to 4


# Examples that result in True
print(15 > 10)          # True, 15 is greater than 10
print("cat" != "dog")   # True, because the strings are different
print(5 + 5 == 10)      # True, because 5+5 equals 10

# Examples that result in False
print(12 < 8)           # False, because 12 is not less than 8
print(9 == 5)           # False, because 9 is not equal to 5
print(7 >= 10)          # False, because 7 is not greater than or equal to 10


# Grade-checking condition
score = 75  # Example student score

# This comparison checks if the score is greater than or equal to 60
print(score >= 60)   # True, because 75 is greater than 60

# Using an if/else statement to print a message
if score >= 60:
    print("You passed the test!")  # This will run if the condition is True
else:
    print("You failed the test.")  # This runs if the condition is False


# Password validation example
password = "mypassword1"

# Check two things:
# 1. The password is at least 8 characters long
# 2. It contains at least one digit (number)
print(len(password) >= 8 and any(char.isdigit() for char in password))
# True, because "mypassword1" is longer than 8 characters and contains the number 1
