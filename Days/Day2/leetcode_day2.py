# Leet code day 2 Problems 


# 286. Missing number
# Task is to find the missing number from a given list of unique numbers
def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual


# 905. Sort Array by Parity 
# Even numbers at start and odd numbers at end of list
def sortArrayByParity(self, nums: list[int]) -> list[int]:
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even + odd