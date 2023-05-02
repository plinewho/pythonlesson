
def prime_numbers(n):
    response = []
    for i in range(2,n+1):
        isPrime = True
        for j in range(2,i):
            if i % j == 0: 
                isPrime = False
                break
        if isPrime:
            response.append(i)
    return response

assert prime_numbers(10) == [2, 3, 5, 7]
assert prime_numbers(20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert prime_numbers(5) == [2, 3, 5]