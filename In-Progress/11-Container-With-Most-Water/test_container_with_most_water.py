from container_with_most_water import Solution


def test_ex1():
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert solution.maxArea(height) == 49