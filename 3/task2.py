def check_palindrome(s: str) -> bool:
    return True if s == s[::-1] else False

def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("level") == True
    assert check_palindrome("") == True
    assert check_palindrome("a") == True
    assert check_palindrome("ab") == False
    print("All test_check_palindrome passed!")

test_check_palindrome()