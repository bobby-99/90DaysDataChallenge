# 342. Power of Four

def PowerOfFour(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 4 == 0:
            n /= 4
        else:
            return False
    return True

print(PowerOfFour(16))