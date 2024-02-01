from trapping_rain_water import Solution


def test_ex1():
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert solution.trap(height) == 6


def test_ex2():
    solution = Solution()
    height = [4, 2, 0, 3, 2, 5]
    assert solution.trap(height) == 9
