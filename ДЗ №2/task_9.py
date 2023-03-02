# https://www.codewars.com/kata/59974515b4c40be3cc000263/train/python
from fractions import Fraction

def friendly_numbers(m, n):
    mm = m
    nn = n
    sum = [0, 0]

    while mm != 0:
        if m % mm == 0:
            sum[0] += mm
        mm -= 1

    while nn != 0:
        if n % nn == 0:
            sum[1] += nn
        nn -= 1

    if sum[0] / m == sum[1] / n:
        return 'Friendly!'
    else:
        return f'{Fraction(sum[0], m)} {Fraction(sum[1], n)}'

if __name__ == '__main__':
    print(friendly_numbers(6, 28))
