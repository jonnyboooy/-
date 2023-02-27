# https://www.codewars.com/kata/588463cae61257e44600006d/train/python
def magical_well(a, b, n):
    return sum((a+i)*(b+i) for i in range(0, n))