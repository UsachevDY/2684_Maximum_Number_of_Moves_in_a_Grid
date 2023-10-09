from unittest import TestCase

from main import Solution


class TestSolution(TestCase):

    def test_1(self):
        grid = [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]
        expected = 3
        result = Solution().maxMoves(grid)
        self.assertEqual(expected, result)

    def test_2(self):
        grid = [[3, 2, 4], [2, 1, 9], [1, 1, 7]]
        expected = 0
        result = Solution().maxMoves(grid)
        self.assertEqual(expected, result)

    def test_3(self):
        max_size = 1000
        grid = []
        for i in range(max_size):
            array = [0] * max_size
            grid.append(array)
        grid[max_size - 1] = list(range(max_size))
        expected = max_size - 1
        result = Solution().maxMoves(grid)
        self.assertEqual(expected, result)

    def test_4(self):
        grid = [
            [3, 2],
            [2, 1],
            [1, 4]
        ]
        expected = 1
        result = Solution().maxMoves(grid)
        self.assertEqual(expected, result)

    def test_5(self):
        grid = [[187, 167, 209, 251, 152, 236, 263, 128, 135], [267, 249, 251, 285, 73, 204, 70, 207, 74],
                [189, 159, 235, 66, 84, 89, 153, 111, 189], [120, 81, 210, 7, 2, 231, 92, 128, 218],
                [193, 131, 244, 293, 284, 175, 226, 205, 245]]
        expected = 3
        result = Solution().maxMoves(grid)
        self.assertEqual(expected, result)
