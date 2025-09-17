from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert sum(split_integer(19, 5)) == 19
    assert sum(split_integer(3, 5)) == 3


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(12, 3) == [4, 4, 4]
    assert split_integer(20, 5) == [4, 4, 4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(99, 1) == [99]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == [4, 4, 4, 5]  # конкретно очікуваний результат
    result = split_integer(32, 6)
    assert result == [5, 5, 5, 5, 6, 6]


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    result = split_integer(3, 5)
    assert result == [0, 0, 1, 1, 1]  # саме так треба розподілити
    assert len(result) == 5


def test_difference_between_min_and_max_not_greater_than_one() -> None:
    result = split_integer(25, 4)
    assert max(result) - min(result) <= 1
    assert result == [6, 6, 6, 7]


def test_all_parts_are_integers() -> None:
    result = split_integer(50, 7)
    assert all(isinstance(x, int) for x in result)
