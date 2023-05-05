def create_name_age_strings(names: list, ages: list) -> list:
    response = []
    for index, item in enumerate(names):
        response.append(f'{item} - {ages[index]}')
    return response     

def test_create_name_age_strings():
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    expected = ["Alice - 25", "Bob - 30", "Charlie - 35"]
    result = create_name_age_strings(names, ages)
    assert result == expected

    names = []
    ages = []
    expected = []
    result = create_name_age_strings(names, ages)
    assert result == expected
    print("All test_create_name_age_strings pass")
test_create_name_age_strings()