# Input: Two integers, n and m.
# Check if m is non-zero:
# If m is zero, return False immediately because division by zero is undefined.
# Compute the remainder:
# Calculate the remainder when n is divided by m (i.e., n % m).
# Check the remainder:
# If the remainder is 0, return True (since n is divisible by m).
# If the remainder is not 0, return False (since n is not divisible by m).
# End
def multple(n,m=0):
    if m==0:
        return ZeroDivisionError
    # rem=0
    rem=n%m
    if rem==0:
        return True
    else :
        return False
print(multple(2))


