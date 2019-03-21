import hypothesis

from hypothesis import strategies as st


@hypothesis.given(st.lists(st.integers(), min_size=2))
def test_sort_list_of_ints(generated_ints):
    print(generated_ints)
    result = sorted(generated_ints)
    assert all(x <= y for x, y in zip(result, result[1:]))
