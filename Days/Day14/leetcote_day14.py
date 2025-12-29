# Largest 3-same-Digit number in string

import re

def largestGoodInteger(self, num: str) -> str:
    matches = re.findall(r'(\d)\1\1', num)

    return max(matches, default='') * 3 if matches else ''




# Divide Array Into Equal Pairs



def divideArray(self, nums: list[int]) -> bool:
    bit = 0
    for num in nums:
        bit ^= (1 << num)  # Toggle the bit at position 'num'

    return bit == 0