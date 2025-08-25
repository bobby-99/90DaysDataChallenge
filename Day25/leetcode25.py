# 498. Diagonal Travese

from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row = col = 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):
            result.append(mat[row][col])

            if direction == 1:  # Moving up-right
                if col == n - 1:  # Last column
                    row += 1
                    direction = -1
                elif row == 0:  # First row
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:  # Moving down-left
                if row == m - 1:  # Last row
                    col += 1
                    direction = 1
                elif col == 0:  # First column
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result
