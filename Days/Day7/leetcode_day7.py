# 20. Check Paranthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False