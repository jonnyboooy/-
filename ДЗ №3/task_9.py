# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python
def unique_in_order(sequence):
    if len(sequence) == 0:
        return []
    l = 0
    r = 1
    result = []

    while l != len(sequence) - 1:
        if sequence[l] != sequence[r]:
            result.append(sequence[l])

        l += 1
        r += 1

    result.append(sequence[-1])

    return result

if __name__ == '__main__':
    print(unique_in_order("AAAABBBCCDAABBB"))
