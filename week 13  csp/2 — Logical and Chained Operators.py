# Objective:
# Students will use logical (and, or, not) and chained comparison operators in Python to build compound conditions.

# Key Notes:
# and → Both conditions must be True
# or  → At least one condition must be True
# not → Inverts (flips) True/False
# You can chain comparisons: 1 < x < 5

# -------------------------------
# EXAMPLES
# -------------------------------

x = 10

print(x > 5 and x < 15)   # True, because both 10 > 5 and 10 < 15 are True
print(x < 5 or x == 10)   # True, because x == 10 is True (only one side needs to be True)
print(not(x == 10))       # False, because x == 10 is True, and not(True) = False
print(1 < x < 20)         # True, because x is between 1 and 20


# -------------------------------
# PRACTICE PROBLEMS
# -------------------------------

# 1. Score/grade checking
score = 85  # Example score

# Use chained comparisons to check score ranges
if 90 <= score <= 100:
    print("A")  # 90–100
elif 80 <= score <= 89:
    print("B")  # 80–89
elif 70 <= score <= 79:
    print("C")  # 70–79
elif 60 <= score <= 69:
    print("D")  # 60–69
else:
    print("F")  # below 60


# 2. Check if a number is between 50 and 100 (inclusive)
number = 75
print(50 <= number <= 100)   # True, because 75 is between 50 and 100


# 3. Check if a number is NOT equal to 0 and greater than 10
num = 15
print(num != 0 and num > 10)  # True, because 15 is not 0 and it’s greater than 10


# 4. Use chained comparison to check if 3 < 4 < 5
print(3 < 4 < 5)  # True, because 3 < 4 and 4 < 5 are both True


# 5. Challenge: Create a password rule using logical operators
password = "secure123"

# Rule: password must be at least 8 characters long AND contain at least one digit
# len(password) >= 8 → checks length
# any(char.isdigit() for char in password) → checks for at least one number
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is strong enough.")
else:
    print("Password must be at least 8 characters long and contain a number.")
