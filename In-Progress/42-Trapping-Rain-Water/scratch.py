N = 10


def min_time(c1: int, c2: int) -> int:
    if c1 > c2:
        return min(c1 - c2, c2 + N - c1)
    else:
        return min(c2 - c1, c1 + N - c2)


print(min_time(1, 9))
print(min_time(9, 4))
print(min_time(4, 4))
print(min_time(4, 8))
