def max_number(arr, low=0, hi=1):
    max_el = -1000000000
    for el in arr:
        if low <= el <= hi and el > max_el:
            max_el = el

    return max_el

if __name__ == '__main__':
    print(max_number([4, 1, 7, 3, 1, 6, 8], low=0, hi=5))