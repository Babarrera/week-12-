# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:
# Comparison operators compare two values and return either True or False.
# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#  Predict the output of the following comparisons:
print(10 > 5)          # True
print(7 == 2 * 3 + 1)  # True (7 == 7)
print(8 != 8)          # False
print(4 <= 2 + 2)      # True (4 <= 4)


#  Write 3 examples that result in True:
print(15 > 10)          # True
print("cat" != "dog")   # True
print(5 + 5 == 10)      # True

#  Write 3 examples that result in False:
print(12 < 8)           # False
print(9 == 5)           # False
print(7 >= 10)          # False


#  Create a simple grade-checking condition:
score = 75
print(score >= 60)   # True → student passed

# Optional: Add a message for clarity
if score >= 60:
    print("You passed the test!")
else:
    print("You failed the test.")


# Bonus: Password validation example
password = "mypassword1"

# Check if the password is at least 8 characters long AND has at least one digit
print(len(password) >= 8 and any(char.isdigit() for char in password))  # True
