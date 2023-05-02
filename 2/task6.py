def remove_odd_numbers(lst):
    response = []
    for i in lst:
        if i % 2 == 0:
            response.append(i)
    return response

assert remove_odd_numbers([1, 2, 3, 4, 5]) == [2, 4]
assert remove_odd_numbers([10, 11, 12, 13, 14]) == [10, 12, 14]
assert remove_odd_numbers([2, 4, 6, 8, 10]) == [2, 4, 6, 8, 10]