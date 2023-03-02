def max_number(*arr, low=0, hi=1):
    max_el = -1000000000
    for el in arr:
        if el > max_el:
            max_el = el

    if max_el <= low:
        return low
    elif max_el >= hi:
        return hi
    else:
        return max_el

if __name__ == '__main__':
    print(max_number(1, 2, 5, 2, 5, 7, 3, 7, low=0, hi=4))
