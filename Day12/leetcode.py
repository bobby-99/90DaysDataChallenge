# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
    

# 2878. Ways to Express an Integer as Sum of Powers

class Solution:
    def numberOfWays(self, n, x):
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            val = i**x
            if val <= n:
                for i in range(n, val - 1, -1):
                    dp[i] = (dp[i] + dp[i - val])
            else:
                break

        return dp[n] % mod
    