
> Collection of elements stored in contiguous memory


# 217. Contains Duplicate

## Problem:  Check list for Duplicates

## Solution:

Two approaches. 
1. Nested Loops: for each element in list1, check for duplicate in the list2 by iterating over it
2. **Set approach**: 

```python
if len(set(nums)) == len(nums):
	return False
else:
	return True
```
### Notes:

- Time and space O(N) : Iterate through list and create set(time) and Space = size of set
- sets are fast
- Note: Empty set cannot be created through {}, it creates dictionary, unless you include values
- set is implemented as a Hash Table, so one expect to lookup/insert/delete in O(1) average

---

# 268. Missing Number

### Problem: 
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return _the only number in the range that is missing from the array. 

**Input:** nums = [3,0,1]
**Output:** 2

### Solution:

```python
# Solution 1
def missingNumber(nums : list[int]) -> int:
	n = len(nums)
	expected = n * (n + 1) // 2
	actual = sum(nums)
	return expected - actual
```

```python
# solution 2
return sum(range(len(nums) + 1)) - sum(nums)
```

#### Notes:

- solution 1: # This is my initial solution, where we are taking advantage of the fact that given a natural number n, we know that sum of numbers from 0 upto n is n(n + 1)/2. 
- Thus, actual sum of num list will not be equal to expected number!
- Second one is by another youtuber *stoney codes*
- Both are O(n) complexity. 