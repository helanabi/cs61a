def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
    return minutes

# Find positive integers x and y (with x < y <= 2 * x), for which either:
#  race(x, y) returns the wrong value or
#  race(x, y) runs forever

# Solution:

# race(x, y) returns the wrong value for any x and y such that:
# 5*y != k*x, for any integer k. e.g. x=2, y=3.

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    i = 1
    while i <= n:
        say = ''
        if i % 3 == 0:
            say = "fizz"
        if i % 5 == 0:
            say += "buzz"
        print(say or i)
        i += 1

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    if n == 1:
        return False
    
    i = 2
    while i < n:
        if n % i == 0: 
            return False
        i += 1
    return True

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    if not n:
        return 1

    counter = 0
    while n > 0:
        n, d = n // 10, n % 10
        if not has_digit(n, d):
            counter += 1
    return counter

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    if n == k == 0:
        return True
    
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False
