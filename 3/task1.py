def get_odd_doubled_numbers(numbers: list) -> list:
    filter_list = filter(lambda x: True if x % 2 != 0 else False, numbers)
    return list(map(lambda x: x*2, list(filter_list)))

def test_get_odd_doubled_numbers():
    assert get_odd_doubled_numbers([1, 2, 3, 4, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([10, 20, 30]) == []
    assert get_odd_doubled_numbers([]) == []
    assert get_odd_doubled_numbers([1, 3, 5]) == [2, 6, 10]
    assert get_odd_doubled_numbers([2, 4, 6]) == []
    print("All test_get_odd_doubled_numbers passed!")

test_get_odd_doubled_numbers()