def fact(n):
    if n< 0:
        raise ValueError("n must be a non-negative integer")
    result =1
    for i in range(1, n+1):
        result *= i

    return result


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
    