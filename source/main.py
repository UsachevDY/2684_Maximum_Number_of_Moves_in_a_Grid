from typing import List


class Solution:

    def maxMoves(self, grid: List[List[int]]) -> int:
        steps = []
        max_row_len = len(grid[0])
        moves = 0
        for _ in range(len(grid)):
            row = [-1] * max_row_len
            row[0] = 0
            steps.append(row)

        for column in range(max_row_len - 1):
            for row in range(len(grid)):
                if steps[row][column] != -1:
                    for next_row, next_col in [(row - 1, column + 1), (row, column + 1), (row + 1, column + 1)]:
                        if 0 <= next_row < len(grid) and grid[row][column] < \
                                grid[next_row][next_col]:
                            next_step = steps[row][column] + 1
                            steps[next_row][next_col] = next_step
                            moves = max(moves, next_step)

        return moves
