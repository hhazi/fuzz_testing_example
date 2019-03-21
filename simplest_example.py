def test_sort_list_of_ints():
    ints = [1, 5, 4, 3, 2]

    result = sorted(ints)

    assert result == [1, 2, 3, 4, 5]
