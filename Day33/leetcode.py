# 167. TwoSum II - Input Array is Sorted

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff]+1, i+1]  # 1-based
            seen[num] = i