# For finding second Largest digit in a Alphanumeric Array

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
inpp = input("Num")
uuu = secondHighest(inpp)
print(uuu)