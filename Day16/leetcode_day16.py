
# POTD 1323. Maximum 69 Number

def maximum69Number (self, num: int) -> int:
    return int(str(num).replace('6','9', 1))


# Brute Force

def twoSum(self, nums: list[int], target: int) -> list[int]:
    arr = []
    n = len(nums)
    for i in range(1,  n + 1):
        for j in range(i+ 1, n + 1):
            if i + j == target:
                arr.append(i)
                arr.append(j)

    return arr

# Hash-Map

def twoSum(self, nums: list[int], target: int) -> list[int]:

    visited = {}

    for i, num in enumerate(nums):
        if target - num in visited:
            return [visited[target - num], i]
        visited[nums[i]] = i
    return []

