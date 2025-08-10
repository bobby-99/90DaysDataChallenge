# 26. Remove Duplicates from sorted array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        w = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[w] = nums[r]
                w += 1

        return w

# 189. Rotate array by n places

def rotateArray(nums: list[int], k: int):
    n = len(nums)
    k = k % n # for handling multiple iterations (if k > n)
    if not nums or n == 1:
        return nums

    def reverse(num, l, r):
        while l < r:
            num[l], num[r] = num[r], num[l]
            l += 1
            r -= 1

    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)

# 869. Reordered power of two

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        allpowers = {"011237","0122579","012356789","0124","0134449", "0145678","01466788","0248","0368888","0469","1","112234778","11266777","122446","125","128","1289","13468","16","2","224588","23","23334455","234455668","23678","256","35566","4","46","8"}

        digit = sorted([x for x in str(n)])
        s = ''.join(digit)
        return True if s in allpowers else False