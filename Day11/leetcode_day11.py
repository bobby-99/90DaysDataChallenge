# Create a list of exponents if n is a sum of powers of 2
def UsingBitManipulation(n: int):
    if n <= 0:
        return []
    powers = []
    i = 0
    while n > 0:
        if n & 1: powers.append(i)
        n >>= 1
        i += 1
    return powers

# My actual Intuition of the sum
def getPowerOfTwoSum(num: int):
    binary = bin(num)[2:]
    powers = []
    for i in range(len(binary)):
        if binary[len(binary) - 1 - i] == "1":
            powers.append(2**i)

    return powers

# Using that here
# 2438. Range Product Queries of Powers
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        powers = []
        if n <= 0:
            return powers
        i = 0
        while n > 0:
            if n & 1:
                powers.append(i)
            n >>= 1
            i += 1
        ans = []
        for left, right in queries:
            i = 1
            for j in range(left, right + 1):
                i = (i * powers[j]) % mod
            ans.append(i)
        return ans