# 167. TwoSum II - Input Array is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff]+1, i+1]  # 1-based
            seen[num] = i


# Duplicate characters
from collections import Counter

def duplicate_char(s: str, n: int):
    freq = Counter(s)
    ans = []
    for i in set(s):
        if freq[i] > 1:
            ans.append([i, freq[i]])
    ans.sort()
    return ans