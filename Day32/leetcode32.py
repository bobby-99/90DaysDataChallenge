# 11. Container With Most Water

class Solution:

    def maxArea(self, height: list[int]) -> int:

        n = len(height)

        l = 0

        r = n - 1

        max_area = 0

        while l < r:

            w = r - l

            h = min(height[l], height[r])

            a = w * h

            max_area = max(max_area, a)

            if height[l] < height[r]:

                l += 1

            else:

                r -= 1

        return max_area

# Time Complexity: O(n)

# Space Complexity: O(1)


## 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1  # Pointer for nums1 valid elements
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for merged result in nums1
    
        # Merge from the end
        while p2 >= 0 and p1 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
    
        # If any elements remain in nums2, copy them (nums1's remaining part is already sorted)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1