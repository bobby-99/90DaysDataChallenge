# LeetCode day 1

# Check Palindrome
def ifPalindrome(s):
    return str(s) == str(s)[::-1]

# Second Largest
def secondHighest(s: str) -> int:
    second_largest = -1
    nums = []
    for char in s:
        if '0' <= char <= '9':
            char = int(char)
            nums.append(char)
    largest = nums[0]
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    return second_largest


# Contains Duplicates
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False