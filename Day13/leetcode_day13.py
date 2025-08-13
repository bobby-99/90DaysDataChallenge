# 326. Power of Three

def isPowerOfThree(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 3 == 0:
            n /= 3
        else:
            return False
    return True

print(isPowerOfThree(243))