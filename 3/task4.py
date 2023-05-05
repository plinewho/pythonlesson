def sum_of_digits(n: int, remainder=0) -> int:
    response = int(str(n)[0]) + remainder
    if(len(str(n)) == 1):
        return response
    return sum_of_digits(int(str(n)[1:]), response)


def test_sum_of_digits():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5) == 5
    assert sum_of_digits(10) == 1
    assert sum_of_digits(12345) == 15
    assert sum_of_digits(999999999999999) == 135
    print("All test_sum_of_digits pass")

test_sum_of_digits()