# https://www.codewars.com//kata/570a6a46455d08ff8d001002
def no_boring_zeros(n):
    lst = list(str(n))

    for el in lst[::-1]:
        if len(lst) == 1:
            break
        elif el == '0':
            lst.pop(-1)
        else:
            break

    return int(''.join(lst))

if __name__ == '__main__':
    print(no_boring_zeros(21000))
