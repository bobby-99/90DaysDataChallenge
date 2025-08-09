# 344. Reverse string
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and bin(n).count('1') == 1