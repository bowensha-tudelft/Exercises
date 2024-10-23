def fizz_buzz(n):
    if n <= 0:
        return 'Failed'
    elif n % 3 == 0:
        if n % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return n

def test_fb():
    assert fizz_buzz(-1) == 'Failed'
    assert fizz_buzz(0) == 'Failed'
    assert fizz_buzz(3) == 'Fizz'
    assert fizz_buzz(5) == 'Buzz'
    assert fizz_buzz(15) == 'FizzBuzz'
    assert fizz_buzz(1) == 1