import random


def test_sort_list_of_ints():
    ints = [random.randint(-1000, 1000) for _ in range(2, 100)]  # Different each time
    result = sorted(ints)
    assert all(x <= y for x, y in zip(result, result[1:]))
