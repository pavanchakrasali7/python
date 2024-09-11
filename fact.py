def fact(n):
    if n==1:
        return n
    else:
        return (n*fact(n-1))
n=int(input("enter the number"))
print(fact(n))

# Factorial:

# The factorial of a number n is the product of all positive integers from 1 to n.
# It is represented as n!.
# For example:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# 3! = 3 × 2 × 1 = 6
# The factorial of 1 is defined as 1.
# Recursion:

# Recursion is a process where a function calls itself to solve smaller subproblems until it reaches a base condition.
# In this case, the base condition is when the input number is 1.
# Step-by-Step Explanation:
# Input:

# The user is prompted to enter a number. This number is stored in the variable n.
# Base Case (When n equals 1):

# The function checks if the input n is 1.
# If n is 1, the function simply returns 1. This is the base case that stops the recursion, as we know that 1! = 1.
# Recursive Case (When n is greater than 1):

# If n is greater than 1, the function returns n * fact(n-1).
# This means the function calls itself with the value n-1, multiplying n by the result of fact(n-1).
# This continues until n becomes 1.